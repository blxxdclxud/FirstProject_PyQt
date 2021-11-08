# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'first_pages.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1384, 763)
        MainWindow.setStyleSheet("background-color: #021c1e;\n"
"")
        self.gridLayout_2 = QtWidgets.QGridLayout(MainWindow)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.mw_grid = QtWidgets.QGridLayout()
        self.mw_grid.setSpacing(0)
        self.mw_grid.setObjectName("mw_grid")
        self.frame_2 = QtWidgets.QFrame(MainWindow)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.gridLayout = QtWidgets.QGridLayout(self.frame_2)
        self.gridLayout.setObjectName("gridLayout")
        self.stacked_widget = QtWidgets.QStackedWidget(self.frame_2)
        self.stacked_widget.setObjectName("stacked_widget")
        self.sign_in_widget = QtWidgets.QWidget()
        self.sign_in_widget.setObjectName("sign_in_widget")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.sign_in_widget)
        self.gridLayout_4.setObjectName("gridLayout_4")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_4.addItem(spacerItem, 2, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem1, 3, 0, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem2, 3, 2, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_4.addItem(spacerItem3, 4, 1, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_4.addItem(spacerItem4, 5, 1, 1, 1)
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setHorizontalSpacing(0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.show_password = QtWidgets.QCheckBox(self.sign_in_widget)
        self.show_password.setStyleSheet("QCheckBox:indicator:checked{    \n"
"    image: url(./icons/visibility.png);\n"
"}\n"
"QCheckBox:indicator:unchecked{    \n"
"    image: url(./icons/visibility (1).png);\n"
"}")
        self.show_password.setText("")
        self.show_password.setObjectName("show_password")
        self.gridLayout_3.addWidget(self.show_password, 2, 1, 1, 1)
        self.input_email = QtWidgets.QLineEdit(self.sign_in_widget)
        self.input_email.setMinimumSize(QtCore.QSize(320, 35))
        font = QtGui.QFont()
        font.setFamily("MS Reference Sans Serif")
        font.setPointSize(9)
        self.input_email.setFont(font)
        self.input_email.setAutoFillBackground(False)
        self.input_email.setStyleSheet("border: 2px solid transparent;\n"
"border-bottom: 2px ridge #6fb98f;\n"
"color: white;")
        self.input_email.setText("")
        self.input_email.setReadOnly(False)
        self.input_email.setClearButtonEnabled(False)
        self.input_email.setObjectName("input_email")
        self.gridLayout_3.addWidget(self.input_email, 0, 0, 1, 1)
        self.email_error_text = QtWidgets.QLabel(self.sign_in_widget)
        self.email_error_text.setMaximumSize(QtCore.QSize(16777215, 30))
        self.email_error_text.setStyleSheet("color: red;")
        self.email_error_text.setText("")
        self.email_error_text.setAlignment(QtCore.Qt.AlignCenter)
        self.email_error_text.setObjectName("email_error_text")
        self.gridLayout_3.addWidget(self.email_error_text, 1, 0, 1, 1)
        self.password_error_text = QtWidgets.QLabel(self.sign_in_widget)
        self.password_error_text.setMaximumSize(QtCore.QSize(1000, 30))
        self.password_error_text.setStyleSheet("color: red;")
        self.password_error_text.setText("")
        self.password_error_text.setAlignment(QtCore.Qt.AlignCenter)
        self.password_error_text.setObjectName("password_error_text")
        self.gridLayout_3.addWidget(self.password_error_text, 4, 0, 1, 1)
        self.input_password = QtWidgets.QLineEdit(self.sign_in_widget)
        self.input_password.setMinimumSize(QtCore.QSize(320, 35))
        font = QtGui.QFont()
        font.setFamily("MS Reference Sans Serif")
        font.setPointSize(9)
        self.input_password.setFont(font)
        self.input_password.setStyleSheet("border: 2px solid transparent;\n"
"border-bottom: 2px ridge #6fb98f;\n"
"color: white;")
        self.input_password.setLocale(QtCore.QLocale(QtCore.QLocale.Russian, QtCore.QLocale.Russia))
        self.input_password.setText("")
        self.input_password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.input_password.setObjectName("input_password")
        self.gridLayout_3.addWidget(self.input_password, 2, 0, 1, 1)
        self.sign_in_button = QtWidgets.QPushButton(self.sign_in_widget)
        font = QtGui.QFont()
        font.setFamily("MS Reference Sans Serif")
        font.setPointSize(10)
        self.sign_in_button.setFont(font)
        self.sign_in_button.setStyleSheet("QPushButton {\n"
"    color: #6fb98f;\n"
"}\n"
"QPushButton:pressed {\n"
"    color: #2c7873\n"
"}")
        self.sign_in_button.setAutoDefault(False)
        self.sign_in_button.setDefault(False)
        self.sign_in_button.setFlat(True)
        self.sign_in_button.setObjectName("sign_in_button")
        self.gridLayout_3.addWidget(self.sign_in_button, 6, 0, 1, 1)
        self.sign_up_button = QtWidgets.QPushButton(self.sign_in_widget)
        self.sign_up_button.setMinimumSize(QtCore.QSize(0, 41))
        font = QtGui.QFont()
        font.setFamily("MS Reference Sans Serif")
        font.setPointSize(10)
        self.sign_up_button.setFont(font)
        self.sign_up_button.setStyleSheet("QPushButton{\n"
"    background-color: #2c7873;\n"
"    color: #021c1e;\n"
"    border: 2px solid #2c7873;\n"
"    border-radius: 20;\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color: #5d9e9a;\n"
"    color: #021c1e;\n"
"    border: 2px solid #2c7873;\n"
"    border-radius: 20;\n"
"}")
        self.sign_up_button.setFlat(True)
        self.sign_up_button.setObjectName("sign_up_button")
        self.gridLayout_3.addWidget(self.sign_up_button, 8, 0, 1, 1)
        self.remember_me_check_box = QtWidgets.QCheckBox(self.sign_in_widget)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.remember_me_check_box.setFont(font)
        self.remember_me_check_box.setStyleSheet("color: #ffffff")
        self.remember_me_check_box.setObjectName("remember_me_check_box")
        self.gridLayout_3.addWidget(self.remember_me_check_box, 5, 0, 1, 1)
        self.gridLayout_4.addLayout(self.gridLayout_3, 3, 1, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_4.addItem(spacerItem5, 0, 1, 1, 1)
        self.phrase = QtWidgets.QLabel(self.sign_in_widget)
        self.phrase.setEnabled(True)
        font = QtGui.QFont()
        font.setFamily("MS Reference Sans Serif")
        font.setPointSize(11)
        self.phrase.setFont(font)
        self.phrase.setStyleSheet("color: white;\n"
"")
        self.phrase.setAlignment(QtCore.Qt.AlignCenter)
        self.phrase.setObjectName("phrase")
        self.gridLayout_4.addWidget(self.phrase, 1, 1, 1, 1)
        self.stacked_widget.addWidget(self.sign_in_widget)
        self.sign_up_widget = QtWidgets.QWidget()
        self.sign_up_widget.setObjectName("sign_up_widget")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.sign_up_widget)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.gridLayout_5 = QtWidgets.QGridLayout()
        self.gridLayout_5.setHorizontalSpacing(0)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.create_password = QtWidgets.QLineEdit(self.sign_up_widget)
        self.create_password.setMinimumSize(QtCore.QSize(40, 35))
        font = QtGui.QFont()
        font.setFamily("MS Reference Sans Serif")
        font.setPointSize(9)
        self.create_password.setFont(font)
        self.create_password.setAutoFillBackground(False)
        self.create_password.setStyleSheet("border: 2px solid transparent;\n"
"border-bottom: 2px ridge #6fb98f;\n"
"color: white;")
        self.create_password.setInputMask("")
        self.create_password.setText("")
        self.create_password.setFrame(True)
        self.create_password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.create_password.setDragEnabled(False)
        self.create_password.setReadOnly(False)
        self.create_password.setCursorMoveStyle(QtCore.Qt.LogicalMoveStyle)
        self.create_password.setClearButtonEnabled(False)
        self.create_password.setObjectName("create_password")
        self.gridLayout_5.addWidget(self.create_password, 4, 0, 1, 1)
        self.error_new_password = QtWidgets.QLabel(self.sign_up_widget)
        font = QtGui.QFont()
        font.setFamily("MS Reference Sans Serif")
        font.setPointSize(8)
        self.error_new_password.setFont(font)
        self.error_new_password.setStyleSheet("color: red;")
        self.error_new_password.setText("")
        self.error_new_password.setObjectName("error_new_password")
        self.gridLayout_5.addWidget(self.error_new_password, 5, 0, 1, 1)
        self.repeat_password = QtWidgets.QLineEdit(self.sign_up_widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.repeat_password.sizePolicy().hasHeightForWidth())
        self.repeat_password.setSizePolicy(sizePolicy)
        self.repeat_password.setMinimumSize(QtCore.QSize(40, 35))
        font = QtGui.QFont()
        font.setFamily("MS Reference Sans Serif")
        font.setPointSize(9)
        self.repeat_password.setFont(font)
        self.repeat_password.setAutoFillBackground(False)
        self.repeat_password.setStyleSheet("border: 2px solid transparent;\n"
"border-bottom: 2px ridge #6fb98f;\n"
"color: white;")
        self.repeat_password.setText("")
        self.repeat_password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.repeat_password.setReadOnly(False)
        self.repeat_password.setClearButtonEnabled(False)
        self.repeat_password.setObjectName("repeat_password")
        self.gridLayout_5.addWidget(self.repeat_password, 6, 0, 1, 1)
        self.create_email = QtWidgets.QLineEdit(self.sign_up_widget)
        self.create_email.setMinimumSize(QtCore.QSize(40, 35))
        font = QtGui.QFont()
        font.setFamily("MS Reference Sans Serif")
        font.setPointSize(9)
        self.create_email.setFont(font)
        self.create_email.setAutoFillBackground(False)
        self.create_email.setStyleSheet("\n"
"    border: 2px solid transparent;\n"
"    border-bottom: 2px ridge #6fb98f;\n"
"    color: white;\n"
"")
        self.create_email.setText("")
        self.create_email.setReadOnly(False)
        self.create_email.setObjectName("create_email")
        self.gridLayout_5.addWidget(self.create_email, 2, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.sign_up_widget)
        font = QtGui.QFont()
        font.setFamily("MS Reference Sans Serif")
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: white")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout_5.addWidget(self.label_2, 3, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.sign_up_widget)
        font = QtGui.QFont()
        font.setFamily("MS Reference Sans Serif")
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setStyleSheet("color: white")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout_5.addWidget(self.label, 1, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.sign_up_widget)
        font = QtGui.QFont()
        font.setFamily("MS Reference Sans Serif")
        font.setPointSize(8)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color: white;")
        self.label_5.setObjectName("label_5")
        self.gridLayout_5.addWidget(self.label_5, 11, 0, 1, 1)
        self.error_repeat_password = QtWidgets.QLabel(self.sign_up_widget)
        font = QtGui.QFont()
        font.setFamily("MS Reference Sans Serif")
        font.setPointSize(8)
        self.error_repeat_password.setFont(font)
        self.error_repeat_password.setStyleSheet("color: red;")
        self.error_repeat_password.setText("")
        self.error_repeat_password.setObjectName("error_repeat_password")
        self.gridLayout_5.addWidget(self.error_repeat_password, 7, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.sign_up_widget)
        font = QtGui.QFont()
        font.setFamily("MS Reference Sans Serif")
        font.setPointSize(8)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: white;")
        self.label_4.setObjectName("label_4")
        self.gridLayout_5.addWidget(self.label_4, 9, 0, 1, 1)
        self.sign_up_button_2 = QtWidgets.QPushButton(self.sign_up_widget)
        self.sign_up_button_2.setMinimumSize(QtCore.QSize(0, 41))
        self.sign_up_button_2.setMaximumSize(QtCore.QSize(16777215, 41))
        font = QtGui.QFont()
        font.setFamily("MS Reference Sans Serif")
        font.setPointSize(10)
        self.sign_up_button_2.setFont(font)
        self.sign_up_button_2.setStyleSheet("QPushButton{\n"
"    background-color: #2c7873;\n"
"    color: #021c1e;\n"
"    border: 2px solid #2c7873;\n"
"    border-radius: 20;\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color: #5d9e9a;\n"
"    color: #021c1e;\n"
"    border: 2px solid #2c7873;\n"
"    border-radius: 20;\n"
"}")
        self.sign_up_button_2.setFlat(True)
        self.sign_up_button_2.setObjectName("sign_up_button_2")
        self.gridLayout_5.addWidget(self.sign_up_button_2, 13, 0, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.sign_up_widget)
        font = QtGui.QFont()
        font.setFamily("MS Reference Sans Serif")
        font.setPointSize(8)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("color: white;")
        self.label_7.setObjectName("label_7")
        self.gridLayout_5.addWidget(self.label_7, 10, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.sign_up_widget)
        font = QtGui.QFont()
        font.setFamily("MS Reference Sans Serif")
        font.setPointSize(8)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: white;")
        self.label_3.setObjectName("label_3")
        self.gridLayout_5.addWidget(self.label_3, 8, 0, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.sign_up_widget)
        font = QtGui.QFont()
        font.setFamily("MS Reference Sans Serif")
        font.setPointSize(8)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("color: white;")
        self.label_8.setObjectName("label_8")
        self.gridLayout_5.addWidget(self.label_8, 12, 0, 1, 1)
        self.show_new_password = QtWidgets.QCheckBox(self.sign_up_widget)
        self.show_new_password.setStyleSheet("QCheckBox:indicator:checked{    \n"
"    image: url(./icons/visibility.png);\n"
"}\n"
"QCheckBox:indicator:unchecked{    \n"
"    image: url(./icons/visibility (1).png);\n"
"}")
        self.show_new_password.setText("")
        self.show_new_password.setObjectName("show_new_password")
        self.gridLayout_5.addWidget(self.show_new_password, 4, 1, 1, 1)
        self.show_repeated_password = QtWidgets.QCheckBox(self.sign_up_widget)
        self.show_repeated_password.setStyleSheet("QCheckBox:indicator:checked{    \n"
"    image: url(./icons/visibility.png);\n"
"}\n"
"QCheckBox:indicator:unchecked{    \n"
"    image: url(./icons/visibility (1).png);\n"
"}")
        self.show_repeated_password.setText("")
        self.show_repeated_password.setObjectName("show_repeated_password")
        self.gridLayout_5.addWidget(self.show_repeated_password, 6, 1, 1, 1)
        self.go_back_button = QtWidgets.QPushButton(self.sign_up_widget)
        self.go_back_button.setMaximumSize(QtCore.QSize(50, 16777215))
        self.go_back_button.setStyleSheet("QPushButton {    \n"
"    height: 50px;\n"
"    width: 50px;\n"
"    border-radius: 20%;\n"
"}\n"
"QPushButton:pressed {\n"
"    height: 50px;\n"
"    width: 50px;\n"
"    border-radius: 20%;\n"
"    background-color: #525252;\n"
"}  \n"
"")
        self.go_back_button.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons/arrow.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon.addPixmap(QtGui.QPixmap("icons/arrow_p.png"), QtGui.QIcon.Active, QtGui.QIcon.On)
        self.go_back_button.setIcon(icon)
        self.go_back_button.setIconSize(QtCore.QSize(24, 24))
        self.go_back_button.setFlat(False)
        self.go_back_button.setObjectName("go_back_button")
        self.gridLayout_5.addWidget(self.go_back_button, 0, 0, 1, 1)
        self.gridLayout_6.addLayout(self.gridLayout_5, 1, 1, 1, 1)
        spacerItem6 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_6.addItem(spacerItem6, 0, 1, 1, 1)
        spacerItem7 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_6.addItem(spacerItem7, 2, 1, 1, 1)
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_6.addItem(spacerItem8, 1, 2, 1, 1)
        spacerItem9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_6.addItem(spacerItem9, 1, 0, 1, 1)
        self.stacked_widget.addWidget(self.sign_up_widget)
        self.gridLayout.addWidget(self.stacked_widget, 1, 0, 1, 1)
        self.mw_grid.addWidget(self.frame_2, 2, 1, 1, 1)
        self.logo_frame = QtWidgets.QFrame(MainWindow)
        self.logo_frame.setMinimumSize(QtCore.QSize(0, 80))
        self.logo_frame.setMaximumSize(QtCore.QSize(16777215, 80))
        self.logo_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.logo_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.logo_frame.setObjectName("logo_frame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.logo_frame)
        self.verticalLayout.setContentsMargins(-1, 9, 9, 9)
        self.verticalLayout.setSpacing(40)
        self.verticalLayout.setObjectName("verticalLayout")
        self.logo = QtWidgets.QLabel(self.logo_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.logo.sizePolicy().hasHeightForWidth())
        self.logo.setSizePolicy(sizePolicy)
        self.logo.setText("")
        self.logo.setPixmap(QtGui.QPixmap("icons/logo.png"))
        self.logo.setAlignment(QtCore.Qt.AlignCenter)
        self.logo.setObjectName("logo")
        self.verticalLayout.addWidget(self.logo)
        self.mw_grid.addWidget(self.logo_frame, 1, 1, 1, 1)
        self.gridLayout_2.addLayout(self.mw_grid, 0, 0, 1, 1)

        self.retranslateUi(MainWindow)
        self.stacked_widget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Form"))
        self.input_email.setWhatsThis(_translate("MainWindow", "<html><head/><body><p><br/></p></body></html>"))
        self.input_email.setPlaceholderText(_translate("MainWindow", "Введите e-mail"))
        self.input_password.setPlaceholderText(_translate("MainWindow", "Введите пароль"))
        self.sign_in_button.setText(_translate("MainWindow", "Войти"))
        self.sign_up_button.setText(_translate("MainWindow", "Регистрация"))
        self.remember_me_check_box.setText(_translate("MainWindow", "Запомнить меня"))
        self.phrase.setText(_translate("MainWindow", "Войдите в аккаунт, чтобы не потерять данные"))
        self.create_password.setWhatsThis(_translate("MainWindow", "<html><head/><body><p><br/></p></body></html>"))
        self.create_password.setPlaceholderText(_translate("MainWindow", "Пример: Gradskiy1201"))
        self.repeat_password.setWhatsThis(_translate("MainWindow", "<html><head/><body><p><br/></p></body></html>"))
        self.repeat_password.setPlaceholderText(_translate("MainWindow", "Введите пароль еще раз"))
        self.create_email.setWhatsThis(_translate("MainWindow", "<html><head/><body><p><br/></p></body></html>"))
        self.create_email.setPlaceholderText(_translate("MainWindow", "Например: ivanov@gmail.com"))
        self.label_2.setText(_translate("MainWindow", "Введите пароль"))
        self.label.setText(_translate("MainWindow", "Введите электроную почту"))
        self.label_5.setText(_translate("MainWindow", "• Пароль должен содержать как строчные,"))
        self.label_4.setText(_translate("MainWindow", "• Пароль должен состоять из букв латинского"))
        self.sign_up_button_2.setText(_translate("MainWindow", "Зарегистрировать"))
        self.label_7.setText(_translate("MainWindow", "алфавита(A-z) и арабских цифр(0-9)."))
        self.label_3.setText(_translate("MainWindow", "• Длина пароля должна быть не менее 8 символов."))
        self.label_8.setText(_translate("MainWindow", "так и заглавные буквы."))
