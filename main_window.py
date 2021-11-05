from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QLineEdit, QListWidgetItem, QTableWidgetItem, QMessageBox
from PyQt5.QtCore import Qt
from main_page import Ui_MainPage
import sqlite3
from currency_converter import CurrencyConverter
from forex_python.converter import CurrencyRates, RatesNotAvailableError
import datetime
import sqlite3
from custom_view_for_rates import CustomView
from regular_details_window import PaymentDetails
from requests.exceptions import ConnectionError
from CONSTANTS import *


class MainPage(QWidget, Ui_MainPage):
    def __init__(self, cur_email, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        self.list_of_pages.itemSelectionChanged.connect(self.change_page)
        self.convert_button.clicked.connect(self.convert_money)
        self.show_rates_button.clicked.connect(self.show_exchange_rates)
        self.quit_button.clicked.connect(self.go_sign_in_page_from_main_page)
        self.create_regular_button.clicked.connect(self.create_regular)
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

        cur = CurrencyConverter(decimal=True)

        try:
            converted = cur.convert(start_money, start_currency, end_currency)
        except ConnectionError:
            self.no_internet_msg()
            return

        self.required_sum.setText(f"{round(converted, 4)}")

    def show_exchange_rates(self):
        conv = CurrencyRates()

        try:
            list_of_currencies = list(conv.get_rates("RUB").keys())
        except ConnectionError:
            self.no_internet_msg()
            return

        selected_date = datetime.date(int(self.years_box.currentText()),
                                      int(self.months_box.currentText()),
                                      int(self.days_box.currentText()))

        if selected_date.year == 2005 and selected_date.month <= 4 and selected_date.day < 4:
            self.out_of_range()
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
    def no_internet_msg():
        msg = QMessageBox()
        msg.setWindowFlags(Qt.FramelessWindowHint)
        msg.setText("Нет подключения к интернету")
        msg.setIcon(QMessageBox.Warning)
        msg.setStyleSheet("""background-color: #021c1e;
                            color: #ffffff;
                            font-size: 13px;""")
        msg.exec_()

    @staticmethod
    def out_of_range():
        msg = QMessageBox()
        msg.setWindowFlags(Qt.FramelessWindowHint)
        msg.setText("Самая ранняя дата начала отсчета курса валют 04.04.2005")
        msg.setIcon(QMessageBox.Warning)
        msg.setStyleSheet("""background-color: #021c1e;
                                    color: #ffffff;
                                    font-size: 13px;""")
        msg.exec_()

    def create_regular(self):
        self.pay_window = PaymentDetails()
        self.pay_window.show()

    def delete_regular(self):
        row = self.regular_list.currentRow()
        if row != -1:
            CURSOR.execute("""DELETE FROM regular_payments
                                WHERE paymentId =(
                                SELECT paymentId FROM payment_details
                                    WHERE name = ?""", (self.regular_list.currentItem().text(),))
            self.regular_list.takeItem(row)
