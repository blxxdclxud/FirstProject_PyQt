import sys

from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget
from main_page import Ui_MainPage
from first_pages import Ui_MainWindow
from string import digits, ascii_lowercase, ascii_uppercase, ascii_letters


class EntrancePage(QWidget, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.sign_up_button.clicked.connect(self.run)
        self.go_back_button.clicked.connect(self.back)
        self.sign_up_button_2.clicked.connect(self.go_main_page)
        self.sign_in_button.clicked.connect(self.go_main_page)

    def run(self):
        self.stacked_widget.setCurrentWidget(self.sign_up_widget)
        self.create_email.setFocus()

    def back(self):
        self.stacked_widget.setCurrentWidget(self.sign_in_widget)

    def go_main_page(self):
        if self.check_password_sign_in_page() or \
                self.check_password_sign_up_page():
            self.close()
            self.main_page = MainPage()
            self.main_page.show()

    def check_password_sign_in_page(self):
        password_1 = self.input_password.text()
        pass

    def check_password_sign_up_page(self):
        password_1 = self.create_password.text()
        password_2 = self.repeat_password.text()

        if len(password_1) != 0:
            if len(password_1) < 8:
                self.error_new_password.setText("Длина пароля меньше 8 символов")
                return False
            else:
                self.error_new_password.setText("")
                self.error_repeat_password.setText("")

            if not set(password_1).intersection(set(digits)):
                self.error_new_password.setText("Пароль не содержит цифры")
                return False
            else:
                self.error_new_password.setText("")
                self.error_repeat_password.setText("")

            if not set(password_1).intersection(set(ascii_letters)):
                self.error_new_password.setText("Пароль не содержит буквы")
                return False
            else:
                self.error_new_password.setText("")
                self.error_repeat_password.setText("")

            if not set(password_1).intersection(set(ascii_uppercase)):
                self.error_new_password.setText("Пароль не содержит заглавные буквы")
                return False
            else:
                self.error_new_password.setText("")
                self.error_repeat_password.setText("")

            if not set(password_1).intersection(set(ascii_lowercase)):
                self.error_new_password.setText("Пароль не содержит строчные буквы")
                return False
            else:
                self.error_new_password.setText("")
                self.error_repeat_password.setText("")

            if password_1 != password_2:
                self.error_repeat_password.setText("Пароли не совпадают")
                return False
            else:
                self.error_new_password.setText("")
                self.error_repeat_password.setText("")
                return True


class MainPage(QWidget, Ui_MainPage):
    def __init__(self):
        super().__init__()
        self.setupUi(self)


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = EntrancePage()
    ex.show()
    sys.excepthook = except_hook
    sys.exit(app.exec_())
