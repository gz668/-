# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainWindow.ui'
##
## Created by: Qt User Interface Compiler version 5.14.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QDate, QDateTime, QMetaObject,
    QObject, QPoint, QRect, QSize, QTime, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter,
    QPixmap, QRadialGradient)
from PySide2.QtWidgets import *

from pyqtgraph import PlotWidget


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1029, 594)
        MainWindow.setMinimumSize(QSize(1029, 594))
        MainWindow.setMaximumSize(QSize(1029, 594))
        MainWindow.setSizeIncrement(QSize(0, 0))
        MainWindow.setAnimated(True)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(180, 10, 611, 391))
        self.groupBox.setAlignment(Qt.AlignCenter)
        self.tabWidget = QTabWidget(self.groupBox)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setGeometry(QRect(10, 20, 601, 361))
        self.tabWidget.setMovable(True)
        self.tab_1 = QWidget()
        self.tab_1.setObjectName(u"tab_1")
        self.plotView_1 = PlotWidget(self.tab_1)
        self.plotView_1.setObjectName(u"plotView_1")
        self.plotView_1.setGeometry(QRect(10, 10, 571, 311))
        self.tabWidget.addTab(self.tab_1, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.plotView_2 = PlotWidget(self.tab_2)
        self.plotView_2.setObjectName(u"plotView_2")
        self.plotView_2.setGeometry(QRect(10, 10, 571, 311))
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.plotView_3 = PlotWidget(self.tab_3)
        self.plotView_3.setObjectName(u"plotView_3")
        self.plotView_3.setGeometry(QRect(10, 10, 571, 311))
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QWidget()
        self.tab_4.setObjectName(u"tab_4")
        self.plotView_4 = PlotWidget(self.tab_4)
        self.plotView_4.setObjectName(u"plotView_4")
        self.plotView_4.setGeometry(QRect(10, 10, 571, 311))
        self.tabWidget.addTab(self.tab_4, "")
        self.tab_5 = QWidget()
        self.tab_5.setObjectName(u"tab_5")
        self.plotView_5 = PlotWidget(self.tab_5)
        self.plotView_5.setObjectName(u"plotView_5")
        self.plotView_5.setGeometry(QRect(10, 10, 571, 311))
        self.tabWidget.addTab(self.tab_5, "")
        self.tab_6 = QWidget()
        self.tab_6.setObjectName(u"tab_6")
        self.plotView_6 = PlotWidget(self.tab_6)
        self.plotView_6.setObjectName(u"plotView_6")
        self.plotView_6.setGeometry(QRect(10, 10, 571, 311))
        self.tabWidget.addTab(self.tab_6, "")
        self.tab_7 = QWidget()
        self.tab_7.setObjectName(u"tab_7")
        self.plotView_7 = PlotWidget(self.tab_7)
        self.plotView_7.setObjectName(u"plotView_7")
        self.plotView_7.setGeometry(QRect(10, 10, 571, 311))
        self.tabWidget.addTab(self.tab_7, "")
        self.tab_8 = QWidget()
        self.tab_8.setObjectName(u"tab_8")
        self.plotView_8 = PlotWidget(self.tab_8)
        self.plotView_8.setObjectName(u"plotView_8")
        self.plotView_8.setGeometry(QRect(10, 10, 571, 311))
        self.tabWidget.addTab(self.tab_8, "")
        self.groupBox_2 = QGroupBox(self.centralwidget)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setGeometry(QRect(10, 409, 781, 141))
        self.groupBox_2.setAlignment(Qt.AlignCenter)
        self.groupBox_2.setFlat(False)
        self.groupBox_2.setCheckable(False)
        self.horizontalLayoutWidget = QWidget(self.groupBox_2)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(10, 20, 761, 111))
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.widget_1 = QWidget(self.horizontalLayoutWidget)
        self.widget_1.setObjectName(u"widget_1")
        self.input_1 = QLineEdit(self.widget_1)
        self.input_1.setObjectName(u"input_1")
        self.input_1.setGeometry(QRect(53, 30, 71, 41))
        self.input_1.setAlignment(Qt.AlignCenter)
        self.Button_send1 = QPushButton(self.widget_1)
        self.Button_send1.setObjectName(u"Button_send1")
        self.Button_send1.setGeometry(QRect(51, 80, 75, 23))
        self.label = QLabel(self.widget_1)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(16, 9, 161, 21))

        self.horizontalLayout.addWidget(self.widget_1)

        self.widget_2 = QWidget(self.horizontalLayoutWidget)
        self.widget_2.setObjectName(u"widget_2")
        self.input_2 = QLineEdit(self.widget_2)
        self.input_2.setObjectName(u"input_2")
        self.input_2.setGeometry(QRect(55, 30, 71, 41))
        self.input_2.setAlignment(Qt.AlignCenter)
        self.Button_send2 = QPushButton(self.widget_2)
        self.Button_send2.setObjectName(u"Button_send2")
        self.Button_send2.setGeometry(QRect(53, 80, 75, 23))
        self.label_7 = QLabel(self.widget_2)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(26, 10, 131, 20))
        self.label_7.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.widget_2)

        self.widget_3 = QWidget(self.horizontalLayoutWidget)
        self.widget_3.setObjectName(u"widget_3")
        self.input_3 = QLineEdit(self.widget_3)
        self.input_3.setObjectName(u"input_3")
        self.input_3.setGeometry(QRect(53, 30, 71, 41))
        self.input_3.setAlignment(Qt.AlignCenter)
        self.Button_send3 = QPushButton(self.widget_3)
        self.Button_send3.setObjectName(u"Button_send3")
        self.Button_send3.setGeometry(QRect(52, 80, 75, 23))
        self.label_3 = QLabel(self.widget_3)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(43, 10, 91, 20))
        self.label_3.setTextFormat(Qt.AutoText)
        self.label_3.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.widget_3)

        self.widget_4 = QWidget(self.horizontalLayoutWidget)
        self.widget_4.setObjectName(u"widget_4")
        self.input_4 = QLineEdit(self.widget_4)
        self.input_4.setObjectName(u"input_4")
        self.input_4.setGeometry(QRect(52, 30, 71, 41))
        self.input_4.setAlignment(Qt.AlignCenter)
        self.Button_send4 = QPushButton(self.widget_4)
        self.Button_send4.setObjectName(u"Button_send4")
        self.Button_send4.setGeometry(QRect(51, 80, 75, 23))
        self.label_6 = QLabel(self.widget_4)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(43, 10, 91, 20))
        self.label_6.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.widget_4)

        self.groupBox_3 = QGroupBox(self.centralwidget)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setGeometry(QRect(8, 10, 171, 391))
        self.gridLayoutWidget = QWidget(self.groupBox_3)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(4, 17, 163, 361))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.gridLayout.setHorizontalSpacing(3)
        self.gridLayout.setVerticalSpacing(10)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.gridLayoutWidget)
        self.label_2.setObjectName(u"label_2")
        font = QFont()
        font.setFamily(u"AcadEref")
        font.setPointSize(12)
        self.label_2.setFont(font)

        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)

        self.Button_quit = QPushButton(self.gridLayoutWidget)
        self.Button_quit.setObjectName(u"Button_quit")
        self.Button_quit.setFont(font)

        self.gridLayout.addWidget(self.Button_quit, 5, 0, 1, 2)

        self.Button_FindPort = QPushButton(self.gridLayoutWidget)
        self.Button_FindPort.setObjectName(u"Button_FindPort")
        self.Button_FindPort.setFont(font)

        self.gridLayout.addWidget(self.Button_FindPort, 3, 0, 1, 2)

        self.verticalSpacer = QSpacerItem(20, 150, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout.addItem(self.verticalSpacer, 4, 0, 1, 2)

        self.Box_get_port = QComboBox(self.gridLayoutWidget)
        self.Box_get_port.setObjectName(u"Box_get_port")
        font1 = QFont()
        font1.setFamily(u"\u5b8b\u4f53")
        font1.setPointSize(11)
        self.Box_get_port.setFont(font1)
        self.Box_get_port.setIconSize(QSize(30, 20))

        self.gridLayout.addWidget(self.Box_get_port, 0, 1, 1, 1)

        self.Button_Rec = QPushButton(self.gridLayoutWidget)
        self.Button_Rec.setObjectName(u"Button_Rec")
        font2 = QFont()
        font2.setPointSize(12)
        self.Button_Rec.setFont(font2)
        self.Button_Rec.setIconSize(QSize(16, 16))

        self.gridLayout.addWidget(self.Button_Rec, 2, 0, 1, 2)

        self.Button_Open = QPushButton(self.gridLayoutWidget)
        self.Button_Open.setObjectName(u"Button_Open")
        self.Button_Open.setFont(font)
        self.Button_Open.setIconSize(QSize(20, 40))

        self.gridLayout.addWidget(self.Button_Open, 1, 0, 1, 2)

        self.groupBox_4 = QGroupBox(self.centralwidget)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.groupBox_4.setGeometry(QRect(800, 10, 221, 541))
        self.gridLayoutWidget_2 = QWidget(self.groupBox_4)
        self.gridLayoutWidget_2.setObjectName(u"gridLayoutWidget_2")
        self.gridLayoutWidget_2.setGeometry(QRect(10, 20, 201, 511))
        self.gridLayout_2 = QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label_value_2 = QLabel(self.gridLayoutWidget_2)
        self.label_value_2.setObjectName(u"label_value_2")

        self.gridLayout_2.addWidget(self.label_value_2, 1, 1, 1, 1)

        self.label_name_3 = QLabel(self.gridLayoutWidget_2)
        self.label_name_3.setObjectName(u"label_name_3")

        self.gridLayout_2.addWidget(self.label_name_3, 2, 0, 1, 1)

        self.label_value_3 = QLabel(self.gridLayoutWidget_2)
        self.label_value_3.setObjectName(u"label_value_3")
        self.label_value_3.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_2.addWidget(self.label_value_3, 2, 1, 1, 1)

        self.label_value_1 = QLabel(self.gridLayoutWidget_2)
        self.label_value_1.setObjectName(u"label_value_1")

        self.gridLayout_2.addWidget(self.label_value_1, 0, 1, 1, 1)

        self.label_value_4 = QLabel(self.gridLayoutWidget_2)
        self.label_value_4.setObjectName(u"label_value_4")

        self.gridLayout_2.addWidget(self.label_value_4, 3, 1, 1, 1)

        self.label_name_5 = QLabel(self.gridLayoutWidget_2)
        self.label_name_5.setObjectName(u"label_name_5")

        self.gridLayout_2.addWidget(self.label_name_5, 4, 0, 1, 1)

        self.label_value_6 = QLabel(self.gridLayoutWidget_2)
        self.label_value_6.setObjectName(u"label_value_6")

        self.gridLayout_2.addWidget(self.label_value_6, 5, 1, 1, 1)

        self.label_name_7 = QLabel(self.gridLayoutWidget_2)
        self.label_name_7.setObjectName(u"label_name_7")

        self.gridLayout_2.addWidget(self.label_name_7, 6, 0, 1, 1)

        self.label_name_1 = QLabel(self.gridLayoutWidget_2)
        self.label_name_1.setObjectName(u"label_name_1")

        self.gridLayout_2.addWidget(self.label_name_1, 0, 0, 1, 1)

        self.label_name_6 = QLabel(self.gridLayoutWidget_2)
        self.label_name_6.setObjectName(u"label_name_6")

        self.gridLayout_2.addWidget(self.label_name_6, 5, 0, 1, 1)

        self.label_name_2 = QLabel(self.gridLayoutWidget_2)
        self.label_name_2.setObjectName(u"label_name_2")

        self.gridLayout_2.addWidget(self.label_name_2, 1, 0, 1, 1)

        self.label_value_7 = QLabel(self.gridLayoutWidget_2)
        self.label_value_7.setObjectName(u"label_value_7")

        self.gridLayout_2.addWidget(self.label_value_7, 6, 1, 1, 1)

        self.label_name_4 = QLabel(self.gridLayoutWidget_2)
        self.label_name_4.setObjectName(u"label_name_4")

        self.gridLayout_2.addWidget(self.label_name_4, 3, 0, 1, 1)

        self.label_value_5 = QLabel(self.gridLayoutWidget_2)
        self.label_value_5.setObjectName(u"label_value_5")

        self.gridLayout_2.addWidget(self.label_value_5, 4, 1, 1, 1)

        self.label_name_8 = QLabel(self.gridLayoutWidget_2)
        self.label_name_8.setObjectName(u"label_name_8")

        self.gridLayout_2.addWidget(self.label_name_8, 7, 0, 1, 1)

        self.label_value_8 = QLabel(self.gridLayoutWidget_2)
        self.label_value_8.setObjectName(u"label_value_8")

        self.gridLayout_2.addWidget(self.label_value_8, 7, 1, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1029, 23))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(7)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"\u6ce2\u5f62\u663e\u793a\u533a\u57df", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_1), QCoreApplication.translate("MainWindow", u"\u6d41\u91cf", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"\u6e29\u5ea6", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QCoreApplication.translate("MainWindow", u"\u52a8\u8109\u538b", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), QCoreApplication.translate("MainWindow", u"\u9759\u8109\u538b", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), QCoreApplication.translate("MainWindow", u"\u65b0\u9c9c\u6db2\u538b\u529b", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_6), QCoreApplication.translate("MainWindow", u"\u5e9f\u6db2\u538b\u529b", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_7), QCoreApplication.translate("MainWindow", u"\u7535\u5bfc", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_8), QCoreApplication.translate("MainWindow", u"PH", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"\u53c2\u6570\u8bbe\u7f6e\u533a\u57df", None))
        self.input_1.setText("")
        self.Button_send1.setText(QCoreApplication.translate("MainWindow", u"\u53d1\u9001", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u65b0\u9c9c\u6db2\u548c\u5e9f\u6db2(\u5355\u4f4d\uff1aml/min)", None))
        self.Button_send2.setText(QCoreApplication.translate("MainWindow", u"\u53d1\u9001", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"\u8d85\u6ee4(\u5355\u4f4d\uff1aml/min)", None))
        self.Button_send3.setText(QCoreApplication.translate("MainWindow", u"\u53d1\u9001", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u809d\u7d20\u6cf5", None))
        self.Button_send4.setText(QCoreApplication.translate("MainWindow", u"\u53d1\u9001", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"\u8840\u6cf5", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"\u4e32\u53e3\u8bbe\u7f6e", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u4e32\u53e3\u53f7", None))
        self.Button_quit.setText(QCoreApplication.translate("MainWindow", u"\u9000\u51fa", None))
        self.Button_FindPort.setText(QCoreApplication.translate("MainWindow", u"\u68c0\u6d4b\u4e32\u53e3", None))
        self.Button_Rec.setText(QCoreApplication.translate("MainWindow", u"\u63a5\u6536", None))
        self.Button_Open.setText(QCoreApplication.translate("MainWindow", u"\u6253\u5f00", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("MainWindow", u"\u6570\u503c\u663e\u793a\u533a\u57df", None))
        self.label_value_2.setText("")
        self.label_name_3.setText(QCoreApplication.translate("MainWindow", u"\u52a8\u8109\u538b\uff1a", None))
        self.label_value_3.setText("")
        self.label_value_1.setText("")
        self.label_value_4.setText("")
        self.label_name_5.setText(QCoreApplication.translate("MainWindow", u"\u65b0\u9c9c\u6db2\u538b\u529b\uff1a", None))
        self.label_value_6.setText("")
        self.label_name_7.setText(QCoreApplication.translate("MainWindow", u"\u7535\u5bfc\uff08ms/cm\uff09\uff1a", None))
        self.label_name_1.setText(QCoreApplication.translate("MainWindow", u"\u6d41\u91cf\uff08ml/min\uff09\uff1a", None))
        self.label_name_6.setText(QCoreApplication.translate("MainWindow", u"\u5e9f\u6db2\u538b\u529b\uff1a", None))
        self.label_name_2.setText(QCoreApplication.translate("MainWindow", u"\u6e29\u5ea6\uff08\u2103\uff09\uff1a", None))
        self.label_value_7.setText("")
        self.label_name_4.setText(QCoreApplication.translate("MainWindow", u"\u9759\u8109\u538b\uff1a", None))
        self.label_value_5.setText("")
        self.label_name_8.setText(QCoreApplication.translate("MainWindow", u"PH\uff1a", None))
        self.label_value_8.setText("")
    # retranslateUi

