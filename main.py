import sys

from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget
from PyQt5.QtWidgets import QLineEdit, QListWidgetItem, QTableWidgetItem
from PyQt5.QtCore import Qt
from main_page import Ui_MainPage
from first_pages import Ui_MainWindow
from string import digits, ascii_lowercase, ascii_uppercase, ascii_letters
import hashlib
import sqlite3
from currency_converter import CurrencyConverter
import datetime


class EntrancePage(QWidget, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.move(0, 0)

        self.connection = sqlite3.connect("accounts_db.db")
        self.cursor = self.connection.cursor()

        try:
            with open("remember_me_file.txt", 'r', encoding='utf8') as file:
                data = file.read().split(';')
                if data[0] == "True":
                    self.remember_me_check_box.setChecked(True)
                    self.input_email.setText(data[1])
                    self.input_password.setText(data[2])
        except FileNotFoundError:
            pass

        self.sign_up_button.clicked.connect(self.go_to_register_page)
        self.go_back_button.clicked.connect(self.go_back_to_sign_in_page)
        self.sign_up_button_2.clicked.connect(self.go_main_page)
        self.sign_in_button.clicked.connect(self.go_main_page)
        self.show_password.stateChanged.connect(self.show_or_hide_existing_password)
        self.show_new_password.stateChanged.connect(self.show_or_hide_created_password)
        self.show_repeated_password.stateChanged.connect(self.show_or_hide_repeated_password)

    def show_or_hide_existing_password(self):
        check_box = self.sender()
        if check_box.isChecked():
            self.input_password.setEchoMode(QLineEdit.Normal)
        else:
            self.input_password.setEchoMode(QLineEdit.Password)

    def show_or_hide_created_password(self):
        check_box = self.sender()
        if check_box.isChecked():
            self.create_password.setEchoMode(QLineEdit.Normal)
        else:
            self.create_password.setEchoMode(QLineEdit.Password)

    def show_or_hide_repeated_password(self):
        check_box = self.sender()
        if check_box.isChecked():
            self.repeat_password.setEchoMode(QLineEdit.Normal)
        else:
            self.repeat_password.setEchoMode(QLineEdit.Password)

    def go_to_register_page(self):
        self.stacked_widget.setCurrentWidget(self.sign_up_widget)
        self.create_email.setFocus()

    def go_back_to_sign_in_page(self):
        self.stacked_widget.setCurrentWidget(self.sign_in_widget)

    def go_main_page(self):
        if self.stacked_widget.currentIndex() == 0:
            if not self.check_data_sign_in_page():
                return

        else:
            if not self.check_data_sign_up_page():
                return

        email = self.input_email.text()
        password = self.input_password.text()

        with open("remember_me_file.txt", 'w', encoding='utf8') as file:
            if self.remember_me_check_box.isChecked():
                file.write(f"True;{email};{password}")
            else:
                file.write("False;")

        self.close()
        self.main_page = MainPage(self.connection, email)
        self.main_page.show()

    def check_data_sign_in_page(self):
        password = self.input_password.text()
        email = self.input_email.text()
        list_of_emails = self.cursor.execute("""SELECT email FROM accounts
                        WHERE email = ?""", (email,)).fetchall()
        if len(list_of_emails) != 0 and hashlib.sha1(password.encode()).hexdigest() == \
                self.cursor.execute("""SELECT password FROM accounts
                WHERE email = ?""", (email,)).fetchone()[0]:
            return True
        else:
            self.password_error_text.setText("Неверный e-mail или пароль")

    def check_data_sign_up_page(self):
        password_1 = self.create_password.text()
        password_2 = self.repeat_password.text()
        email = self.create_email.text()

        self.password_error_text.setText("")
        self.error_repeat_password.setText("")
        self.error_new_password.setText("")

        if not self.check_email_correctness(email):
            if self.stacked_widget.currentIndex() == 0:
                self.password_error_text.setText("Неверный e-mail или пароль")
            else:
                self.error_repeat_password.setText("Неверный e-mail")
            return False

        if len(password_1) < 8:
            self.error_new_password.setText("Длина пароля меньше 8 символов")
            return False

        if not set(password_1).intersection(set(digits)):
            self.error_new_password.setText("Пароль не содержит цифры")
            return False

        if not set(password_1).intersection(set(ascii_letters)):
            self.error_new_password.setText("Пароль не содержит буквы")
            return False

        if not set(password_1).intersection(set(ascii_uppercase)):
            self.error_new_password.setText("Пароль не содержит заглавные буквы")
            return False

        if not set(password_1).intersection(set(ascii_lowercase)):
            self.error_new_password.setText("Пароль не содержит строчные буквы")
            return False

        if password_1 != password_2:
            self.error_repeat_password.setText("Пароли не совпадают")
            return False

        self.cursor.execute("""INSERT INTO accounts(email, password) VALUES(?, ?)""",
                            (email, hashlib.sha1(password_1.encode()).hexdigest()))
        self.connection.commit()
        return True

    def check_email_correctness(self, mail):
        if '@' not in mail or mail[0] == '@' or mail[-1] == '@':
            return False
        if '.' not in mail or mail[0] == '.' or mail[-1] == '.':
            return False
        return True


class MainPage(QWidget, Ui_MainPage):
    def __init__(self, database, cur_email, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        self.cursor = database
        self.list_of_pages.itemSelectionChanged.connect(self.change_page)
        self.convert_button.clicked.connect(self.convert_money)
        self.show_rates_button.clicked.connect(self.show_exchange_rates)
        self.quit_button.clicked.connect(self.go_sign_in_page_from_main_page)
        self.current_email.setText(f"{cur_email}")

        today = datetime.datetime.today()
        self.years_box.setCurrentText(f"{today.year}")
        self.months_box.setCurrentText(f"{today.month}")
        self.days_box.setCurrentText(f"{today.day}")

    def go_sign_in_page_from_main_page(self):
        self.close()
        self.entrance_page = EntrancePage()
        self.entrance_page.show()

    def change_page(self):
        page_name = self.list_of_pages.selectedItems()[0]

        if page_name.text() == 'Диаграмма':
            self.stacked_main_pages.setCurrentWidget(self.diagramm_page)
        elif page_name.text() == 'График':
            self.stacked_main_pages.setCurrentWidget(self.schedule_page)
        elif page_name.text() == 'Регулярные платежи':
            self.stacked_main_pages.setCurrentWidget(self.regular_page)
        elif page_name.text() == 'Конвертер валют':
            self.stacked_main_pages.setCurrentWidget(self.converter_page)
        elif page_name.text() == 'Курс валют':
            self.stacked_main_pages.setCurrentWidget(self.exchange_page)
        elif page_name.text() == 'Профиль':
            self.stacked_main_pages.setCurrentWidget(self.profile_page)
        else:
            self.stacked_main_pages.setCurrentWidget(self.settings_page)

    def convert_money(self):
        start_money = float(self.available_sum.text())
        start_currency = self.available_currency.currentText()
        end_currency = self.required_currency.currentText()

        if start_currency == "Имеющаяся валюта:" or \
                end_currency == "Нужная валюта:":
            return

        c = CurrencyConverter(decimal=True)
        converted = c.convert(start_money, start_currency, end_currency)
        self.required_sum.setText(f"{round(converted, 4)}")

    def show_exchange_rates(self):
        conv = CurrencyConverter(decimal=True, fallback_on_wrong_date=True,
                                 fallback_on_missing_rate=True)
        date = datetime.date(int(self.years_box.currentText()),
                             int(self.months_box.currentText()),
                             int(self.days_box.currentText()))
        for i in range(32):
            price_in_rubles = conv.convert(1, f"{self.rates_table.item(i, 0).text()}", 'RUB',
                                           date=date)
            self.rates_table.setItem(
                i, 1, QTableWidgetItem(f"{round(price_in_rubles, 4)}"))
            self.rates_table.item(i, 1).setTextAlignment(Qt.AlignRight)


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = EntrancePage()
    ex.show()
    sys.excepthook = except_hook
    sys.exit(app.exec_())
