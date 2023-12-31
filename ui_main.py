# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_main.ui'
##
## Created by: Qt User Interface Compiler version 6.3.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QGridLayout, QGroupBox,
    QHBoxLayout, QHeaderView, QLabel, QMainWindow,
    QMenu, QMenuBar, QPushButton, QSizePolicy,
    QSlider, QSpacerItem, QStatusBar, QTableWidget,
    QTableWidgetItem, QTextEdit, QVBoxLayout, QWidget)
import picture_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1180, 670)
        icon = QIcon()
        icon.addFile(u":/bg/Image/git.png", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(u"QMainWindow{\n"
"	background-color:rgb(245,245,245);\n"
"}\n"
"\n"
"/**********************************QGroupBox*****************************************/\n"
"QGroupBox {\n"
"	border:1px solid rgb(230,230,230);\n"
"	margin-top: 1.5ex;\n"
"}\n"
"\n"
"QGroupBox::title {\n"
"	color: rgb(0, 0, 0);\n"
"	subcontrol-origin: margin;\n"
"	subcontrol-position: top left;\n"
"	left:10px;\n"
"	top:0px;\n"
"	padding: 0px 3px;\n"
"}\n"
"\n"
"/**********************************QTableView*****************************************/\n"
"QTableView {\n"
"    /*\u8868\u683c\u5185\u6587\u5b57\u989c\u8272*/\n"
"    color: black;\n"
"    /*\u8868\u683c\u5185\u80cc\u666f\u8272*/\n"
"    background-color: rgb(255, 255, 255);\n"
"    alternate-background-color: rgb(245, 245, 245);\n"
"    /*\u9009\u4e2d\u533a\u57df\u7684\u6587\u5b57\u989c\u8272*/\n"
"    selection-color: black;\n"
"    /*\u9009\u4e2d\u533a\u57df\u7684\u80cc\u666f\u8272*/\n"
"    selection-background-color: rgb(200, 220, 246);\n"
"    border: 1px solid rgb(210,210,210);\n"
""
                        "    border-radius: 0px;\n"
"    padding: 2px 4px;\n"
"}\n"
"\n"
"\n"
"QHeaderView::section{\n"
"    background-color: rgb(131, 194, 235);\n"
"    padding-left: 4px;\n"
"    border-bottom: 2px solid grey;\n"
"    height: 18;\n"
"}\n"
"\n"
"/**********************************QPushButton*****************************************/\n"
"QPushButton{\n"
"	padding:2px 5px 2px;\n"
"	border-radius: 2px;\n"
"	border:1px solid rgb(210,210,210);\n"
"	background-color: rgb(246,246,246);\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(239,239,239);\n"
" }\n"
"QPushButton:pressed{\n"
"	background-color:rgb(232,232,232);\n"
" }\n"
"\n"
"/**********************************QComboBox*****************************************/\n"
"QComboBox {\n"
"    color: #666666;\n"
"    font-size: 12px;\n"
"    padding: 1px 15px 1px 3px;\n"
"    border: 1px solid rgba(228, 228, 228, 1);\n"
"    border-radius: 5px 5px 0px 0px;\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;"
                        "\n"
"    width: 15px;\n"
"    border: none;\n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setSpacing(9)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(9, 9, 9, 0)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.groupBox_3 = QGroupBox(self.centralwidget)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.verticalLayout_5 = QVBoxLayout(self.groupBox_3)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_slider_id3 = QLabel(self.groupBox_3)
        self.label_slider_id3.setObjectName(u"label_slider_id3")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_slider_id3.sizePolicy().hasHeightForWidth())
        self.label_slider_id3.setSizePolicy(sizePolicy)
        self.label_slider_id3.setMinimumSize(QSize(30, 0))
        self.label_slider_id3.setLayoutDirection(Qt.LeftToRight)
        self.label_slider_id3.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_slider_id3, 3, 2, 1, 1)

        self.horizontalSlider_1 = QSlider(self.groupBox_3)
        self.horizontalSlider_1.setObjectName(u"horizontalSlider_1")
        sizePolicy.setHeightForWidth(self.horizontalSlider_1.sizePolicy().hasHeightForWidth())
        self.horizontalSlider_1.setSizePolicy(sizePolicy)
        self.horizontalSlider_1.setMinimum(0)
        self.horizontalSlider_1.setMaximum(180)
        self.horizontalSlider_1.setOrientation(Qt.Horizontal)
        self.horizontalSlider_1.setTickPosition(QSlider.NoTicks)
        self.horizontalSlider_1.setTickInterval(0)

        self.gridLayout.addWidget(self.horizontalSlider_1, 1, 1, 1, 1)

        self.horizontalSlider_5 = QSlider(self.groupBox_3)
        self.horizontalSlider_5.setObjectName(u"horizontalSlider_5")
        sizePolicy.setHeightForWidth(self.horizontalSlider_5.sizePolicy().hasHeightForWidth())
        self.horizontalSlider_5.setSizePolicy(sizePolicy)
        self.horizontalSlider_5.setMinimum(0)
        self.horizontalSlider_5.setMaximum(180)
        self.horizontalSlider_5.setOrientation(Qt.Horizontal)
        self.horizontalSlider_5.setTickPosition(QSlider.NoTicks)
        self.horizontalSlider_5.setTickInterval(0)

        self.gridLayout.addWidget(self.horizontalSlider_5, 5, 1, 1, 1)

        self.horizontalSlider_3 = QSlider(self.groupBox_3)
        self.horizontalSlider_3.setObjectName(u"horizontalSlider_3")
        sizePolicy.setHeightForWidth(self.horizontalSlider_3.sizePolicy().hasHeightForWidth())
        self.horizontalSlider_3.setSizePolicy(sizePolicy)
        self.horizontalSlider_3.setMinimum(0)
        self.horizontalSlider_3.setMaximum(180)
        self.horizontalSlider_3.setOrientation(Qt.Horizontal)
        self.horizontalSlider_3.setTickPosition(QSlider.NoTicks)
        self.horizontalSlider_3.setTickInterval(0)

        self.gridLayout.addWidget(self.horizontalSlider_3, 3, 1, 1, 1)

        self.comboBox_time_select = QComboBox(self.groupBox_3)
        self.comboBox_time_select.addItem("")
        self.comboBox_time_select.addItem("")
        self.comboBox_time_select.addItem("")
        self.comboBox_time_select.addItem("")
        self.comboBox_time_select.addItem("")
        self.comboBox_time_select.addItem("")
        self.comboBox_time_select.setObjectName(u"comboBox_time_select")

        self.gridLayout.addWidget(self.comboBox_time_select, 0, 1, 1, 1)

        self.label_slider_id1 = QLabel(self.groupBox_3)
        self.label_slider_id1.setObjectName(u"label_slider_id1")
        sizePolicy.setHeightForWidth(self.label_slider_id1.sizePolicy().hasHeightForWidth())
        self.label_slider_id1.setSizePolicy(sizePolicy)
        self.label_slider_id1.setMinimumSize(QSize(30, 0))
        self.label_slider_id1.setLayoutDirection(Qt.LeftToRight)
        self.label_slider_id1.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_slider_id1, 1, 2, 1, 1)

        self.label_slider_id4 = QLabel(self.groupBox_3)
        self.label_slider_id4.setObjectName(u"label_slider_id4")
        sizePolicy.setHeightForWidth(self.label_slider_id4.sizePolicy().hasHeightForWidth())
        self.label_slider_id4.setSizePolicy(sizePolicy)
        self.label_slider_id4.setMinimumSize(QSize(30, 0))
        self.label_slider_id4.setLayoutDirection(Qt.LeftToRight)
        self.label_slider_id4.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_slider_id4, 4, 2, 1, 1)

        self.label_slider_id6 = QLabel(self.groupBox_3)
        self.label_slider_id6.setObjectName(u"label_slider_id6")
        sizePolicy.setHeightForWidth(self.label_slider_id6.sizePolicy().hasHeightForWidth())
        self.label_slider_id6.setSizePolicy(sizePolicy)
        self.label_slider_id6.setMinimumSize(QSize(30, 0))
        self.label_slider_id6.setLayoutDirection(Qt.LeftToRight)
        self.label_slider_id6.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_slider_id6, 6, 2, 1, 1)

        self.label_time = QLabel(self.groupBox_3)
        self.label_time.setObjectName(u"label_time")
        sizePolicy.setHeightForWidth(self.label_time.sizePolicy().hasHeightForWidth())
        self.label_time.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.label_time, 0, 0, 1, 1)

        self.horizontalSlider_2 = QSlider(self.groupBox_3)
        self.horizontalSlider_2.setObjectName(u"horizontalSlider_2")
        sizePolicy.setHeightForWidth(self.horizontalSlider_2.sizePolicy().hasHeightForWidth())
        self.horizontalSlider_2.setSizePolicy(sizePolicy)
        self.horizontalSlider_2.setMinimum(0)
        self.horizontalSlider_2.setMaximum(180)
        self.horizontalSlider_2.setOrientation(Qt.Horizontal)
        self.horizontalSlider_2.setTickPosition(QSlider.NoTicks)
        self.horizontalSlider_2.setTickInterval(0)

        self.gridLayout.addWidget(self.horizontalSlider_2, 2, 1, 1, 1)

        self.label_ms = QLabel(self.groupBox_3)
        self.label_ms.setObjectName(u"label_ms")
        sizePolicy.setHeightForWidth(self.label_ms.sizePolicy().hasHeightForWidth())
        self.label_ms.setSizePolicy(sizePolicy)
        self.label_ms.setMinimumSize(QSize(30, 0))
        self.label_ms.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_ms, 0, 2, 1, 1)

        self.label_slider_id5 = QLabel(self.groupBox_3)
        self.label_slider_id5.setObjectName(u"label_slider_id5")
        sizePolicy.setHeightForWidth(self.label_slider_id5.sizePolicy().hasHeightForWidth())
        self.label_slider_id5.setSizePolicy(sizePolicy)
        self.label_slider_id5.setMinimumSize(QSize(30, 0))
        self.label_slider_id5.setLayoutDirection(Qt.LeftToRight)
        self.label_slider_id5.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_slider_id5, 5, 2, 1, 1)

        self.label_id2 = QLabel(self.groupBox_3)
        self.label_id2.setObjectName(u"label_id2")

        self.gridLayout.addWidget(self.label_id2, 2, 0, 1, 1)

        self.label_id5 = QLabel(self.groupBox_3)
        self.label_id5.setObjectName(u"label_id5")

        self.gridLayout.addWidget(self.label_id5, 5, 0, 1, 1)

        self.label_slider_id2 = QLabel(self.groupBox_3)
        self.label_slider_id2.setObjectName(u"label_slider_id2")
        sizePolicy.setHeightForWidth(self.label_slider_id2.sizePolicy().hasHeightForWidth())
        self.label_slider_id2.setSizePolicy(sizePolicy)
        self.label_slider_id2.setMinimumSize(QSize(30, 0))
        self.label_slider_id2.setLayoutDirection(Qt.LeftToRight)
        self.label_slider_id2.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_slider_id2, 2, 2, 1, 1)

        self.horizontalSlider_6 = QSlider(self.groupBox_3)
        self.horizontalSlider_6.setObjectName(u"horizontalSlider_6")
        sizePolicy.setHeightForWidth(self.horizontalSlider_6.sizePolicy().hasHeightForWidth())
        self.horizontalSlider_6.setSizePolicy(sizePolicy)
        self.horizontalSlider_6.setMinimum(0)
        self.horizontalSlider_6.setMaximum(180)
        self.horizontalSlider_6.setOrientation(Qt.Horizontal)
        self.horizontalSlider_6.setTickPosition(QSlider.NoTicks)
        self.horizontalSlider_6.setTickInterval(0)

        self.gridLayout.addWidget(self.horizontalSlider_6, 6, 1, 1, 1)

        self.label_id6 = QLabel(self.groupBox_3)
        self.label_id6.setObjectName(u"label_id6")

        self.gridLayout.addWidget(self.label_id6, 6, 0, 1, 1)

        self.label_id1 = QLabel(self.groupBox_3)
        self.label_id1.setObjectName(u"label_id1")
        sizePolicy.setHeightForWidth(self.label_id1.sizePolicy().hasHeightForWidth())
        self.label_id1.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.label_id1, 1, 0, 1, 1)

        self.horizontalSlider_4 = QSlider(self.groupBox_3)
        self.horizontalSlider_4.setObjectName(u"horizontalSlider_4")
        sizePolicy.setHeightForWidth(self.horizontalSlider_4.sizePolicy().hasHeightForWidth())
        self.horizontalSlider_4.setSizePolicy(sizePolicy)
        self.horizontalSlider_4.setMinimum(0)
        self.horizontalSlider_4.setMaximum(180)
        self.horizontalSlider_4.setOrientation(Qt.Horizontal)
        self.horizontalSlider_4.setTickPosition(QSlider.NoTicks)
        self.horizontalSlider_4.setTickInterval(0)

        self.gridLayout.addWidget(self.horizontalSlider_4, 4, 1, 1, 1)

        self.label_id3 = QLabel(self.groupBox_3)
        self.label_id3.setObjectName(u"label_id3")

        self.gridLayout.addWidget(self.label_id3, 3, 0, 1, 1)

        self.label_id4 = QLabel(self.groupBox_3)
        self.label_id4.setObjectName(u"label_id4")

        self.gridLayout.addWidget(self.label_id4, 4, 0, 1, 1)

        self.pushButton_update_frame = QPushButton(self.groupBox_3)
        self.pushButton_update_frame.setObjectName(u"pushButton_update_frame")

        self.gridLayout.addWidget(self.pushButton_update_frame, 7, 1, 1, 1)

        self.pushButton_del_frame = QPushButton(self.groupBox_3)
        self.pushButton_del_frame.setObjectName(u"pushButton_del_frame")

        self.gridLayout.addWidget(self.pushButton_del_frame, 7, 2, 1, 1)

        self.pushButton_add_frame = QPushButton(self.groupBox_3)
        self.pushButton_add_frame.setObjectName(u"pushButton_add_frame")

        self.gridLayout.addWidget(self.pushButton_add_frame, 7, 0, 1, 1)


        self.verticalLayout_5.addLayout(self.gridLayout)


        self.verticalLayout.addWidget(self.groupBox_3)

        self.verticalSpacer_2 = QSpacerItem(20, 15, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.groupBox_2 = QGroupBox(self.centralwidget)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.verticalLayout_4 = QVBoxLayout(self.groupBox_2)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.comboBox_choose_act = QComboBox(self.groupBox_2)
        self.comboBox_choose_act.addItem("")
        self.comboBox_choose_act.addItem("")
        self.comboBox_choose_act.addItem("")
        self.comboBox_choose_act.addItem("")
        self.comboBox_choose_act.addItem("")
        self.comboBox_choose_act.addItem("")
        self.comboBox_choose_act.addItem("")
        self.comboBox_choose_act.addItem("")
        self.comboBox_choose_act.addItem("")
        self.comboBox_choose_act.addItem("")
        self.comboBox_choose_act.addItem("")
        self.comboBox_choose_act.setObjectName(u"comboBox_choose_act")
        self.comboBox_choose_act.setLayoutDirection(Qt.LeftToRight)

        self.gridLayout_2.addWidget(self.comboBox_choose_act, 0, 1, 1, 1)

        self.pushButton_stop_act = QPushButton(self.groupBox_2)
        self.pushButton_stop_act.setObjectName(u"pushButton_stop_act")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.pushButton_stop_act.sizePolicy().hasHeightForWidth())
        self.pushButton_stop_act.setSizePolicy(sizePolicy1)

        self.gridLayout_2.addWidget(self.pushButton_stop_act, 1, 1, 1, 1)

        self.pushButton_start_act = QPushButton(self.groupBox_2)
        self.pushButton_start_act.setObjectName(u"pushButton_start_act")
        sizePolicy1.setHeightForWidth(self.pushButton_start_act.sizePolicy().hasHeightForWidth())
        self.pushButton_start_act.setSizePolicy(sizePolicy1)

        self.gridLayout_2.addWidget(self.pushButton_start_act, 1, 0, 1, 1)

        self.label = QLabel(self.groupBox_2)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)

        self.pushButton_download = QPushButton(self.groupBox_2)
        self.pushButton_download.setObjectName(u"pushButton_download")
        sizePolicy1.setHeightForWidth(self.pushButton_download.sizePolicy().hasHeightForWidth())
        self.pushButton_download.setSizePolicy(sizePolicy1)

        self.gridLayout_2.addWidget(self.pushButton_download, 2, 0, 1, 1)

        self.pushButton_clear = QPushButton(self.groupBox_2)
        self.pushButton_clear.setObjectName(u"pushButton_clear")
        sizePolicy1.setHeightForWidth(self.pushButton_clear.sizePolicy().hasHeightForWidth())
        self.pushButton_clear.setSizePolicy(sizePolicy1)

        self.gridLayout_2.addWidget(self.pushButton_clear, 2, 1, 1, 1)


        self.verticalLayout_4.addLayout(self.gridLayout_2)


        self.verticalLayout.addWidget(self.groupBox_2)

        self.verticalSpacer = QSpacerItem(20, 15, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.verticalLayout_3 = QVBoxLayout(self.groupBox)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.label_port = QLabel(self.groupBox)
        self.label_port.setObjectName(u"label_port")
        sizePolicy2 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.label_port.sizePolicy().hasHeightForWidth())
        self.label_port.setSizePolicy(sizePolicy2)
        self.label_port.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_3.addWidget(self.label_port, 0, 0, 1, 1)

        self.comboBox_baud = QComboBox(self.groupBox)
        self.comboBox_baud.setObjectName(u"comboBox_baud")

        self.gridLayout_3.addWidget(self.comboBox_baud, 1, 1, 1, 1)

        self.comboBox_port = QComboBox(self.groupBox)
        self.comboBox_port.setObjectName(u"comboBox_port")

        self.gridLayout_3.addWidget(self.comboBox_port, 0, 1, 1, 1)

        self.label_bard_2 = QLabel(self.groupBox)
        self.label_bard_2.setObjectName(u"label_bard_2")
        sizePolicy2.setHeightForWidth(self.label_bard_2.sizePolicy().hasHeightForWidth())
        self.label_bard_2.setSizePolicy(sizePolicy2)
        self.label_bard_2.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_3.addWidget(self.label_bard_2, 3, 0, 1, 1)

        self.comboBox_parity = QComboBox(self.groupBox)
        self.comboBox_parity.setObjectName(u"comboBox_parity")

        self.gridLayout_3.addWidget(self.comboBox_parity, 3, 1, 1, 1)

        self.label_bard_3 = QLabel(self.groupBox)
        self.label_bard_3.setObjectName(u"label_bard_3")
        sizePolicy2.setHeightForWidth(self.label_bard_3.sizePolicy().hasHeightForWidth())
        self.label_bard_3.setSizePolicy(sizePolicy2)
        self.label_bard_3.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_3.addWidget(self.label_bard_3, 4, 0, 1, 1)

        self.comboBox_stop_bits = QComboBox(self.groupBox)
        self.comboBox_stop_bits.setObjectName(u"comboBox_stop_bits")

        self.gridLayout_3.addWidget(self.comboBox_stop_bits, 4, 1, 1, 1)

        self.label_bard = QLabel(self.groupBox)
        self.label_bard.setObjectName(u"label_bard")
        sizePolicy2.setHeightForWidth(self.label_bard.sizePolicy().hasHeightForWidth())
        self.label_bard.setSizePolicy(sizePolicy2)
        self.label_bard.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_3.addWidget(self.label_bard, 1, 0, 1, 1)

        self.label_bard_9 = QLabel(self.groupBox)
        self.label_bard_9.setObjectName(u"label_bard_9")
        sizePolicy2.setHeightForWidth(self.label_bard_9.sizePolicy().hasHeightForWidth())
        self.label_bard_9.setSizePolicy(sizePolicy2)
        self.label_bard_9.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_3.addWidget(self.label_bard_9, 2, 0, 1, 1)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_start_stop_icon = QLabel(self.groupBox)
        self.label_start_stop_icon.setObjectName(u"label_start_stop_icon")
        sizePolicy1.setHeightForWidth(self.label_start_stop_icon.sizePolicy().hasHeightForWidth())
        self.label_start_stop_icon.setSizePolicy(sizePolicy1)
        self.label_start_stop_icon.setMinimumSize(QSize(0, 0))
        self.label_start_stop_icon.setMaximumSize(QSize(20, 20))
        self.label_start_stop_icon.setPixmap(QPixmap(u":/bg/Image/failed.png"))
        self.label_start_stop_icon.setScaledContents(True)

        self.horizontalLayout_3.addWidget(self.label_start_stop_icon)


        self.gridLayout_3.addLayout(self.horizontalLayout_3, 5, 0, 1, 1)

        self.comboBox_data_bits = QComboBox(self.groupBox)
        self.comboBox_data_bits.setObjectName(u"comboBox_data_bits")

        self.gridLayout_3.addWidget(self.comboBox_data_bits, 2, 1, 1, 1)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.pushButton_start_port = QPushButton(self.groupBox)
        self.pushButton_start_port.setObjectName(u"pushButton_start_port")
        sizePolicy1.setHeightForWidth(self.pushButton_start_port.sizePolicy().hasHeightForWidth())
        self.pushButton_start_port.setSizePolicy(sizePolicy1)

        self.horizontalLayout_7.addWidget(self.pushButton_start_port)

        self.pushButton_close_port = QPushButton(self.groupBox)
        self.pushButton_close_port.setObjectName(u"pushButton_close_port")

        self.horizontalLayout_7.addWidget(self.pushButton_close_port)


        self.gridLayout_3.addLayout(self.horizontalLayout_7, 5, 1, 1, 1)


        self.verticalLayout_3.addLayout(self.gridLayout_3)


        self.verticalLayout.addWidget(self.groupBox)


        self.horizontalLayout.addLayout(self.verticalLayout)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.tableWidget = QTableWidget(self.centralwidget)
        if (self.tableWidget.columnCount() < 8):
            self.tableWidget.setColumnCount(8)
        brush = QBrush(QColor(0, 0, 0, 255))
        brush.setStyle(Qt.SolidPattern)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setForeground(brush);
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(7, __qtablewidgetitem7)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.tableWidget.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.tableWidget.setAutoScrollMargin(16)
        self.tableWidget.setGridStyle(Qt.DotLine)

        self.verticalLayout_2.addWidget(self.tableWidget)

        self.verticalLayout_chart = QVBoxLayout()
        self.verticalLayout_chart.setObjectName(u"verticalLayout_chart")

        self.verticalLayout_2.addLayout(self.verticalLayout_chart)


        self.horizontalLayout.addLayout(self.verticalLayout_2)

        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.groupBox_4 = QGroupBox(self.centralwidget)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.gridLayout_6 = QGridLayout(self.groupBox_4)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.textEdit_read = QTextEdit(self.groupBox_4)
        self.textEdit_read.setObjectName(u"textEdit_read")
        sizePolicy.setHeightForWidth(self.textEdit_read.sizePolicy().hasHeightForWidth())
        self.textEdit_read.setSizePolicy(sizePolicy)
        self.textEdit_read.setMinimumSize(QSize(0, 150))
        self.textEdit_read.setMaximumSize(QSize(16777215, 150))
        self.textEdit_read.setFocusPolicy(Qt.NoFocus)

        self.gridLayout_6.addWidget(self.textEdit_read, 0, 0, 1, 1)

        self.pushButton_clear_read = QPushButton(self.groupBox_4)
        self.pushButton_clear_read.setObjectName(u"pushButton_clear_read")
        self.pushButton_clear_read.setFocusPolicy(Qt.StrongFocus)

        self.gridLayout_6.addWidget(self.pushButton_clear_read, 1, 0, 1, 1)


        self.verticalLayout_7.addWidget(self.groupBox_4)

        self.groupBox_5 = QGroupBox(self.centralwidget)
        self.groupBox_5.setObjectName(u"groupBox_5")
        self.gridLayout_5 = QGridLayout(self.groupBox_5)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_7 = QGridLayout()
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.pushButton_send_text = QPushButton(self.groupBox_5)
        self.pushButton_send_text.setObjectName(u"pushButton_send_text")

        self.gridLayout_7.addWidget(self.pushButton_send_text, 0, 0, 1, 1)

        self.pushButton_clear_write = QPushButton(self.groupBox_5)
        self.pushButton_clear_write.setObjectName(u"pushButton_clear_write")

        self.gridLayout_7.addWidget(self.pushButton_clear_write, 0, 1, 1, 1)


        self.gridLayout_5.addLayout(self.gridLayout_7, 1, 0, 1, 1)

        self.textEdit_write = QTextEdit(self.groupBox_5)
        self.textEdit_write.setObjectName(u"textEdit_write")
        sizePolicy.setHeightForWidth(self.textEdit_write.sizePolicy().hasHeightForWidth())
        self.textEdit_write.setSizePolicy(sizePolicy)
        self.textEdit_write.setMinimumSize(QSize(0, 150))
        self.textEdit_write.setMaximumSize(QSize(16777215, 150))

        self.gridLayout_5.addWidget(self.textEdit_write, 0, 0, 1, 1)


        self.verticalLayout_7.addWidget(self.groupBox_5)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_7.addItem(self.verticalSpacer_3)

        self.gridLayout_4 = QGridLayout()
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.pushButton_ins1 = QPushButton(self.centralwidget)
        self.pushButton_ins1.setObjectName(u"pushButton_ins1")

        self.verticalLayout_6.addWidget(self.pushButton_ins1)

        self.pushButton_ins2 = QPushButton(self.centralwidget)
        self.pushButton_ins2.setObjectName(u"pushButton_ins2")

        self.verticalLayout_6.addWidget(self.pushButton_ins2)

        self.pushButton_ins3 = QPushButton(self.centralwidget)
        self.pushButton_ins3.setObjectName(u"pushButton_ins3")

        self.verticalLayout_6.addWidget(self.pushButton_ins3)

        self.pushButton_ins4 = QPushButton(self.centralwidget)
        self.pushButton_ins4.setObjectName(u"pushButton_ins4")

        self.verticalLayout_6.addWidget(self.pushButton_ins4)


        self.gridLayout_4.addLayout(self.verticalLayout_6, 0, 2, 1, 1)


        self.verticalLayout_7.addLayout(self.gridLayout_4)


        self.horizontalLayout.addLayout(self.verticalLayout_7)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1180, 22))
        self.menu = QMenu(self.menubar)
        self.menu.setObjectName(u"menu")
        self.menuhelp = QMenu(self.menubar)
        self.menuhelp.setObjectName(u"menuhelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menuhelp.menuAction())

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u673a\u68b0\u81c2\u4e0a\u4f4d\u673a", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"\u8235\u673a\u89d2\u5ea6\u63a7\u5236", None))
        self.label_slider_id3.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.comboBox_time_select.setItemText(0, QCoreApplication.translate("MainWindow", u"1000", None))
        self.comboBox_time_select.setItemText(1, QCoreApplication.translate("MainWindow", u"1100", None))
        self.comboBox_time_select.setItemText(2, QCoreApplication.translate("MainWindow", u"1200", None))
        self.comboBox_time_select.setItemText(3, QCoreApplication.translate("MainWindow", u"1300", None))
        self.comboBox_time_select.setItemText(4, QCoreApplication.translate("MainWindow", u"1400", None))
        self.comboBox_time_select.setItemText(5, QCoreApplication.translate("MainWindow", u"1500", None))

        self.label_slider_id1.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_slider_id4.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_slider_id6.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_time.setText(QCoreApplication.translate("MainWindow", u"\u65f6\u95f4\uff1a", None))
        self.label_ms.setText(QCoreApplication.translate("MainWindow", u"ms", None))
        self.label_slider_id5.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_id2.setText(QCoreApplication.translate("MainWindow", u"ID:2", None))
        self.label_id5.setText(QCoreApplication.translate("MainWindow", u"ID:5", None))
        self.label_slider_id2.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_id6.setText(QCoreApplication.translate("MainWindow", u"ID:6", None))
        self.label_id1.setText(QCoreApplication.translate("MainWindow", u"ID:1", None))
        self.label_id3.setText(QCoreApplication.translate("MainWindow", u"ID:3", None))
        self.label_id4.setText(QCoreApplication.translate("MainWindow", u"ID:4", None))
        self.pushButton_update_frame.setText(QCoreApplication.translate("MainWindow", u"\u66f4\u65b0\u52a8\u4f5c\u5e27", None))
        self.pushButton_del_frame.setText(QCoreApplication.translate("MainWindow", u"\u5220\u9664\u52a8\u4f5c\u5e27", None))
        self.pushButton_add_frame.setText(QCoreApplication.translate("MainWindow", u"\u6dfb\u52a0\u52a8\u4f5c\u5e27", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"\u52a8\u4f5c\u7ec4", None))
        self.comboBox_choose_act.setItemText(0, QCoreApplication.translate("MainWindow", u"0", None))
        self.comboBox_choose_act.setItemText(1, QCoreApplication.translate("MainWindow", u"1", None))
        self.comboBox_choose_act.setItemText(2, QCoreApplication.translate("MainWindow", u"2", None))
        self.comboBox_choose_act.setItemText(3, QCoreApplication.translate("MainWindow", u"3", None))
        self.comboBox_choose_act.setItemText(4, QCoreApplication.translate("MainWindow", u"4", None))
        self.comboBox_choose_act.setItemText(5, QCoreApplication.translate("MainWindow", u"5", None))
        self.comboBox_choose_act.setItemText(6, QCoreApplication.translate("MainWindow", u"6", None))
        self.comboBox_choose_act.setItemText(7, QCoreApplication.translate("MainWindow", u"7", None))
        self.comboBox_choose_act.setItemText(8, QCoreApplication.translate("MainWindow", u"8", None))
        self.comboBox_choose_act.setItemText(9, QCoreApplication.translate("MainWindow", u"9", None))
        self.comboBox_choose_act.setItemText(10, QCoreApplication.translate("MainWindow", u"100", None))

        self.pushButton_stop_act.setText(QCoreApplication.translate("MainWindow", u"\u505c\u6b62\u6267\u884c", None))
        self.pushButton_start_act.setText(QCoreApplication.translate("MainWindow", u"\u5f00\u59cb\u6267\u884c", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u6307\u5b9a\u52a8\u4f5c\u7ec4\uff1a", None))
#if QT_CONFIG(tooltip)
        self.pushButton_download.setToolTip(QCoreApplication.translate("MainWindow", u"\u5c06\u53f3\u4fa7\u8868\u683c\u4e2d\u7684\u52a8\u4f5c\u5e27\u70e7\u5199\u5230\u6307\u4ee4\u7684\u52a8\u4f5c\u7ec4", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_download.setText(QCoreApplication.translate("MainWindow", u"\u70e7\u5199\u52a8\u4f5c\u7ec4", None))
#if QT_CONFIG(tooltip)
        self.pushButton_clear.setToolTip(QCoreApplication.translate("MainWindow", u"\u64e6\u9664\u6307\u5b9a\u7684\u52a8\u4f5c\u7ec4\u6587\u4ef6", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_clear.setText(QCoreApplication.translate("MainWindow", u"\u64e6\u9664\u52a8\u4f5c\u7ec4", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"\u4e32\u53e3\u8bbe\u7f6e", None))
        self.label_port.setText(QCoreApplication.translate("MainWindow", u"Port\uff1a", None))
        self.label_bard_2.setText(QCoreApplication.translate("MainWindow", u"Parity\uff1a", None))
        self.label_bard_3.setText(QCoreApplication.translate("MainWindow", u"Stop bits\uff1a", None))
        self.label_bard.setText(QCoreApplication.translate("MainWindow", u"BaudRate\uff1a", None))
        self.label_bard_9.setText(QCoreApplication.translate("MainWindow", u"Data bits\uff1a", None))
        self.label_start_stop_icon.setText("")
        self.pushButton_start_port.setText(QCoreApplication.translate("MainWindow", u"\u5f00\u542f\u4e32\u53e3", None))
        self.pushButton_close_port.setText(QCoreApplication.translate("MainWindow", u"\u5173\u95ed\u4e32\u53e3", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"\u7f16\u53f7", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"\u65f6\u95f4(ms)", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"ID:1", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"ID:2", None));
        ___qtablewidgetitem4 = self.tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"ID:3", None));
        ___qtablewidgetitem5 = self.tableWidget.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"ID:4", None));
        ___qtablewidgetitem6 = self.tableWidget.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"ID:5", None));
        ___qtablewidgetitem7 = self.tableWidget.horizontalHeaderItem(7)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"ID:6", None));
        self.groupBox_4.setTitle(QCoreApplication.translate("MainWindow", u"\u63a5\u53d7\u7a97\u53e3", None))
        self.pushButton_clear_read.setText(QCoreApplication.translate("MainWindow", u"\u6e05\u9664", None))
        self.groupBox_5.setTitle(QCoreApplication.translate("MainWindow", u"\u53d1\u9001\u7a97\u53e3", None))
        self.pushButton_send_text.setText(QCoreApplication.translate("MainWindow", u"\u53d1\u9001", None))
        self.pushButton_clear_write.setText(QCoreApplication.translate("MainWindow", u"\u6e05\u9664", None))
        self.pushButton_ins1.setText(QCoreApplication.translate("MainWindow", u"\u6307\u4ee41", None))
        self.pushButton_ins2.setText(QCoreApplication.translate("MainWindow", u"\u6307\u4ee42", None))
        self.pushButton_ins3.setText(QCoreApplication.translate("MainWindow", u"\u6307\u4ee43", None))
        self.pushButton_ins4.setText(QCoreApplication.translate("MainWindow", u"\u5173\u95ed\u89d2\u5ea6\u91c7\u96c6", None))
        self.menu.setTitle(QCoreApplication.translate("MainWindow", u"Menu", None))
        self.menuhelp.setTitle(QCoreApplication.translate("MainWindow", u"Help", None))
    # retranslateUi

