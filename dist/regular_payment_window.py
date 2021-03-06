# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'regular_payment_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_RegularWindow(object):
    def setupUi(self, RegularWindow):
        RegularWindow.setObjectName("RegularWindow")
        RegularWindow.resize(759, 589)
        RegularWindow.setStyleSheet("background-color: #021c1e;")
        self.gridLayout = QtWidgets.QGridLayout(RegularWindow)
        self.gridLayout.setObjectName("gridLayout")
        self.frame = QtWidgets.QFrame(RegularWindow)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.formLayout = QtWidgets.QFormLayout(self.frame)
        self.formLayout.setHorizontalSpacing(10)
        self.formLayout.setObjectName("formLayout")
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.frequency_label = QtWidgets.QLabel(self.frame)
        self.frequency_label.setStyleSheet("color: white;\n"
"font-size: 11px;")
        self.frequency_label.setObjectName("frequency_label")
        self.gridLayout_3.addWidget(self.frequency_label, 0, 0, 1, 1)
        self.frequency_box = QtWidgets.QComboBox(self.frame)
        self.frequency_box.setMinimumSize(QtCore.QSize(110, 23))
        self.frequency_box.setMaximumSize(QtCore.QSize(110, 16777215))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.frequency_box.setFont(font)
        self.frequency_box.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.frequency_box.setStyleSheet("QComboBox:drop-down {\n"
"    background-color: transparent;\n"
"}\n"
"\n"
"QComboBox {\n"
"    border: none;\n"
"    color: #6fb98f;\n"
"    font-size: 12px;\n"
"}")
        self.frequency_box.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToContents)
        self.frequency_box.setObjectName("frequency_box")
        self.frequency_box.addItem("")
        self.frequency_box.addItem("")
        self.gridLayout_3.addWidget(self.frequency_box, 1, 0, 1, 1)
        self.formLayout.setLayout(2, QtWidgets.QFormLayout.LabelRole, self.gridLayout_3)
        self.gridLayout_4 = QtWidgets.QGridLayout()
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.start_date_label = QtWidgets.QLabel(self.frame)
        self.start_date_label.setMinimumSize(QtCore.QSize(148, 0))
        self.start_date_label.setStyleSheet("color: white;\n"
"font-size: 11px;")
        self.start_date_label.setObjectName("start_date_label")
        self.gridLayout_4.addWidget(self.start_date_label, 0, 0, 1, 1)
        self.start_date = QtWidgets.QDateEdit(self.frame)
        self.start_date.setMinimumSize(QtCore.QSize(120, 0))
        self.start_date.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.start_date.setStyleSheet("QDateEdit {\n"
"    color: #6fb98f;\n"
"    font-size: 12px;\n"
"}\n"
"\n"
"QDateEdit::QToolButton  {\n"
"    background-color: transparent;\n"
"}")
        self.start_date.setWrapping(False)
        self.start_date.setFrame(False)
        self.start_date.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.start_date.setCorrectionMode(QtWidgets.QAbstractSpinBox.CorrectToPreviousValue)
        self.start_date.setKeyboardTracking(True)
        self.start_date.setProperty("showGroupSeparator", False)
        self.start_date.setObjectName("start_date")
        self.gridLayout_4.addWidget(self.start_date, 1, 0, 1, 1)
        self.formLayout.setLayout(4, QtWidgets.QFormLayout.LabelRole, self.gridLayout_4)
        self.gridLayout_5 = QtWidgets.QGridLayout()
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.time_label = QtWidgets.QLabel(self.frame)
        self.time_label.setStyleSheet("color: white;\n"
"font-size: 11px;")
        self.time_label.setObjectName("time_label")
        self.gridLayout_5.addWidget(self.time_label, 0, 0, 1, 1)
        self.start_time = QtWidgets.QTimeEdit(self.frame)
        self.start_time.setMinimumSize(QtCore.QSize(110, 0))
        self.start_time.setStyleSheet("QTimeEdit {\n"
"    color: #6fb98f;\n"
"    font-size: 12px;\n"
"}\n"
"\n"
"QTimeEdit:drop-down {\n"
"    background-color: transparent;\n"
"}")
        self.start_time.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.start_time.setObjectName("start_time")
        self.gridLayout_5.addWidget(self.start_time, 1, 0, 1, 1)
        self.formLayout.setLayout(6, QtWidgets.QFormLayout.LabelRole, self.gridLayout_5)
        self.gridLayout_6 = QtWidgets.QGridLayout()
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.category_label = QtWidgets.QLabel(self.frame)
        self.category_label.setStyleSheet("color: white;\n"
"font-size: 11px;")
        self.category_label.setObjectName("category_label")
        self.gridLayout_6.addWidget(self.category_label, 0, 0, 1, 1)
        self.category_box = QtWidgets.QComboBox(self.frame)
        self.category_box.setMinimumSize(QtCore.QSize(110, 23))
        self.category_box.setStyleSheet("QComboBox:drop-down {\n"
"    background-color: transparent;\n"
"}\n"
"\n"
"QComboBox {\n"
"    border: none;\n"
"    color: #6fb98f;\n"
"    font-size: 12px;\n"
"}")
        self.category_box.setObjectName("category_box")
        self.category_box.addItem("")
        self.category_box.addItem("")
        self.category_box.addItem("")
        self.category_box.addItem("")
        self.category_box.addItem("")
        self.category_box.addItem("")
        self.gridLayout_6.addWidget(self.category_box, 1, 0, 1, 1)
        self.formLayout.setLayout(8, QtWidgets.QFormLayout.LabelRole, self.gridLayout_6)
        self.gridLayout_7 = QtWidgets.QGridLayout()
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.payment_amount = QtWidgets.QLineEdit(self.frame)
        self.payment_amount.setStyleSheet("border: 2px solid transparent;\n"
"border-bottom: 2px ridge #6fb98f;\n"
"color: white;")
        self.payment_amount.setLocale(QtCore.QLocale(QtCore.QLocale.German, QtCore.QLocale.Germany))
        self.payment_amount.setInputMethodHints(QtCore.Qt.ImhNone)
        self.payment_amount.setInputMask("")
        self.payment_amount.setFrame(True)
        self.payment_amount.setCursorMoveStyle(QtCore.Qt.LogicalMoveStyle)
        self.payment_amount.setClearButtonEnabled(False)
        self.payment_amount.setObjectName("payment_amount")
        self.gridLayout_7.addWidget(self.payment_amount, 1, 0, 1, 1)
        self.sum_label = QtWidgets.QLabel(self.frame)
        self.sum_label.setStyleSheet("color: white;\n"
"font-size: 11px;")
        self.sum_label.setObjectName("sum_label")
        self.gridLayout_7.addWidget(self.sum_label, 0, 0, 1, 1)
        self.formLayout.setLayout(10, QtWidgets.QFormLayout.LabelRole, self.gridLayout_7)
        self.gridLayout_9 = QtWidgets.QGridLayout()
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.payment_name = QtWidgets.QLineEdit(self.frame)
        self.payment_name.setStyleSheet("border: 2px solid transparent;\n"
"border-bottom: 2px ridge #6fb98f;\n"
"color: white;")
        self.payment_name.setObjectName("payment_name")
        self.gridLayout_9.addWidget(self.payment_name, 2, 0, 1, 1)
        self.name_label = QtWidgets.QLabel(self.frame)
        self.name_label.setStyleSheet("color: white;\n"
"font-size: 11px;")
        self.name_label.setObjectName("name_label")
        self.gridLayout_9.addWidget(self.name_label, 1, 0, 1, 1)
        self.formLayout.setLayout(12, QtWidgets.QFormLayout.LabelRole, self.gridLayout_9)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.formLayout.setItem(1, QtWidgets.QFormLayout.LabelRole, spacerItem)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.formLayout.setItem(3, QtWidgets.QFormLayout.LabelRole, spacerItem1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.formLayout.setItem(5, QtWidgets.QFormLayout.LabelRole, spacerItem2)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.formLayout.setItem(7, QtWidgets.QFormLayout.LabelRole, spacerItem3)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.formLayout.setItem(9, QtWidgets.QFormLayout.LabelRole, spacerItem4)
        self.create_payment = QtWidgets.QPushButton(self.frame)
        self.create_payment.setMinimumSize(QtCore.QSize(200, 40))
        self.create_payment.setStyleSheet("QPushButton{\n"
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
        self.create_payment.setObjectName("create_payment")
        self.formLayout.setWidget(12, QtWidgets.QFormLayout.FieldRole, self.create_payment)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.type_of_reg = QtWidgets.QLabel(self.frame)
        self.type_of_reg.setStyleSheet("color: white;\n"
"font-size: 11px;")
        self.type_of_reg.setObjectName("type_of_reg")
        self.gridLayout_2.addWidget(self.type_of_reg, 0, 0, 1, 1)
        self.expenditure_radio = QtWidgets.QRadioButton(self.frame)
        self.expenditure_radio.setMinimumSize(QtCore.QSize(80, 0))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.expenditure_radio.setFont(font)
        self.expenditure_radio.setStyleSheet("color: #6fb98f;")
        self.expenditure_radio.setObjectName("expenditure_radio")
        self.radio_group = QtWidgets.QButtonGroup(RegularWindow)
        self.radio_group.setObjectName("radio_group")
        self.radio_group.addButton(self.expenditure_radio)
        self.gridLayout_2.addWidget(self.expenditure_radio, 1, 0, 1, 1)
        self.income_radio = QtWidgets.QRadioButton(self.frame)
        self.income_radio.setMinimumSize(QtCore.QSize(80, 0))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.income_radio.setFont(font)
        self.income_radio.setStyleSheet("color: #6fb98f;")
        self.income_radio.setObjectName("income_radio")
        self.radio_group.addButton(self.income_radio)
        self.gridLayout_2.addWidget(self.income_radio, 1, 1, 1, 1)
        self.formLayout.setLayout(0, QtWidgets.QFormLayout.LabelRole, self.gridLayout_2)
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.formLayout.setItem(11, QtWidgets.QFormLayout.LabelRole, spacerItem5)
        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)

        self.retranslateUi(RegularWindow)
        QtCore.QMetaObject.connectSlotsByName(RegularWindow)

    def retranslateUi(self, RegularWindow):
        _translate = QtCore.QCoreApplication.translate
        RegularWindow.setWindowTitle(_translate("RegularWindow", "Form"))
        self.frequency_label.setText(_translate("RegularWindow", "?????????????????????????? ??????????????????????"))
        self.frequency_box.setItemText(0, _translate("RegularWindow", "???????????? ??????????"))
        self.frequency_box.setItemText(1, _translate("RegularWindow", "???????????? ????????"))
        self.start_date_label.setText(_translate("RegularWindow", "???????? ???????????? ??????????????????????"))
        self.time_label.setText(_translate("RegularWindow", "??????????"))
        self.category_label.setText(_translate("RegularWindow", "??????????????????"))
        self.category_box.setItemText(0, _translate("RegularWindow", "????????"))
        self.category_box.setItemText(1, _translate("RegularWindow", "??????????????????????"))
        self.category_box.setItemText(2, _translate("RegularWindow", "??????????????????"))
        self.category_box.setItemText(3, _translate("RegularWindow", "????????????????"))
        self.category_box.setItemText(4, _translate("RegularWindow", "????????????????"))
        self.category_box.setItemText(5, _translate("RegularWindow", "????????????"))
        self.sum_label.setText(_translate("RegularWindow", "??????????"))
        self.name_label.setText(_translate("RegularWindow", "???????????????????????? ??????????????"))
        self.create_payment.setText(_translate("RegularWindow", "??????????????"))
        self.type_of_reg.setText(_translate("RegularWindow", "?????? ??????????????"))
        self.expenditure_radio.setText(_translate("RegularWindow", "??????????????"))
        self.income_radio.setText(_translate("RegularWindow", "????????????"))
