import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget


class MyWidget(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('first_pages.ui', self)

        self.sign_up_button.clicked.connect(self.run)
        self.go_back_button.clicked.connect(self.back)

    def run(self):
        self.stacked_widget.setCurrentWidget(self.sign_up_widget)
        self.create_email.setFocus()

    def back(self):
        self.stacked_widget.setCurrentWidget(self.sign_in_widget)


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.excepthook = except_hook
    sys.exit(app.exec_())