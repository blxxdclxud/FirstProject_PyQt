import sys
from PyQt5.QtWidgets import QWidget, QApplication, QHBoxLayout, QLabel
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt


class CustomView(QWidget):
    def __init__(self, text, img, parent=None):
        QWidget.__init__(self, parent)

        self._text = text
        self._img = img

        self.setLayout(QHBoxLayout())
        self.setMaximumSize(860, 30)
        self.icon = QLabel(self)
        self.label = QLabel(self)
        self.label.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        self.label.setStyleSheet("""color: #FFFFFF;
                                    font-family: Segoe UI;
                                    font-size: 14px""")

        self.layout().addWidget(self.icon)
        self.layout().addWidget(self.label)
        self.layout().setAlignment(Qt.AlignRight)

        self.create_custom_view()

    def create_custom_view(self):
        self.icon.setPixmap(QPixmap(self._img).scaled(10, 10, Qt.KeepAspectRatio))
        self.label.setText(self._text)
