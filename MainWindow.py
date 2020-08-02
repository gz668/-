# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainWindow_1.ui'
##
## Created by: Qt User Interface Compiler version 5.15.0
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
        MainWindow.resize(1353, 736)
        MainWindow.setMinimumSize(QSize(1353, 736))
        MainWindow.setMaximumSize(QSize(1353, 736))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.wave_form_group_box = QGroupBox(self.centralwidget)
        self.wave_form_group_box.setObjectName(u"wave_form_group_box")
        self.wave_form_group_box.setGeometry(QRect(261, 13, 841, 491))
        font = QFont()
        font.setFamily(u"\u9ed1\u4f53")
        font.setPointSize(12)
        self.wave_form_group_box.setFont(font)
        self.wave_form_group_box.setAlignment(Qt.AlignCenter)
        self.tabWidget = QTabWidget(self.wave_form_group_box)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setGeometry(QRect(10, 20, 821, 461))
        self.tabWidget.setFont(font)
        self.tabWidget.setMovable(True)
        self.dialysis_widget = QWidget()
        self.dialysis_widget.setObjectName(u"dialysis_widget")
        self.dialysis_pressure_plot_view = PlotWidget(self.dialysis_widget)
        self.dialysis_pressure_plot_view.setObjectName(u"dialysis_pressure_plot_view")
        self.dialysis_pressure_plot_view.setGeometry(QRect(10, 10, 801, 411))
        self.tabWidget.addTab(self.dialysis_widget, "")
        self.dialysis_flow_widget = QWidget()
        self.dialysis_flow_widget.setObjectName(u"dialysis_flow_widget")
        self.dialysis_flow_plot_view = PlotWidget(self.dialysis_flow_widget)
        self.dialysis_flow_plot_view.setObjectName(u"dialysis_flow_plot_view")
        self.dialysis_flow_plot_view.setGeometry(QRect(10, 10, 801, 411))
        self.tabWidget.addTab(self.dialysis_flow_widget, "")
        self.pluse_widget = QWidget()
        self.pluse_widget.setObjectName(u"pluse_widget")
        self.pluse_plot_view = PlotWidget(self.pluse_widget)
        self.pluse_plot_view.setObjectName(u"pluse_plot_view")
        self.pluse_plot_view.setGeometry(QRect(10, 10, 801, 411))
        self.tabWidget.addTab(self.pluse_widget, "")
        self.weight_view = QWidget()
        self.weight_view.setObjectName(u"weight_view")
        self.weight_plot_view = PlotWidget(self.weight_view)
        self.weight_plot_view.setObjectName(u"weight_plot_view")
        self.weight_plot_view.setGeometry(QRect(10, 10, 801, 411))
        self.tabWidget.addTab(self.weight_view, "")
        self.tmp_widget = QWidget()
        self.tmp_widget.setObjectName(u"tmp_widget")
        self.tmp_plot_view = PlotWidget(self.tmp_widget)
        self.tmp_plot_view.setObjectName(u"tmp_plot_view")
        self.tmp_plot_view.setGeometry(QRect(10, 10, 801, 411))
        self.tabWidget.addTab(self.tmp_widget, "")
        self.value_group_box = QGroupBox(self.centralwidget)
        self.value_group_box.setObjectName(u"value_group_box")
        self.value_group_box.setGeometry(QRect(1113, 14, 231, 681))
        self.value_group_box.setFont(font)
        self.gridLayoutWidget_2 = QWidget(self.value_group_box)
        self.gridLayoutWidget_2.setObjectName(u"gridLayoutWidget_2")
        self.gridLayoutWidget_2.setGeometry(QRect(10, 29, 211, 641))
        self.gridLayout_2 = QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.waste_flow_label = QLabel(self.gridLayoutWidget_2)
        self.waste_flow_label.setObjectName(u"waste_flow_label")
        self.waste_flow_label.setFont(font)
        self.waste_flow_label.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.waste_flow_label, 6, 0, 1, 1)

        self.fresh_flow_label = QLabel(self.gridLayoutWidget_2)
        self.fresh_flow_label.setObjectName(u"fresh_flow_label")
        self.fresh_flow_label.setFont(font)

        self.gridLayout_2.addWidget(self.fresh_flow_label, 4, 0, 1, 1)

        self.waste_flow_value = QLabel(self.gridLayoutWidget_2)
        self.waste_flow_value.setObjectName(u"waste_flow_value")
        self.waste_flow_value.setFont(font)
        self.waste_flow_value.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(30, 71, 255);")
        self.waste_flow_value.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.waste_flow_value, 6, 1, 1, 1)

        self.fresh_pressure_value = QLabel(self.gridLayoutWidget_2)
        self.fresh_pressure_value.setObjectName(u"fresh_pressure_value")
        self.fresh_pressure_value.setFont(font)
        self.fresh_pressure_value.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.fresh_pressure_value.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.fresh_pressure_value, 1, 1, 1, 1)

        self.artery_pressure_value = QLabel(self.gridLayoutWidget_2)
        self.artery_pressure_value.setObjectName(u"artery_pressure_value")
        self.artery_pressure_value.setFont(font)
        self.artery_pressure_value.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.artery_pressure_value.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.artery_pressure_value, 9, 1, 1, 1)

        self.fresh_pressure_label = QLabel(self.gridLayoutWidget_2)
        self.fresh_pressure_label.setObjectName(u"fresh_pressure_label")
        self.fresh_pressure_label.setFont(font)
        self.fresh_pressure_label.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.fresh_pressure_label, 1, 0, 1, 1)

        self.process_temperature_label = QLabel(self.gridLayoutWidget_2)
        self.process_temperature_label.setObjectName(u"process_temperature_label")
        self.process_temperature_label.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.process_temperature_label, 16, 0, 1, 1)

        self.artery_pressure_label = QLabel(self.gridLayoutWidget_2)
        self.artery_pressure_label.setObjectName(u"artery_pressure_label")
        self.artery_pressure_label.setFont(font)
        self.artery_pressure_label.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.artery_pressure_label, 9, 0, 1, 1)

        self.waste_pressure_vlue = QLabel(self.gridLayoutWidget_2)
        self.waste_pressure_vlue.setObjectName(u"waste_pressure_vlue")
        self.waste_pressure_vlue.setFont(font)
        self.waste_pressure_vlue.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(30, 71, 255);")
        self.waste_pressure_vlue.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.waste_pressure_vlue, 3, 1, 1, 1)

        self.vein_pressure_value = QLabel(self.gridLayoutWidget_2)
        self.vein_pressure_value.setObjectName(u"vein_pressure_value")
        self.vein_pressure_value.setFont(font)
        self.vein_pressure_value.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(30, 71, 255);")
        self.vein_pressure_value.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.vein_pressure_value, 10, 1, 1, 1)

        self.fresh_flow_value = QLabel(self.gridLayoutWidget_2)
        self.fresh_flow_value.setObjectName(u"fresh_flow_value")
        self.fresh_flow_value.setFont(font)
        self.fresh_flow_value.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.fresh_flow_value.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.fresh_flow_value, 4, 1, 1, 1)

        self.vein_pressure_label = QLabel(self.gridLayoutWidget_2)
        self.vein_pressure_label.setObjectName(u"vein_pressure_label")
        self.vein_pressure_label.setFont(font)
        self.vein_pressure_label.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.vein_pressure_label, 10, 0, 1, 1)

        self.waste_pressure_label = QLabel(self.gridLayoutWidget_2)
        self.waste_pressure_label.setObjectName(u"waste_pressure_label")
        self.waste_pressure_label.setFont(font)
        self.waste_pressure_label.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.waste_pressure_label, 3, 0, 1, 1)

        self.initial_temperature_label = QLabel(self.gridLayoutWidget_2)
        self.initial_temperature_label.setObjectName(u"initial_temperature_label")
        self.initial_temperature_label.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.initial_temperature_label, 15, 0, 1, 1)

        self.ultrafiltration_show_label = QLabel(self.gridLayoutWidget_2)
        self.ultrafiltration_show_label.setObjectName(u"ultrafiltration_show_label")
        self.ultrafiltration_show_label.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.ultrafiltration_show_label, 17, 0, 1, 1)

        self.initial_temperature_value = QLabel(self.gridLayoutWidget_2)
        self.initial_temperature_value.setObjectName(u"initial_temperature_value")
        self.initial_temperature_value.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(30, 71, 255);")
        self.initial_temperature_value.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.initial_temperature_value, 15, 1, 1, 1)

        self.process_temperature_value = QLabel(self.gridLayoutWidget_2)
        self.process_temperature_value.setObjectName(u"process_temperature_value")
        self.process_temperature_value.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.process_temperature_value.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.process_temperature_value, 16, 1, 1, 1)

        self.ultrafiltration_show_value = QLabel(self.gridLayoutWidget_2)
        self.ultrafiltration_show_value.setObjectName(u"ultrafiltration_show_value")
        self.ultrafiltration_show_value.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(30, 71, 255);")
        self.ultrafiltration_show_value.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.ultrafiltration_show_value, 17, 1, 1, 1)

        self.blood_flow_label = QLabel(self.gridLayoutWidget_2)
        self.blood_flow_label.setObjectName(u"blood_flow_label")
        self.blood_flow_label.setFont(font)
        self.blood_flow_label.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.blood_flow_label, 7, 0, 1, 1)

        self.blood_flow_value = QLabel(self.gridLayoutWidget_2)
        self.blood_flow_value.setObjectName(u"blood_flow_value")
        self.blood_flow_value.setFont(font)
        self.blood_flow_value.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.blood_flow_value.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.blood_flow_value, 7, 1, 1, 1)

        self.setting_group_box = QGroupBox(self.centralwidget)
        self.setting_group_box.setObjectName(u"setting_group_box")
        self.setting_group_box.setGeometry(QRect(10, 510, 1091, 181))
        font1 = QFont()
        font1.setFamily(u"\u9ed1\u4f53")
        font1.setPointSize(12)
        font1.setBold(False)
        font1.setWeight(50)
        self.setting_group_box.setFont(font1)
        self.setting_group_box.setAlignment(Qt.AlignCenter)
        self.setting_group_box.setFlat(False)
        self.setting_group_box.setCheckable(False)
        self.horizontalLayout = QHBoxLayout(self.setting_group_box)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.gridLayout_6 = QGridLayout()
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.fresh_waste_forward_button = QPushButton(self.setting_group_box)
        self.fresh_waste_forward_button.setObjectName(u"fresh_waste_forward_button")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fresh_waste_forward_button.sizePolicy().hasHeightForWidth())
        self.fresh_waste_forward_button.setSizePolicy(sizePolicy)
        self.fresh_waste_forward_button.setMinimumSize(QSize(50, 30))

        self.gridLayout_6.addWidget(self.fresh_waste_forward_button, 3, 0, 1, 1)

        self.fresh_waste_edit = QLineEdit(self.setting_group_box)
        self.fresh_waste_edit.setObjectName(u"fresh_waste_edit")
        self.fresh_waste_edit.setAlignment(Qt.AlignCenter)

        self.gridLayout_6.addWidget(self.fresh_waste_edit, 2, 0, 1, 2)

        self.fresh_waste_label = QLabel(self.setting_group_box)
        self.fresh_waste_label.setObjectName(u"fresh_waste_label")
        self.fresh_waste_label.setFont(font1)
        self.fresh_waste_label.setAlignment(Qt.AlignCenter)

        self.gridLayout_6.addWidget(self.fresh_waste_label, 1, 0, 1, 2)

        self.fresh_waste_reverse_button = QPushButton(self.setting_group_box)
        self.fresh_waste_reverse_button.setObjectName(u"fresh_waste_reverse_button")
        sizePolicy.setHeightForWidth(self.fresh_waste_reverse_button.sizePolicy().hasHeightForWidth())
        self.fresh_waste_reverse_button.setSizePolicy(sizePolicy)
        self.fresh_waste_reverse_button.setMinimumSize(QSize(50, 30))

        self.gridLayout_6.addWidget(self.fresh_waste_reverse_button, 3, 1, 1, 1)

        self.fresh_waste_stop_button = QPushButton(self.setting_group_box)
        self.fresh_waste_stop_button.setObjectName(u"fresh_waste_stop_button")
        sizePolicy.setHeightForWidth(self.fresh_waste_stop_button.sizePolicy().hasHeightForWidth())
        self.fresh_waste_stop_button.setSizePolicy(sizePolicy)
        self.fresh_waste_stop_button.setMinimumSize(QSize(50, 30))

        self.gridLayout_6.addWidget(self.fresh_waste_stop_button, 4, 0, 1, 2)


        self.horizontalLayout.addLayout(self.gridLayout_6)

        self.gridLayout_7 = QGridLayout()
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.fresh_forward_button = QPushButton(self.setting_group_box)
        self.fresh_forward_button.setObjectName(u"fresh_forward_button")
        sizePolicy.setHeightForWidth(self.fresh_forward_button.sizePolicy().hasHeightForWidth())
        self.fresh_forward_button.setSizePolicy(sizePolicy)
        self.fresh_forward_button.setMinimumSize(QSize(50, 30))

        self.gridLayout_7.addWidget(self.fresh_forward_button, 3, 0, 1, 1)

        self.fresh_edit = QLineEdit(self.setting_group_box)
        self.fresh_edit.setObjectName(u"fresh_edit")
        self.fresh_edit.setAlignment(Qt.AlignCenter)

        self.gridLayout_7.addWidget(self.fresh_edit, 2, 0, 1, 2)

        self.fresh_label = QLabel(self.setting_group_box)
        self.fresh_label.setObjectName(u"fresh_label")
        self.fresh_label.setFont(font1)
        self.fresh_label.setAlignment(Qt.AlignCenter)

        self.gridLayout_7.addWidget(self.fresh_label, 1, 0, 1, 2)

        self.fresh_reverse_button = QPushButton(self.setting_group_box)
        self.fresh_reverse_button.setObjectName(u"fresh_reverse_button")
        sizePolicy.setHeightForWidth(self.fresh_reverse_button.sizePolicy().hasHeightForWidth())
        self.fresh_reverse_button.setSizePolicy(sizePolicy)
        self.fresh_reverse_button.setMinimumSize(QSize(50, 30))

        self.gridLayout_7.addWidget(self.fresh_reverse_button, 3, 1, 1, 1)

        self.fresh_stop_button = QPushButton(self.setting_group_box)
        self.fresh_stop_button.setObjectName(u"fresh_stop_button")
        sizePolicy.setHeightForWidth(self.fresh_stop_button.sizePolicy().hasHeightForWidth())
        self.fresh_stop_button.setSizePolicy(sizePolicy)
        self.fresh_stop_button.setMinimumSize(QSize(50, 30))

        self.gridLayout_7.addWidget(self.fresh_stop_button, 4, 0, 1, 2)


        self.horizontalLayout.addLayout(self.gridLayout_7)

        self.gridLayout_8 = QGridLayout()
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.waste_forward_button = QPushButton(self.setting_group_box)
        self.waste_forward_button.setObjectName(u"waste_forward_button")
        sizePolicy.setHeightForWidth(self.waste_forward_button.sizePolicy().hasHeightForWidth())
        self.waste_forward_button.setSizePolicy(sizePolicy)
        self.waste_forward_button.setMinimumSize(QSize(50, 30))

        self.gridLayout_8.addWidget(self.waste_forward_button, 3, 0, 1, 1)

        self.waste_edit = QLineEdit(self.setting_group_box)
        self.waste_edit.setObjectName(u"waste_edit")
        self.waste_edit.setAlignment(Qt.AlignCenter)

        self.gridLayout_8.addWidget(self.waste_edit, 2, 0, 1, 2)

        self.waste_label = QLabel(self.setting_group_box)
        self.waste_label.setObjectName(u"waste_label")
        self.waste_label.setFont(font1)
        self.waste_label.setAlignment(Qt.AlignCenter)

        self.gridLayout_8.addWidget(self.waste_label, 1, 0, 1, 2)

        self.waste_reverse_button = QPushButton(self.setting_group_box)
        self.waste_reverse_button.setObjectName(u"waste_reverse_button")
        sizePolicy.setHeightForWidth(self.waste_reverse_button.sizePolicy().hasHeightForWidth())
        self.waste_reverse_button.setSizePolicy(sizePolicy)
        self.waste_reverse_button.setMinimumSize(QSize(50, 30))

        self.gridLayout_8.addWidget(self.waste_reverse_button, 3, 1, 1, 1)

        self.waste_stop_button = QPushButton(self.setting_group_box)
        self.waste_stop_button.setObjectName(u"waste_stop_button")
        sizePolicy.setHeightForWidth(self.waste_stop_button.sizePolicy().hasHeightForWidth())
        self.waste_stop_button.setSizePolicy(sizePolicy)
        self.waste_stop_button.setMinimumSize(QSize(50, 30))

        self.gridLayout_8.addWidget(self.waste_stop_button, 4, 0, 1, 2)


        self.horizontalLayout.addLayout(self.gridLayout_8)

        self.gridLayout_9 = QGridLayout()
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.blood_forward_button = QPushButton(self.setting_group_box)
        self.blood_forward_button.setObjectName(u"blood_forward_button")
        sizePolicy.setHeightForWidth(self.blood_forward_button.sizePolicy().hasHeightForWidth())
        self.blood_forward_button.setSizePolicy(sizePolicy)
        self.blood_forward_button.setMinimumSize(QSize(50, 30))

        self.gridLayout_9.addWidget(self.blood_forward_button, 3, 0, 1, 1)

        self.blood_edit = QLineEdit(self.setting_group_box)
        self.blood_edit.setObjectName(u"blood_edit")
        self.blood_edit.setAlignment(Qt.AlignCenter)

        self.gridLayout_9.addWidget(self.blood_edit, 2, 0, 1, 2)

        self.blood_label = QLabel(self.setting_group_box)
        self.blood_label.setObjectName(u"blood_label")
        self.blood_label.setFont(font1)
        self.blood_label.setAlignment(Qt.AlignCenter)

        self.gridLayout_9.addWidget(self.blood_label, 1, 0, 1, 2)

        self.blood_reverse_button = QPushButton(self.setting_group_box)
        self.blood_reverse_button.setObjectName(u"blood_reverse_button")
        sizePolicy.setHeightForWidth(self.blood_reverse_button.sizePolicy().hasHeightForWidth())
        self.blood_reverse_button.setSizePolicy(sizePolicy)
        self.blood_reverse_button.setMinimumSize(QSize(50, 30))

        self.gridLayout_9.addWidget(self.blood_reverse_button, 3, 1, 1, 1)

        self.blood_stop_button = QPushButton(self.setting_group_box)
        self.blood_stop_button.setObjectName(u"blood_stop_button")
        sizePolicy.setHeightForWidth(self.blood_stop_button.sizePolicy().hasHeightForWidth())
        self.blood_stop_button.setSizePolicy(sizePolicy)
        self.blood_stop_button.setMinimumSize(QSize(50, 30))

        self.gridLayout_9.addWidget(self.blood_stop_button, 4, 0, 1, 2)


        self.horizontalLayout.addLayout(self.gridLayout_9)

        self.gridLayout_5 = QGridLayout()
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.ultrafiltration_label = QLabel(self.setting_group_box)
        self.ultrafiltration_label.setObjectName(u"ultrafiltration_label")
        self.ultrafiltration_label.setAlignment(Qt.AlignCenter)

        self.gridLayout_5.addWidget(self.ultrafiltration_label, 0, 0, 1, 2)

        self.ultrafiltration_reverse_button = QPushButton(self.setting_group_box)
        self.ultrafiltration_reverse_button.setObjectName(u"ultrafiltration_reverse_button")
        sizePolicy.setHeightForWidth(self.ultrafiltration_reverse_button.sizePolicy().hasHeightForWidth())
        self.ultrafiltration_reverse_button.setSizePolicy(sizePolicy)
        self.ultrafiltration_reverse_button.setMinimumSize(QSize(50, 30))

        self.gridLayout_5.addWidget(self.ultrafiltration_reverse_button, 2, 1, 1, 1)

        self.ultrafiltration_forward_button = QPushButton(self.setting_group_box)
        self.ultrafiltration_forward_button.setObjectName(u"ultrafiltration_forward_button")
        sizePolicy.setHeightForWidth(self.ultrafiltration_forward_button.sizePolicy().hasHeightForWidth())
        self.ultrafiltration_forward_button.setSizePolicy(sizePolicy)
        self.ultrafiltration_forward_button.setMinimumSize(QSize(50, 30))

        self.gridLayout_5.addWidget(self.ultrafiltration_forward_button, 2, 0, 1, 1)

        self.ultrafiltration_edit = QLineEdit(self.setting_group_box)
        self.ultrafiltration_edit.setObjectName(u"ultrafiltration_edit")
        self.ultrafiltration_edit.setAlignment(Qt.AlignCenter)

        self.gridLayout_5.addWidget(self.ultrafiltration_edit, 1, 0, 1, 2)

        self.ultrafiltration_stop_button = QPushButton(self.setting_group_box)
        self.ultrafiltration_stop_button.setObjectName(u"ultrafiltration_stop_button")
        sizePolicy.setHeightForWidth(self.ultrafiltration_stop_button.sizePolicy().hasHeightForWidth())
        self.ultrafiltration_stop_button.setSizePolicy(sizePolicy)
        self.ultrafiltration_stop_button.setMinimumSize(QSize(50, 30))

        self.gridLayout_5.addWidget(self.ultrafiltration_stop_button, 3, 0, 1, 2)


        self.horizontalLayout.addLayout(self.gridLayout_5)

        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.debug_send_button = QPushButton(self.setting_group_box)
        self.debug_send_button.setObjectName(u"debug_send_button")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.debug_send_button.sizePolicy().hasHeightForWidth())
        self.debug_send_button.setSizePolicy(sizePolicy1)
        self.debug_send_button.setMinimumSize(QSize(50, 25))

        self.gridLayout_3.addWidget(self.debug_send_button, 2, 0, 1, 2)

        self.debug_send_label = QLabel(self.setting_group_box)
        self.debug_send_label.setObjectName(u"debug_send_label")
        self.debug_send_label.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.debug_send_label, 0, 0, 1, 2)

        self.debug_send_edit = QLineEdit(self.setting_group_box)
        self.debug_send_edit.setObjectName(u"debug_send_edit")
        self.debug_send_edit.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.debug_send_edit, 1, 0, 1, 2)


        self.horizontalLayout.addLayout(self.gridLayout_3)

        self.serial_group_box = QGroupBox(self.centralwidget)
        self.serial_group_box.setObjectName(u"serial_group_box")
        self.serial_group_box.setGeometry(QRect(10, 12, 241, 491))
        self.serial_group_box.setFont(font)
        self.gridLayoutWidget = QWidget(self.serial_group_box)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(7, 26, 231, 461))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.gridLayout.setHorizontalSpacing(3)
        self.gridLayout.setVerticalSpacing(10)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.all_send_button = QPushButton(self.gridLayoutWidget)
        self.all_send_button.setObjectName(u"all_send_button")
        self.all_send_button.setFont(font)

        self.gridLayout.addWidget(self.all_send_button, 3, 1, 1, 2)

        self.open_serial_button = QPushButton(self.gridLayoutWidget)
        self.open_serial_button.setObjectName(u"open_serial_button")
        self.open_serial_button.setFont(font)
        self.open_serial_button.setIconSize(QSize(20, 40))

        self.gridLayout.addWidget(self.open_serial_button, 1, 2, 1, 1)

        self.find_port_button = QPushButton(self.gridLayoutWidget)
        self.find_port_button.setObjectName(u"find_port_button")
        self.find_port_button.setFont(font)

        self.gridLayout.addWidget(self.find_port_button, 2, 1, 1, 2)

        self.system_status_label = QLabel(self.gridLayoutWidget)
        self.system_status_label.setObjectName(u"system_status_label")
        palette = QPalette()
        brush = QBrush(QColor(128, 128, 128, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush)
        palette.setBrush(QPalette.Active, QPalette.Base, brush)
        palette.setBrush(QPalette.Active, QPalette.Window, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush)
        self.system_status_label.setPalette(palette)
        self.system_status_label.setStyleSheet(u"background-color: gray;")
        self.system_status_label.setProperty("isOn", True)

        self.gridLayout.addWidget(self.system_status_label, 5, 1, 1, 1)

        self.port_combo_box = QComboBox(self.gridLayoutWidget)
        self.port_combo_box.setObjectName(u"port_combo_box")
        font2 = QFont()
        font2.setFamily(u"\u5b8b\u4f53")
        font2.setPointSize(11)
        self.port_combo_box.setFont(font2)
        self.port_combo_box.setIconSize(QSize(30, 20))

        self.gridLayout.addWidget(self.port_combo_box, 0, 2, 1, 1)

        self.port_status_label = QLabel(self.gridLayoutWidget)
        self.port_status_label.setObjectName(u"port_status_label")
        palette1 = QPalette()
        palette1.setBrush(QPalette.Active, QPalette.Button, brush)
        palette1.setBrush(QPalette.Active, QPalette.Base, brush)
        palette1.setBrush(QPalette.Active, QPalette.Window, brush)
        palette1.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette1.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette1.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette1.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette1.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette1.setBrush(QPalette.Disabled, QPalette.Window, brush)
        self.port_status_label.setPalette(palette1)
        self.port_status_label.setStyleSheet(u"background-color: gray;")
        self.port_status_label.setProperty("isOn", True)

        self.gridLayout.addWidget(self.port_status_label, 1, 1, 1, 1)

        self.start_stop_button = QPushButton(self.gridLayoutWidget)
        self.start_stop_button.setObjectName(u"start_stop_button")
        self.start_stop_button.setFont(font)

        self.gridLayout.addWidget(self.start_stop_button, 5, 2, 1, 1)

        self.port_label = QLabel(self.gridLayoutWidget)
        self.port_label.setObjectName(u"port_label")
        self.port_label.setFont(font)

        self.gridLayout.addWidget(self.port_label, 0, 1, 1, 1)

        self.receive_button = QPushButton(self.gridLayoutWidget)
        self.receive_button.setObjectName(u"receive_button")
        self.receive_button.setFont(font)
        self.receive_button.setIconSize(QSize(16, 16))

        self.gridLayout.addWidget(self.receive_button, 4, 1, 1, 2)

        self.quit_button = QPushButton(self.gridLayoutWidget)
        self.quit_button.setObjectName(u"quit_button")
        self.quit_button.setFont(font)

        self.gridLayout.addWidget(self.quit_button, 14, 1, 2, 2)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 13, 1, 1, 2)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1353, 26))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.wave_form_group_box.setTitle(QCoreApplication.translate("MainWindow", u"\u6ce2\u5f62\u663e\u793a\u533a\u57df", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.dialysis_widget), QCoreApplication.translate("MainWindow", u"\u900f\u6790\u6db2\u538b\u529b", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.dialysis_flow_widget), QCoreApplication.translate("MainWindow", u" \u900f\u6790\u6db2\u548c\u8840\u6db2\u6d41\u91cf", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.pluse_widget), QCoreApplication.translate("MainWindow", u"\u52a8 \u9759\u8109\u538b", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.weight_view), QCoreApplication.translate("MainWindow", u" \u91cd\u91cf", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tmp_widget), QCoreApplication.translate("MainWindow", u"TMP", None))
        self.value_group_box.setTitle(QCoreApplication.translate("MainWindow", u"\u6570\u503c\u663e\u793a\u533a\u57df", None))
        self.waste_flow_label.setText(QCoreApplication.translate("MainWindow", u" \u5e9f\u6db2\u6d41\u91cf", None))
        self.fresh_flow_label.setText(QCoreApplication.translate("MainWindow", u"  \u65b0\u9c9c\u6db2\u6d41\u91cf", None))
        self.waste_flow_value.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.fresh_pressure_value.setText("")
        self.artery_pressure_value.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.fresh_pressure_label.setText(QCoreApplication.translate("MainWindow", u"\u65b0\u9c9c\u6db2\u538b\u529b", None))
        self.process_temperature_label.setText(QCoreApplication.translate("MainWindow", u"  \u8fc7\u7a0b\u6e29\u5ea6", None))
        self.artery_pressure_label.setText(QCoreApplication.translate("MainWindow", u"\u52a8\u8109\u538b", None))
        self.waste_pressure_vlue.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.vein_pressure_value.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.fresh_flow_value.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.vein_pressure_label.setText(QCoreApplication.translate("MainWindow", u"\u9759\u8109\u538b", None))
        self.waste_pressure_label.setText(QCoreApplication.translate("MainWindow", u"\u5e9f\u6db2\u538b\u529b", None))
        self.initial_temperature_label.setText(QCoreApplication.translate("MainWindow", u" \u521d\u59cb\u6e29\u5ea6", None))
        self.ultrafiltration_show_label.setText(QCoreApplication.translate("MainWindow", u"\u8d85\u6ee4\u7387", None))
        self.initial_temperature_value.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.process_temperature_value.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.ultrafiltration_show_value.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.blood_flow_label.setText(QCoreApplication.translate("MainWindow", u"\u8840\u6db2\u6d41\u91cf", None))
        self.blood_flow_value.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.setting_group_box.setTitle(QCoreApplication.translate("MainWindow", u"\u53c2\u6570\u8bbe\u7f6e\u533a\u57df", None))
        self.fresh_waste_forward_button.setText(QCoreApplication.translate("MainWindow", u"\u6b63\u8f6c", None))
        self.fresh_waste_edit.setText("")
        self.fresh_waste_label.setText(QCoreApplication.translate("MainWindow", u" \u53cc\u6cf5", None))
        self.fresh_waste_reverse_button.setText(QCoreApplication.translate("MainWindow", u"\u53cd\u8f6c", None))
        self.fresh_waste_stop_button.setText(QCoreApplication.translate("MainWindow", u"\u505c\u6b62", None))
        self.fresh_forward_button.setText(QCoreApplication.translate("MainWindow", u"\u6b63\u8f6c", None))
        self.fresh_edit.setText("")
        self.fresh_label.setText(QCoreApplication.translate("MainWindow", u"\u65b0\u9c9c\u6db2\u6cf5", None))
        self.fresh_reverse_button.setText(QCoreApplication.translate("MainWindow", u"\u53cd\u8f6c", None))
        self.fresh_stop_button.setText(QCoreApplication.translate("MainWindow", u"\u505c\u6b62", None))
        self.waste_forward_button.setText(QCoreApplication.translate("MainWindow", u"\u6b63\u8f6c", None))
        self.waste_edit.setText("")
        self.waste_label.setText(QCoreApplication.translate("MainWindow", u"  \u5e9f\u6db2\u6cf5", None))
        self.waste_reverse_button.setText(QCoreApplication.translate("MainWindow", u"\u53cd\u8f6c", None))
        self.waste_stop_button.setText(QCoreApplication.translate("MainWindow", u"\u505c\u6b62", None))
        self.blood_forward_button.setText(QCoreApplication.translate("MainWindow", u"\u6b63\u8f6c", None))
        self.blood_edit.setText("")
        self.blood_label.setText(QCoreApplication.translate("MainWindow", u"  \u8840\u6cf5", None))
        self.blood_reverse_button.setText(QCoreApplication.translate("MainWindow", u"\u53cd\u8f6c", None))
        self.blood_stop_button.setText(QCoreApplication.translate("MainWindow", u"\u505c\u6b62", None))
        self.ultrafiltration_label.setText(QCoreApplication.translate("MainWindow", u"\u8d85\u6ee4", None))
        self.ultrafiltration_reverse_button.setText(QCoreApplication.translate("MainWindow", u"\u53cd\u8f6c", None))
        self.ultrafiltration_forward_button.setText(QCoreApplication.translate("MainWindow", u" \u6b63\u8f6c", None))
        self.ultrafiltration_stop_button.setText(QCoreApplication.translate("MainWindow", u"\u505c\u6b62", None))
        self.debug_send_button.setText(QCoreApplication.translate("MainWindow", u"\u53d1\u9001", None))
        self.debug_send_label.setText(QCoreApplication.translate("MainWindow", u"\u8c03\u8bd5", None))
        self.serial_group_box.setTitle(QCoreApplication.translate("MainWindow", u"\u4e32\u53e3\u8bbe\u7f6e", None))
        self.all_send_button.setText(QCoreApplication.translate("MainWindow", u"\u5168\u90e8\u8bbe\u7f6e", None))
        self.open_serial_button.setText(QCoreApplication.translate("MainWindow", u"\u6253\u5f00\u4e32\u53e3", None))
        self.find_port_button.setText(QCoreApplication.translate("MainWindow", u"\u68c0\u6d4b\u4e32\u53e3", None))
        self.system_status_label.setText("")
        self.port_status_label.setText("")
        self.start_stop_button.setText(QCoreApplication.translate("MainWindow", u"\u5f00\u542f", None))
        self.port_label.setText(QCoreApplication.translate("MainWindow", u"\u4e32\u53e3\u9009\u62e9", None))
        self.receive_button.setText(QCoreApplication.translate("MainWindow", u"\u63a5\u6536", None))
        self.quit_button.setText(QCoreApplication.translate("MainWindow", u"\u9000\u51fa", None))
    # retranslateUi

