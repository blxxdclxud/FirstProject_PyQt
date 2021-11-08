import expenses_window
import incomes_window
from PyQt5.QtWidgets import QWidget
from PyQt5.QtGui import QDoubleValidator
import CONSTANTS
from CONSTANTS import *


class ExpWindow(QWidget, expenses_window.Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.amount_exp.setValidator(QDoubleValidator(1, 999999999, 2))

        self.add_exp_btn.clicked.connect(self.add_func)

        self.categories = {0: "Кафе",
                           1: "Здоровье",
                           2: "Продукты",
                           3: "Транспорт",
                           4: "Другое"}

    def add_func(self):
        if self.amount_exp.text() and self.exp_category_list.currentIndex() != -1:
            category = self.exp_category_list.currentRow()
            amount_float = round(float(self.amount_exp.text().replace(",", ".")), 2)

            try:
                CURSOR.execute("""INSERT INTO expenditures(expenditureId, amount, category) VALUES(?, ?, ?)""",
                               (CONSTANTS.ID, amount_float, self.categories[category]))
            except:
                CURSOR.execute("""UPDATE expenditures 
                                  SET amount = amount + ?
                                  WHERE category = ?""",
                               (amount_float, self.categories[category]))
            CURSOR.execute("""UPDATE details
                              SET expenditure = expenditure + ?
                              WHERE detailId = ?""", (amount_float, CONSTANTS.ID))
            CONNECTION.commit()
            self.close()


class IncWindow(QWidget, incomes_window.Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.amount_inc.setValidator(QDoubleValidator(1, 999999999, 2))

        self.add_inc_btn.clicked.connect(self.add_func)

        self.categories = {0: "Зарплата",
                           1: "Подарок",
                           2: "Другое"}

    def add_func(self):
        if self.amount_inc.text() and self.inc_category_list.currentRow() != -1:
            category = self.inc_category_list.currentRow()
            amount_float = round(float(self.amount_inc.text().replace(",", ".")), 2)

            try:
                CURSOR.execute("""INSERT INTO incomes(incomeId, amount, category) VALUES(?, ?, ?)""",
                               (CONSTANTS.ID, amount_float, self.categories[category]))
            except:
                CURSOR.execute("""UPDATE incomes 
                                  SET amount = amount + ?
                                  WHERE category = ?""",
                               (amount_float, self.categories[category]))
            CURSOR.execute("""UPDATE details
                                SET income = income + ?
                                WHERE detailId = ?""", (amount_float, CONSTANTS.ID))
            CONNECTION.commit()
            self.close()
