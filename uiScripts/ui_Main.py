# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainTZRkpV.ui'
##
## Created by: Qt User Interface Compiler version 6.1.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 629)
        MainWindow.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayoutWidget = QWidget(self.centralwidget)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(0, 0, 801, 551))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.tabWidget = QTabWidget(self.gridLayoutWidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.tab.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))
        self.gridLayoutWidget_4 = QWidget(self.tab)
        self.gridLayoutWidget_4.setObjectName(u"gridLayoutWidget_4")
        self.gridLayoutWidget_4.setGeometry(QRect(0, 0, 791, 511))
        self.gridLayout_4 = QGridLayout(self.gridLayoutWidget_4)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.listView = QListView(self.gridLayoutWidget_4)
        self.listView.setObjectName(u"listView")

        self.gridLayout_4.addWidget(self.listView, 0, 0, 1, 1)

        self.pushButton_11 = QPushButton(self.gridLayoutWidget_4)
        self.pushButton_11.setObjectName(u"pushButton_11")

        self.gridLayout_4.addWidget(self.pushButton_11, 2, 1, 1, 1)

        self.pushButton_10 = QPushButton(self.gridLayoutWidget_4)
        self.pushButton_10.setObjectName(u"pushButton_10")

        self.gridLayout_4.addWidget(self.pushButton_10, 2, 0, 1, 1)

        self.pushButton_8 = QPushButton(self.gridLayoutWidget_4)
        self.pushButton_8.setObjectName(u"pushButton_8")

        self.gridLayout_4.addWidget(self.pushButton_8, 0, 1, 1, 1)

        self.pushButton_9 = QPushButton(self.gridLayoutWidget_4)
        self.pushButton_9.setObjectName(u"pushButton_9")

        self.gridLayout_4.addWidget(self.pushButton_9, 1, 0, 1, 1)

        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.tab_2.setEnabled(True)
        self.tabWidget_2 = QTabWidget(self.tab_2)
        self.tabWidget_2.setObjectName(u"tabWidget_2")
        self.tabWidget_2.setGeometry(QRect(0, 0, 791, 521))
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.gridLayoutWidget_2 = QWidget(self.tab_3)
        self.gridLayoutWidget_2.setObjectName(u"gridLayoutWidget_2")
        self.gridLayoutWidget_2.setGeometry(QRect(10, 10, 761, 481))
        self.gridLayout_2 = QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label_5 = QLabel(self.gridLayoutWidget_2)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout_2.addWidget(self.label_5, 6, 1, 1, 1)

        self.label_2 = QLabel(self.gridLayoutWidget_2)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout_2.addWidget(self.label_2, 1, 1, 1, 1)

        self.lineEdit_3 = QLineEdit(self.gridLayoutWidget_2)
        self.lineEdit_3.setObjectName(u"lineEdit_3")

        self.gridLayout_2.addWidget(self.lineEdit_3, 2, 2, 1, 1)

        self.pushButton_4 = QPushButton(self.gridLayoutWidget_2)
        self.pushButton_4.setObjectName(u"pushButton_4")

        self.gridLayout_2.addWidget(self.pushButton_4, 3, 4, 1, 1)

        self.label_3 = QLabel(self.gridLayoutWidget_2)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout_2.addWidget(self.label_3, 2, 1, 1, 1)

        self.pushButton_2 = QPushButton(self.gridLayoutWidget_2)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.gridLayout_2.addWidget(self.pushButton_2, 1, 4, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.pushButton_7 = QPushButton(self.gridLayoutWidget_2)
        self.pushButton_7.setObjectName(u"pushButton_7")

        self.horizontalLayout.addWidget(self.pushButton_7)


        self.gridLayout_2.addLayout(self.horizontalLayout, 7, 4, 1, 1)

        self.lineEdit = QLineEdit(self.gridLayoutWidget_2)
        self.lineEdit.setObjectName(u"lineEdit")

        self.gridLayout_2.addWidget(self.lineEdit, 6, 2, 1, 1)

        self.label_4 = QLabel(self.gridLayoutWidget_2)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout_2.addWidget(self.label_4, 3, 1, 1, 1)

        self.lineEdit_4 = QLineEdit(self.gridLayoutWidget_2)
        self.lineEdit_4.setObjectName(u"lineEdit_4")

        self.gridLayout_2.addWidget(self.lineEdit_4, 1, 2, 1, 1)

        self.pushButton = QPushButton(self.gridLayoutWidget_2)
        self.pushButton.setObjectName(u"pushButton")

        self.gridLayout_2.addWidget(self.pushButton, 0, 4, 1, 1)

        self.pushButton_3 = QPushButton(self.gridLayoutWidget_2)
        self.pushButton_3.setObjectName(u"pushButton_3")

        self.gridLayout_2.addWidget(self.pushButton_3, 2, 4, 1, 1)

        self.label = QLabel(self.gridLayoutWidget_2)
        self.label.setObjectName(u"label")

        self.gridLayout_2.addWidget(self.label, 0, 1, 1, 1)

        self.lineEdit_2 = QLineEdit(self.gridLayoutWidget_2)
        self.lineEdit_2.setObjectName(u"lineEdit_2")

        self.gridLayout_2.addWidget(self.lineEdit_2, 3, 2, 1, 1)

        self.lineEdit_5 = QLineEdit(self.gridLayoutWidget_2)
        self.lineEdit_5.setObjectName(u"lineEdit_5")

        self.gridLayout_2.addWidget(self.lineEdit_5, 0, 2, 1, 1)

        self.pushButton_5 = QPushButton(self.gridLayoutWidget_2)
        self.pushButton_5.setObjectName(u"pushButton_5")

        self.gridLayout_2.addWidget(self.pushButton_5, 6, 4, 1, 1)

        self.pushButton_6 = QPushButton(self.gridLayoutWidget_2)
        self.pushButton_6.setObjectName(u"pushButton_6")

        self.gridLayout_2.addWidget(self.pushButton_6, 7, 3, 1, 1)

        self.tabWidget_2.addTab(self.tab_3, "")
        self.tab_4 = QWidget()
        self.tab_4.setObjectName(u"tab_4")
        self.gridLayoutWidget_3 = QWidget(self.tab_4)
        self.gridLayoutWidget_3.setObjectName(u"gridLayoutWidget_3")
        self.gridLayoutWidget_3.setGeometry(QRect(0, 0, 781, 481))
        self.gridLayout_3 = QGridLayout(self.gridLayoutWidget_3)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label_6 = QLabel(self.gridLayoutWidget_3)
        self.label_6.setObjectName(u"label_6")
        font = QFont()
        font.setPointSize(14)
        self.label_6.setFont(font)
        self.label_6.setLayoutDirection(Qt.LeftToRight)
        self.label_6.setFrameShape(QFrame.NoFrame)
        self.label_6.setAlignment(Qt.AlignHCenter|Qt.AlignTop)

        self.gridLayout_3.addWidget(self.label_6, 0, 0, 1, 1)

        self.label_7 = QLabel(self.gridLayoutWidget_3)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.label_7, 1, 0, 1, 1)

        self.tabWidget_2.addTab(self.tab_4, "")
        self.tabWidget.addTab(self.tab_2, "")

        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 1)

        self.label_8 = QLabel(self.centralwidget)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(10, 560, 781, 16))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)
        self.tabWidget_2.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.pushButton_11.setText(QCoreApplication.translate("MainWindow", u"Delete Selected Virtual Machine", None))
        self.pushButton_10.setText(QCoreApplication.translate("MainWindow", u"Edit Selected Virtual Machine", None))
        self.pushButton_8.setText(QCoreApplication.translate("MainWindow", u"New Virtual Machine", None))
        self.pushButton_9.setText(QCoreApplication.translate("MainWindow", u"Start Selected Virtual Machine", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"Main", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"qemu-system-mips64el path", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"qemu-system-i386 path", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"Browse", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"qemu-system-x86_64 path", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Browse", None))
        self.pushButton_7.setText(QCoreApplication.translate("MainWindow", u"Reset", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"qemu-system-ppc path", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Browse", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"Browse", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"qemu-img Path", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"Browse", None))
        self.pushButton_6.setText(QCoreApplication.translate("MainWindow", u"Apply", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_3), QCoreApplication.translate("MainWindow", u"QEMU", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"EmuGUI", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Built on Python and PyQt technology", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_4), QCoreApplication.translate("MainWindow", u"About", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"Settings", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"EmuGUI v0.0.1", None))
    # retranslateUi
