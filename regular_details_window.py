from PyQt5.QtWidgets import QWidget, QMessageBox
from PyQt5.QtCore import QDate
import datetime
from regular_payment_window import Ui_RegularWindow
from dateutil.relativedelta import relativedelta
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QDoubleValidator
from CONSTANTS import *
import CONSTANTS


def show_regular_list(self):
    self.regular_list.clear()
    payments = CURSOR.execute(
        f"""SELECT name, category, amount FROM payment_details WHERE paymentId = {CONSTANTS.ID}""").fetchall()
    self.regular_list.addItems([f"{i[0]}\t{i[1]}\t{i[-1]}" for i in payments])


class PaymentDetails(QWidget, Ui_RegularWindow):
    def __init__(self, main):
        super().__init__()
        self.setupUi(self)

        self.main = main

        current_day = datetime.date.today()
        self.start_date.setDate(QDate(current_day.day, current_day.month, current_day.year))

        self.payment_amount.setValidator(QDoubleValidator(1, 999999999, 2))

        self.type_of_payment = None
        self.radio_group.buttonClicked.connect(self.type)
        self.frequency = self.frequency_box.currentText()
        self.date = self.start_date.date()
        self.category = self.category_box.currentText()

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
        que = "INSERT INTO payment_details(paymentId, amount, category, type, name, date, frequency) " \
              "VALUES"
        que += f"('{CONSTANTS.ID}', {self.amount}, '{self.category}', '{self.type_of_payment}', '{self.name}', " \
               f"'{self.date.toString('yyyy-MM-dd')}', '{self.frequency}')"

        try:
            CURSOR.execute(que)
        except:
            self.error_msg("Платеж с таким именем уже существует")

        CONNECTION.commit()
