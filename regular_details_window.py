from PyQt5.QtWidgets import QWidget, QMessageBox
from PyQt5.QtCore import QDate
import datetime
from dateutil.relativedelta import relativedelta
from regular_payment_window import Ui_RegularWindow
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QDoubleValidator
from CONSTANTS import *
import CONSTANTS
from db_queries import *
from inc_and_exp_classes import *


def show_regular_list(self):
    self.regular_list.clear()
    payments = get_payment_details()
    self.regular_list.addItems([f"{i[0]}\t{i[1]}\t{i[2]}\t{i[-1]}" for i in payments])


def write_off_payments(self):
    all_payments = get_all_payments()
    today = datetime.date.today()
    frequency = {"Каждый день": datetime.timedelta(days=1),
                 "Каждый месяц": relativedelta(months=1)}

    for payment in all_payments:
        payment_date = datetime.datetime.strptime(payment[0], '%Y-%m-%d').date()
        if payment_date == today:
            if payment[2] == "income":
                add_to_balance((payment[1], CONSTANTS.ID))
                try:
                    add_inc((CONSTANTS.ID, payment[1], payment[-1]))
                except:
                    update_inc((payment[1], payment[-1]))
                show_expenditure_pie(self)
            else:
                deduct_from_balance((payment[1], CONSTANTS.ID))
                try:
                    add_exp((CONSTANTS.ID, payment[1], payment[-1]))
                except:
                    update_exp((payment[1], payment[-1]))
                show_income_pie(self)

            update_payment_date((today + frequency[payment[3]], payment[-2]))

    add_operation_to_list(self)
    self.balance_label.setText(str(get_amount()))
    CONNECTION.commit()


class PaymentDetails(QWidget, Ui_RegularWindow):
    def __init__(self, main):
        super().__init__()
        self.setupUi(self)

        self.main = main

        current_date = datetime.date.today()
        self.start_date.setDate(QDate(current_date.year, current_date.month, current_date.day))

        self.payment_amount.setValidator(QDoubleValidator(1, 999999999, 2))

        self.type_of_payment = None
        self.radio_group.buttonClicked.connect(self.type)

        self.create_payment.clicked.connect(self.create)

    def type(self):
        if self.expenditure_radio.isChecked():
            self.type_of_payment = "expenditure"
        else:
            self.type_of_payment = "income"

    def create(self):
        if not self.type_of_payment or not self.payment_amount.text() or not self.payment_name.text():
            self.error_msg("Заполните все поля")
        else:
            self.name = self.payment_name.text()
            self.amount = round(float(self.payment_amount.text().replace(',', '.')), 2)

            self.save_to_db()

            self.close()
        show_regular_list(self.main)
        write_off_payments(self.main)

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

    def save_to_db(self):
        date = self.start_date.date()
        frequency = self.frequency_box.currentText()
        category = self.category_box.currentText()
        try:
            save_payment((CONSTANTS.ID, self.amount, category, self.type_of_payment, self.name,
                          date.toString('yyyy-MM-dd'), frequency))
        except:
            self.error_msg("Платеж с таким именем уже существует")

        CONNECTION.commit()
