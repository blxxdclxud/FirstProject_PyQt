from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QLineEdit, QListWidgetItem, QTableWidgetItem
from PyQt5.QtCore import Qt
from first_pages import Ui_MainWindow
from string import digits, ascii_lowercase, ascii_uppercase, ascii_letters
import hashlib
import main_window as mw
from CONSTANTS import *


class EntrancePage(QWidget, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.move(0, 0)

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

        page_idx = self.stacked_widget.currentIndex()
        if page_idx == 0:
            email = self.input_email.text()
            password = self.input_password.text()
        else:
            email = self.create_email.text()
            password = self.create_password.text()

        with open("remember_me_file.txt", 'w', encoding='utf8') as file:
            if self.remember_me_check_box.isChecked():
                file.write(f"True;{email};{password}")
            else:
                file.write("False;")
        self.close()
        self.main_page = mw.MainPage(email)
        self.main_page.show()
        self.main_page.check_accounts_list()

    def check_data_sign_in_page(self):
        password = self.input_password.text()
        email = self.input_email.text()
        list_of_emails = CURSOR.execute("""SELECT email FROM accounts
                        WHERE email = ?""", (email,)).fetchall()
        if len(list_of_emails) != 0 and hashlib.sha1(password.encode()).hexdigest() == \
                CURSOR.execute("""SELECT password FROM accounts
                WHERE email = ?""", (email,)).fetchone()[0]:
            return True
        else:
            self.password_error_text.setText("???????????????? e-mail ?????? ????????????")

    def check_data_sign_up_page(self):
        password_1 = self.create_password.text()
        password_2 = self.repeat_password.text()
        email = self.create_email.text()

        self.password_error_text.setText("")
        self.error_repeat_password.setText("")
        self.error_new_password.setText("")

        if not self.check_email_correctness(email):
            if self.stacked_widget.currentIndex() == 0:
                self.password_error_text.setText("???????????????? e-mail ?????? ????????????")
            else:
                self.error_repeat_password.setText("???????????????? e-mail")
            return False

        if len(password_1) < 8:
            self.error_new_password.setText("?????????? ???????????? ???????????? 8 ????????????????")
            return False

        if not set(password_1).intersection(set(digits)):
            self.error_new_password.setText("???????????? ???? ???????????????? ??????????")
            return False

        if not set(password_1).intersection(set(ascii_letters)):
            self.error_new_password.setText("???????????? ???? ???????????????? ??????????")
            return False

        if not set(password_1).intersection(set(ascii_uppercase)):
            self.error_new_password.setText("???????????? ???? ???????????????? ?????????????????? ??????????")
            return False

        if not set(password_1).intersection(set(ascii_lowercase)):
            self.error_new_password.setText("???????????? ???? ???????????????? ???????????????? ??????????")
            return False

        if password_1 != password_2:
            self.error_repeat_password.setText("???????????? ???? ??????????????????")
            return False

        CURSOR.execute("""INSERT INTO accounts(email, password) VALUES(?, ?)""",
                       (email, hashlib.sha1(password_1.encode()).hexdigest()))
        CONNECTION.commit()
        return True

    @staticmethod
    def check_email_correctness(mail):
        if '@' not in mail or mail[0] == '@' or mail[-1] == '@':
            return False
        if '.' not in mail or mail[0] == '.' or mail[-1] == '.':
            return False
        return True
