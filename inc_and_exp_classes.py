import expenses_window
import incomes_window
from PyQt5.QtWidgets import QWidget, QGridLayout, QListWidgetItem
from PyQt5.QtGui import QDoubleValidator, QIcon
from PyQt5 import sip
import CONSTANTS
from CONSTANTS import *
from db_queries import *
from plot_class import MplCanvas


def show_expenditure_pie(self):
    percents = []

    categories = ["Кафе", "Здоровье", "Продукты", "Транспорт", "Другое"]

    data = get_exp_data()
    expenditure = get_total_exp()
    used_categories = [i[2] for i in data]

    for idx, value in enumerate(categories):
        if value not in used_categories:
            percents.append(0)
        else:
            index_of_value = used_categories.index(value)
            percent = data[index_of_value][1] / expenditure * 100
            percents.append(percent)

    colors = ['#E2CF2C', '#FF2646', '#8FCCFB', '#1C98FF', '#FF22A1']
    construct_pie_plot(self, percents, colors, expenditure, self.frame_for_expenditures_pie)


def show_income_pie(self):
    percents = []

    data = get_inc_data()

    income = get_total_inc()
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
    construct_pie_plot(self, percents, colors, income, self.frame_for_incomes_pie)


def construct_pie_plot(self, values, colors_list, amount, obj):
    text = f"Сумма: {amount}"

    cur_lay = obj.layout()
    if cur_lay:
        sip.delete(cur_lay)
    framelayout = QGridLayout()

    sc = MplCanvas(self)
    if not sum(values):
        colors_list = ['#696d6e']
        values = [100]
        text = "Нет данных"
    sc.axes.pie(values, wedgeprops=dict(width=0.5, edgecolor='#004445'), colors=colors_list)
    sc.axes.text(0, -1.2, text, color='w', horizontalalignment='center', verticalalignment='top')
    framelayout.addWidget(sc)
    obj.setLayout(framelayout)
    add_operation_to_list(self)


def add_operation_to_list(self):
    icons_for_categories = {"Кафе": "./icons/cafe.png",
                            "Здоровье": "./icons/health.png",
                            "Продукты": "./icons/meal.png",
                            "Транспорт": "./icons/transport.png",
                            "Другое": "./icons/other.png",
                            "Зарплата": "./icons/salary.png",
                            "Подарок": "./icons/gift.png"}
    exp_list = self.list_for_expenditures
    inc_list = self.list_for_incomes


    exp_list.clear()
    inc_list.clear()

    exp_data = get_exp_data()
    inc_data = get_inc_data()

    for elem in exp_data:
        item = QListWidgetItem(f"{elem[-1]}\t\t\t{elem[1]}")
        item.setIcon(QIcon(icons_for_categories[elem[-1]]))
        exp_list.addItem(item)

    for elem in inc_data:
        item = QListWidgetItem(f"{elem[-1]}\t\t\t{elem[1]}")
        item.setIcon(QIcon(icons_for_categories[elem[-1]]))
        inc_list.addItem(item)


class ExpWindow(QWidget, expenses_window.Ui_Form):
    def __init__(self, main):
        super().__init__()
        self.setupUi(self)

        self.main = main

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
                add_exp((CONSTANTS.ID, amount_float, self.categories[category]))
            except:
                update_exp((amount_float, self.categories[category]))
            update_total_exp((amount_float, CONSTANTS.ID))

            deduct_from_balance((amount_float, CONSTANTS.ID))
            self.main.balance_label.setText(str(get_amount()))

            CONNECTION.commit()
            self.close()
            show_expenditure_pie(self.main)


class IncWindow(QWidget, incomes_window.Ui_Form):
    def __init__(self, main):
        super().__init__()
        self.setupUi(self)

        self.main = main

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
                add_inc((CONSTANTS.ID, amount_float, self.categories[category]))
            except:
                update_inc((amount_float, self.categories[category]))
            update_total_inc((amount_float, CONSTANTS.ID))

            add_to_balance((amount_float, CONSTANTS.ID))
            self.main.balance_label.setText(str(get_amount()))

            CONNECTION.commit()
            self.close()
            show_income_pie(self.main)
