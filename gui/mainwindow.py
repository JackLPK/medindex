# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 5.14.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PySide2.QtWidgets import *

from medindex.gui.intableview import InTableView
from medindex.gui.outtableview import OutTableView
from medindex.gui.sidetableview import SideTableView


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(851, 785)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_2 = QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        font = QFont()
        font.setPointSize(10)
        self.label_5.setFont(font)

        self.horizontalLayout.addWidget(self.label_5)

        self.search_bar = QLineEdit(self.centralwidget)
        self.search_bar.setObjectName(u"search_bar")
        self.search_bar.setFont(font)

        self.horizontalLayout.addWidget(self.search_bar)

        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setFont(font)

        self.horizontalLayout.addWidget(self.pushButton)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.in_table_view = InTableView(self.centralwidget)
        self.in_table_view.setObjectName(u"in_table_view")

        self.verticalLayout_2.addWidget(self.in_table_view)


        self.gridLayout_2.addLayout(self.verticalLayout_2, 1, 0, 1, 1)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font)
        self.label_2.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3.addWidget(self.label_2)

        self.patient_name_edit = QLineEdit(self.centralwidget)
        self.patient_name_edit.setObjectName(u"patient_name_edit")
        font1 = QFont()
        font1.setPointSize(12)
        self.patient_name_edit.setFont(font1)

        self.horizontalLayout_3.addWidget(self.patient_name_edit)

        self.btn_patient = QPushButton(self.centralwidget)
        self.btn_patient.setObjectName(u"btn_patient")
        self.btn_patient.setFont(font)

        self.horizontalLayout_3.addWidget(self.btn_patient)


        self.verticalLayout_3.addLayout(self.horizontalLayout_3)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_8 = QLabel(self.centralwidget)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font)
        self.label_8.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_8, 0, 0, 1, 1)

        self.patient_age = QSpinBox(self.centralwidget)
        self.patient_age.setObjectName(u"patient_age")
        self.patient_age.setFont(font)
        self.patient_age.setMaximum(200)

        self.gridLayout.addWidget(self.patient_age, 0, 1, 1, 1)

        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font)
        self.label_4.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_4, 0, 2, 1, 1)

        self.patient_sex = QComboBox(self.centralwidget)
        self.patient_sex.setObjectName(u"patient_sex")
        self.patient_sex.setFont(font)

        self.gridLayout.addWidget(self.patient_sex, 0, 3, 1, 1)

        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font)
        self.label_6.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_6, 1, 0, 1, 1)

        self.shots_of_meds = QSpinBox(self.centralwidget)
        self.shots_of_meds.setObjectName(u"shots_of_meds")
        self.shots_of_meds.setFont(font)
        self.shots_of_meds.setMaximum(500)

        self.gridLayout.addWidget(self.shots_of_meds, 1, 1, 1, 1)

        self.label_9 = QLabel(self.centralwidget)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setFont(font)
        self.label_9.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_9, 2, 0, 1, 2)

        self.organisation = QLineEdit(self.centralwidget)
        self.organisation.setObjectName(u"organisation")
        self.organisation.setFont(font1)

        self.gridLayout.addWidget(self.organisation, 2, 2, 1, 2)

        self.label_10 = QLabel(self.centralwidget)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setFont(font)
        self.label_10.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_10, 3, 0, 1, 2)

        self.doctor = QLineEdit(self.centralwidget)
        self.doctor.setObjectName(u"doctor")
        self.doctor.setFont(font1)

        self.gridLayout.addWidget(self.doctor, 3, 2, 1, 2)


        self.verticalLayout_3.addLayout(self.gridLayout)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_7 = QLabel(self.centralwidget)
        self.label_7.setObjectName(u"label_7")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy)
        self.label_7.setFont(font)

        self.verticalLayout.addWidget(self.label_7)

        self.instruction_for_meds = QTextEdit(self.centralwidget)
        self.instruction_for_meds.setObjectName(u"instruction_for_meds")
        self.instruction_for_meds.setFont(font1)

        self.verticalLayout.addWidget(self.instruction_for_meds)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.pushButton_4 = QPushButton(self.centralwidget)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setFont(font)

        self.horizontalLayout_2.addWidget(self.pushButton_4)

        self.btn_clear = QPushButton(self.centralwidget)
        self.btn_clear.setObjectName(u"btn_clear")
        self.btn_clear.setFont(font)

        self.horizontalLayout_2.addWidget(self.btn_clear)

        self.btn_export = QPushButton(self.centralwidget)
        self.btn_export.setObjectName(u"btn_export")
        self.btn_export.setFont(font)

        self.horizontalLayout_2.addWidget(self.btn_export)


        self.verticalLayout.addLayout(self.horizontalLayout_2)


        self.verticalLayout_3.addLayout(self.verticalLayout)


        self.gridLayout_2.addLayout(self.verticalLayout_3, 1, 1, 1, 1)

        self.out_table_view = OutTableView(self.centralwidget)
        self.out_table_view.setObjectName(u"out_table_view")

        self.gridLayout_2.addWidget(self.out_table_view, 0, 0, 1, 1)

        self.side_table_view = SideTableView(self.centralwidget)
        self.side_table_view.setObjectName(u"side_table_view")

        self.gridLayout_2.addWidget(self.side_table_view, 0, 1, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 851, 25))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MedIndex", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Search", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"PH", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Patient", None))
        self.btn_patient.setText(QCoreApplication.translate("MainWindow", u"Search", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Age", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Sex", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Shots", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Organisation", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Doctor", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Instructions", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"PH", None))
        self.btn_clear.setText(QCoreApplication.translate("MainWindow", u"Clear", None))
        self.btn_export.setText(QCoreApplication.translate("MainWindow", u"Export", None))
    # retranslateUi

