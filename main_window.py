from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QLineEdit, QListWidgetItem, QTableWidgetItem, QMessageBox, QGridLayout, QInputDialog
from PyQt5.QtCore import Qt
from main_page import Ui_MainPage
from inc_and_exp_classes import *
from plot_class import MplCanvas
import sqlite3
from currency_converter import CurrencyConverter
from forex_python.converter import CurrencyRates, RatesNotAvailableError
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.figure import Figure
import datetime
import sqlite3
from custom_view_for_rates import CustomView
from regular_details_window import PaymentDetails, show_regular_list
from requests.exceptions import ConnectionError
from CONSTANTS import *
import CONSTANTS
from entrance_window import *


class MainPage(QWidget, Ui_MainPage):
    def __init__(self, cur_email, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        CONSTANTS.ID = CURSOR.execute("""SELECT id FROM accounts WHERE email = ?""", (cur_email,)).fetchone()[0]
        CONSTANTS.EXPENDITURE = CURSOR.execute("""SELECT expenditure FROM details WHERE detailId = ?""",
                                               (CONSTANTS.ID,))
        CONSTANTS.INCOME = CURSOR.execute("""SELECT income FROM details WHERE detailId = ?""",
                                          (CONSTANTS.ID,))
        try:
            assert CURSOR.execute("""SELECT detailId FROM details WHERE detailId = ?""", (CONSTANTS.ID,)).fetchall()
        except:
            CURSOR.execute("""INSERT INTO details (detailId) VALUES(?)""", (CONSTANTS.ID,))
            CONNECTION.commit()
        self.show_expenditure_pie()
        self.show_income_pie()
        show_regular_list(self)
        self.show_description()

        self.list_of_pages.itemSelectionChanged.connect(self.change_page)
        self.convert_button.clicked.connect(self.convert_money)
        self.show_rates_button.clicked.connect(self.show_exchange_rates)
        self.quit_button.clicked.connect(self.go_sign_in_page_from_main_page)
        self.create_regular_button.clicked.connect(self.create_regular)
        self.current_email.setText(f"{cur_email}")
        self.add_expenditure_button.clicked.connect(self.add_expenditure)
        self.add_income_button.clicked.connect(self.add_income)
        self.delete_regular_button.clicked.connect(self.delete_regular)
        self.account_description.textEdited.connect(self.save_description)
        self.add_balance.clicked.connect(self.add_bill)

        today = datetime.datetime.today()
        self.years_box.setCurrentText(f"{today.year}")
        self.months_box.setCurrentText(f"{today.month}")
        self.days_box.setCurrentText(f"{today.day}")

        self.list_of_accounts.addItem(CURSOR.execute("""SELECT name FROM details WHERE detailId = ?""",
                                                     (CONSTANTS.ID,)).fetchone()[0])
        self.balance_label.setText(str(CURSOR.execute("""SELECT amount FROM details WHERE detailId = ?""",
                                                      (CONSTANTS.ID,)).fetchone()[0]))

    def check_accounts_list(self):
        if self.list_of_accounts.count() == 0:
            name, ok_press = QInputDialog.getText(self, "Добавление счета", "Введите имя счета")

            if ok_press:
                self.list_of_accounts.addItem(name)
                CURSOR.execute("""UPDATE details SET name = ? WHERE detailId = ?""", (name, CONSTANTS.ID))
                CONNECTION.commit()

    def go_sign_in_page_from_main_page(self):
        self.close()
        self.entrance_page = EntrancePage()
        self.entrance_page.show()

    def add_bill(self):
        balance, ok_press = QInputDialog.getText(self, "Редактирование суммы", "Введите сумму на счете")

        if ok_press:
            self.balance_label.setText(balance)
            CURSOR.execute("""UPDATE details SET amount = ? WHERE detailId = ?""", (balance, CONSTANTS.ID))
            CONNECTION.commit()

    def save_description(self):
        CURSOR.execute("""UPDATE accounts SET description = ? WHERE id = ?""",
                       (self.account_description.text(), CONSTANTS.ID))
        CONNECTION.commit()

    def show_description(self):
        des = CURSOR.execute("""SELECT description FROM accounts WHERE id = ?""",
                             (CONSTANTS.ID,)).fetchone()[0]
        if des:
            self.account_description.setText(des)

    def change_page(self):
        page_name = self.list_of_pages.selectedItems()[0]

        if page_name.text() == 'Диаграмма':
            self.stacked_main_pages.setCurrentWidget(self.diagramm_page)
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

        cur = CurrencyConverter(decimal=True)

        try:
            converted = cur.convert(start_money, start_currency, end_currency)
        except ConnectionError:
            self.error_msg("Нет подключения к интернету")
            return

        self.required_sum.setText(f"{round(converted, 4)}")

    def show_exchange_rates(self):
        conv = CurrencyRates()

        try:
            list_of_currencies = list(conv.get_rates("RUB").keys())
        except ConnectionError:
            self.error_msg("Нет подключения к интернету")
            return

        selected_date = datetime.date(int(self.years_box.currentText()),
                                      int(self.months_box.currentText()),
                                      int(self.days_box.currentText()))

        if selected_date.year == 2005 and selected_date.month <= 4 and selected_date.day < 4:
            self.error_msg("Самая ранняя дата начала отсчета курса валют 04.04.2005")
            return

        count_for_previous = 1
        while True:
            try:
                previous_date = selected_date - datetime.timedelta(days=count_for_previous)
                rates_for_previous_date = conv.get_rates("RUB", date_obj=previous_date)
            except RatesNotAvailableError:
                count_for_previous += 1
                continue
            else:
                break

        count_for_selected = 0
        while True:
            try:
                selected_date_true = selected_date - datetime.timedelta(days=count_for_selected)
                rates_for_selected_date = conv.get_rates("RUB", date_obj=selected_date_true)
            except RatesNotAvailableError:
                count_for_selected += 1
                continue
            else:
                break

        if not selected_date_true - previous_date:
            previous_date -= datetime.timedelta(days=1)
            rates_for_previous_date = conv.get_rates("RUB", date_obj=previous_date)

        for i in range(COUNT_OF_CURRENCIES):
            try:
                price_of_current_currency = 1 / float(rates_for_selected_date[list_of_currencies[i]])
                price_of_previous_currency = 1 / float(rates_for_previous_date[list_of_currencies[i]])
            except KeyError:
                self.rates_table.setItem(i, 1, QTableWidgetItem("Н/Д"))
                item = self.rates_table.item(i, 1)
                item.setTextAlignment(Qt.AlignRight)
            else:
                if price_of_current_currency > price_of_previous_currency:
                    custom_item = CustomView(f"{round(price_of_current_currency, 4)}",
                                             "./icons/up-arrow.png")
                elif price_of_current_currency < price_of_previous_currency:
                    custom_item = CustomView(f"{round(price_of_current_currency, 4)}",
                                             "./icons/down-arrow.png")
                else:
                    custom_item = CustomView(f"{round(price_of_current_currency, 4)}",
                                             "./icons/equal.png")

                self.rates_table.setCellWidget(i, 1, custom_item)

    @staticmethod
    def error_msg(text):
        msg = QMessageBox()
        msg.setWindowFlags(Qt.FramelessWindowHint)
        msg.setText(text)
        msg.setIcon(QMessageBox.Warning)
        msg.setStyleSheet("""background-color: #021c1e;
                            color: #ffffff;
                            font-size: 13px;""")
        msg.exec_()

    def delete_regular(self):
        row = self.regular_list.currentRow()
        if row != -1:
            CURSOR.execute("""DELETE FROM payment_details
                                WHERE name = ?""", (self.regular_list.currentItem().text().split("\t")[0],))
            self.regular_list.takeItem(row)
            CONNECTION.commit()

    def create_regular(self):
        self.pay_window = PaymentDetails(self)
        self.pay_window.show()
        show_regular_list(self)

    def show_expenditure_pie(self):
        percents = []

        categories = ["Кафе", "Здоровье", "Продукты", "Транспорт", "Другое"]

        data = CURSOR.execute("""SELECT * FROM expenditures WHERE expenditureId = ?""", (CONSTANTS.ID,)).fetchall()
        expenditure = CURSOR.execute("""SELECT expenditure FROM details WHERE detailId = ?""", (CONSTANTS.ID,)).fetchone()[0]
        used_categories = [i[2] for i in data]

        for idx, value in enumerate(categories):
            if value not in used_categories:
                percents.append(0)
            else:
                index_of_value = used_categories.index(value)
                percent = data[index_of_value][1] / expenditure * 100
                percents.append(percent)

        colors = ['#E2CF2C', '#FF2646', '#8FCCFB', '#1C98FF', '#FF22A1']
        self.construct_pie_plot(percents, colors, expenditure)
        self.frame_for_expenditures_pie.setLayout(self.framelayout)

    def show_income_pie(self):
        percents = []

        data = CURSOR.execute("""SELECT * FROM incomes WHERE incomeId = ?""", (CONSTANTS.ID,)).fetchall()

        income = CURSOR.execute("""SELECT income FROM details WHERE detailId = ?""", (CONSTANTS.ID,)).fetchone()[0]
        categories = ["Зарплата", "Подарок", "Другое"]
        used_categories = [i[2] for i in data]

        for idx, value in enumerate(categories):
            if value not in used_categories:
                percents.append(0)
            else:
                index_of_value = used_categories.index(value)
                percent = data[index_of_value][1] / income * 100
                percents.append(percent)

        colors = ['#84A77C', '#28C887', '#FF22A1']
        self.construct_pie_plot(percents, colors, income)
        self.frame_for_incomes_pie.setLayout(self.framelayout)

    def construct_pie_plot(self, values, colors_list, text):
        self.framelayout = QGridLayout()

        sc = MplCanvas(self)

        if not values:
            return
        sc.axes.pie(values, wedgeprops=dict(width=0.5, edgecolor='#004445'), colors=colors_list)
        sc.axes.text(0, -1.2, f"Сумма: {text}", color='w', horizontalalignment='center', verticalalignment='top')
        self.framelayout.addWidget(sc)
        self.frame_for_expenditures_pie.setLayout(self.framelayout)

    def add_expenditure(self):
        self.ew = ExpWindow()
        self.ew.show()

    def add_income(self):
        self.iw = IncWindow()
        self.iw.show()
