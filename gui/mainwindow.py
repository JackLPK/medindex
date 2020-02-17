# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui',
# licensing of 'mainwindow.ui' applies.
#
# Created: Mon Feb 17 01:58:00 2020
#      by: pyside2-uic  running on PySide2 5.13.2
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setSpacing(9)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.left_layout = QtWidgets.QVBoxLayout()
        self.left_layout.setObjectName("left_layout")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.left_layout.addWidget(self.label_7)
        self.out_table = QtWidgets.QTableWidget(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.out_table.setFont(font)
        self.out_table.setObjectName("out_table")
        self.out_table.setColumnCount(0)
        self.out_table.setRowCount(0)
        self.left_layout.addWidget(self.out_table)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.search_bar = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.search_bar.setFont(font)
        self.search_bar.setObjectName("search_bar")
        self.horizontalLayout.addWidget(self.search_bar)
        self.add_button = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.add_button.setFont(font)
        self.add_button.setObjectName("add_button")
        self.horizontalLayout.addWidget(self.add_button)
        self.left_layout.addLayout(self.horizontalLayout)
        self.in_table = QtWidgets.QTableWidget(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.in_table.setFont(font)
        self.in_table.setObjectName("in_table")
        self.in_table.setColumnCount(0)
        self.in_table.setRowCount(0)
        self.left_layout.addWidget(self.in_table)
        self.horizontalLayout_2.addLayout(self.left_layout)
        self.right_layout = QtWidgets.QVBoxLayout()
        self.right_layout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.right_layout.setObjectName("right_layout")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.right_layout.addWidget(self.label_8)
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.formLayout.setContentsMargins(-1, -1, 9, -1)
        self.formLayout.setVerticalSpacing(16)
        self.formLayout.setObjectName("formLayout")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.patient_age = QtWidgets.QSpinBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.patient_age.sizePolicy().hasHeightForWidth())
        self.patient_age.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.patient_age.setFont(font)
        self.patient_age.setMaximum(200)
        self.patient_age.setObjectName("patient_age")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.patient_age)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.patient_sex = QtWidgets.QComboBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.patient_sex.sizePolicy().hasHeightForWidth())
        self.patient_sex.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.patient_sex.setFont(font)
        self.patient_sex.setEditable(False)
        self.patient_sex.setObjectName("patient_sex")
        self.patient_sex.addItem("")
        self.patient_sex.addItem("")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.patient_sex)
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.days_of_meds = QtWidgets.QSpinBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.days_of_meds.sizePolicy().hasHeightForWidth())
        self.days_of_meds.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.days_of_meds.setFont(font)
        self.days_of_meds.setMaximum(999)
        self.days_of_meds.setObjectName("days_of_meds")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.days_of_meds)
        spacerItem = QtWidgets.QSpacerItem(0, 13, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.formLayout.setItem(4, QtWidgets.QFormLayout.FieldRole, spacerItem)
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.label_6)
        self.doctor_name = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.doctor_name.sizePolicy().hasHeightForWidth())
        self.doctor_name.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.doctor_name.setFont(font)
        self.doctor_name.setMaxLength(100)
        self.doctor_name.setClearButtonEnabled(False)
        self.doctor_name.setObjectName("doctor_name")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.doctor_name)
        self.patient_name = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.patient_name.sizePolicy().hasHeightForWidth())
        self.patient_name.setSizePolicy(sizePolicy)
        self.patient_name.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.patient_name.setFont(font)
        self.patient_name.setStatusTip("")
        self.patient_name.setAutoFillBackground(False)
        self.patient_name.setMaxLength(100)
        self.patient_name.setObjectName("patient_name")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.patient_name)
        self.right_layout.addLayout(self.formLayout)
        self.btn_export = QtWidgets.QPushButton(self.centralwidget)
        self.btn_export.setMaximumSize(QtCore.QSize(177, 16777215))
        self.btn_export.setObjectName("btn_export")
        self.right_layout.addWidget(self.btn_export)
        self.right_layout.setStretch(1, 1)
        self.horizontalLayout_2.addLayout(self.right_layout)
        self.horizontalLayout_2.setStretch(0, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtWidgets.QApplication.translate("MainWindow", "MainWindow", None, -1))
        self.label_7.setText(QtWidgets.QApplication.translate("MainWindow", "Current List", None, -1))
        self.label.setText(QtWidgets.QApplication.translate("MainWindow", "Search", None, -1))
        self.add_button.setText(QtWidgets.QApplication.translate("MainWindow", "Add", None, -1))
        self.label_8.setText(QtWidgets.QApplication.translate("MainWindow", "Export", None, -1))
        self.label_2.setText(QtWidgets.QApplication.translate("MainWindow", "Patient", None, -1))
        self.label_3.setText(QtWidgets.QApplication.translate("MainWindow", "Age", None, -1))
        self.label_4.setText(QtWidgets.QApplication.translate("MainWindow", "Sex", None, -1))
        self.patient_sex.setItemText(0, QtWidgets.QApplication.translate("MainWindow", "男", None, -1))
        self.patient_sex.setItemText(1, QtWidgets.QApplication.translate("MainWindow", "女", None, -1))
        self.label_5.setText(QtWidgets.QApplication.translate("MainWindow", "Days", None, -1))
        self.label_6.setText(QtWidgets.QApplication.translate("MainWindow", "Doctor", None, -1))
        self.btn_export.setText(QtWidgets.QApplication.translate("MainWindow", "Export", None, -1))
