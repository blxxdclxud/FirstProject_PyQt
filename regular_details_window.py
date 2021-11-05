from PyQt5.QtWidgets import QWidget, QMessageBox
from PyQt5.QtCore import QDate
import datetime
from regular_payment_window import Ui_RegularWindow
from dateutil.relativedelta import relativedelta
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QDoubleValidator
from CONSTANTS import *


class PaymentDetails(QWidget, Ui_RegularWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        current_day = datetime.date.today()
        self.start_date.setDate(QDate(current_day.day, current_day.month, current_day.year))

        self.payment_amount.setValidator(QDoubleValidator(1, 999999999, 2))

        self.type_of_payment = None
        self.radio_group.buttonClicked.connect(self.type)
        self.frequency = self.frequency_box.currentText()
        self.date = self.start_date.date()
        self.time = self.start_time.time()
        self.category = self.category_box.currentText()

        self.create_payment.clicked.connect(self.create)

    def type(self):
        if self.expenditure_radio.isChecked():
            self.type_of_payment = "expenditure"
        else:
            self.type_of_payment = "income"

    def create(self):
        if not self.type_of_payment or not self.payment_amount.text() or not self.payment_name.text():
            self.error_msg()
        else:
            self.name = self.payment_name.text()
            self.amount = round(float(self.payment_amount.text().replace(',', '.')), 2)

            self.save_to_db()

            self.close()

    @staticmethod
    def error_msg():
        msg = QMessageBox()
        msg.setWindowFlags(Qt.FramelessWindowHint)
        msg.setText("Заполните все поля")
        msg.setIcon(QMessageBox.Warning)
        msg.setStyleSheet("""background-color: #021c1e;
                                            color: #ffffff;
                                            font-size: 13px;""")
        msg.exec_()

    def save_to_db(self):
        que = "INSERT INTO payment_details(amount, category, type, name, time, date, frequency) " \
              "VALUES"
        que += f"({self.amount}, '{self.category}', '{self.type_of_payment}', '{self.name}', " \
               f"'{self.time.toString()}', '{self.date.toString('yyyy-MM-dd')}', '{self.frequency}')"

        CURSOR.execute(que)

        id_from_payment = CURSOR.execute("""SELECT paymentId FROM payment_details
                                    WHERE name = ?""", (self.name,)).fetchone()[0]
        CURSOR.execute("""INSERT INTO regular_payments(paymentId) VALUES(?)""", (id_from_payment,))

        CONNECTION.commit()
