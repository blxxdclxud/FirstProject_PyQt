from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QLineEdit, QListWidgetItem, QTableWidgetItem
from PyQt5.QtCore import Qt
from main_page import Ui_MainPage
import sqlite3
from currency_converter import CurrencyConverter
import datetime
import sqlite3


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
