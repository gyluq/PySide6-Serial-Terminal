# Copyright (C) 2022 The Qt Company Ltd.
# SPDX-License-Identifier: LicenseRef-Qt-Commercial OR BSD-3-Clause
# -*- coding: utf-8 -*-
import sys

from PySide6 import QtCore, QtWidgets
from PySide6.QtCharts import QChart, QChartView
from PySide6.QtCore import QIODeviceBase, Slot, Qt
from PySide6.QtGui import QPixmap, QPainter
from PySide6.QtWidgets import QLabel, QMainWindow, QMessageBox, QTableWidgetItem, QAbstractItemView
from PySide6.QtSerialPort import QSerialPort, QSerialPortInfo

from m_thread import Thread_detect_port
from ui_main import Ui_MainWindow
from chart import Chart

HELP = """The <b>Simple Terminal</b> example demonstrates how to
 use the Qt Serial Port module in modern GUI applications
 using Qt, with a menu bar, toolbars, and a status bar."""


def description(s):
    return (f"Connected to {s.name} : {s.string_baud_rate}, "
            f"{s.string_data_bits}, {s.string_parity}, {s.string_stop_bits}, "
            f"{s.string_flow_control}")


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.m_ui = Ui_MainWindow()
        self.m_status = QLabel()
        self.m_serial = QSerialPort(self)
        self.m_ui.setupUi(self)

        # 状态栏
        self.m_ui.statusbar.addWidget(self.m_status)

        # 串口控制按钮使能、失能
        self.m_ui.pushButton_start_port.setEnabled(True)
        self.m_ui.pushButton_close_port.setEnabled(False)

        # 连接信号与槽，同步slider值与label文本
        self.m_ui.horizontalSlider_1.valueChanged.connect(lambda: self.update_label_val(1))
        self.m_ui.horizontalSlider_2.valueChanged.connect(lambda: self.update_label_val(2))
        self.m_ui.horizontalSlider_3.valueChanged.connect(lambda: self.update_label_val(3))
        self.m_ui.horizontalSlider_4.valueChanged.connect(lambda: self.update_label_val(4))
        self.m_ui.horizontalSlider_5.valueChanged.connect(lambda: self.update_label_val(5))
        self.m_ui.horizontalSlider_6.valueChanged.connect(lambda: self.update_label_val(6))

        # 连接信号与槽，开启检测按钮
        self.m_ui.pushButton_start_port.clicked.connect(self.open_serial_port)
        self.m_ui.pushButton_close_port.clicked.connect(self.close_serial_port)

        # 动作帧
        self.m_ui.pushButton_add_frame.clicked.connect(self.add_act_frame)
        self.m_ui.pushButton_del_frame.clicked.connect(self.del_act_frame)
        self.m_ui.pushButton_update_frame.clicked.connect(self.update_act_frame)

        # 表格设置
        self.m_ui.tableWidget.setShowGrid(True)
        self.m_ui.tableWidget.setGridStyle(Qt.PenStyle.SolidLine)  # 实线
        self.m_ui.tableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)  # 只能一行一行选择
        self.m_ui.tableWidget.resizeColumnToContents(0)  # 根据内容调整列宽
        self.m_ui.tableWidget.setAlternatingRowColors(True)
        self.m_ui.tableWidget.verticalHeader().setDefaultSectionSize(24)  # 设置单元格行高
        self.m_ui.tableWidget.verticalHeader().close()
        # font = self.m_ui.tableWidget.horizontalHeader().font()
        # font.setBold(True)
        # self.m_ui.tableWidget.horizontalHeader().setFont(font)
        self.m_ui.tableWidget.horizontalHeader().setStretchLastSection(True)  # 最后一列延伸至末尾
        self.m_ui.tableWidget.horizontalHeader().setDefaultAlignment(Qt.AlignLeft)
        self.m_ui.tableWidget.horizontalHeader().setHighlightSections(False)  # item被选中时，使其表头字体不变粗

        # 波特率选项
        self.m_ui.comboBox_baud.addItem("9600", QSerialPort.Baud9600)
        self.m_ui.comboBox_baud.addItem("19200", QSerialPort.Baud19200)
        self.m_ui.comboBox_baud.addItem("38400", QSerialPort.Baud38400)
        self.m_ui.comboBox_baud.addItem("115200", QSerialPort.Baud115200)
        self.m_ui.comboBox_baud.addItem("Custom")
        # 数据位数选项
        self.m_ui.comboBox_data_bits.addItem("5", QSerialPort.Data5)
        self.m_ui.comboBox_data_bits.addItem("6", QSerialPort.Data6)
        self.m_ui.comboBox_data_bits.addItem("7", QSerialPort.Data7)
        self.m_ui.comboBox_data_bits.addItem("8", QSerialPort.Data8)
        self.m_ui.comboBox_data_bits.setCurrentIndex(3)
        # 校验位
        self.m_ui.comboBox_parity.addItem("None", QSerialPort.NoParity)
        self.m_ui.comboBox_parity.addItem("Even", QSerialPort.EvenParity)
        self.m_ui.comboBox_parity.addItem("Odd", QSerialPort.OddParity)
        # 停止位
        self.m_ui.comboBox_stop_bits.addItem("1", QSerialPort.OneStop)
        if sys.platform == "win32":
            self.m_ui.comboBox_stop_bits.addItem("1.5", QSerialPort.OneAndHalfStop)
        self.m_ui.comboBox_stop_bits.addItem("2", QSerialPort.TwoStop)

        # 多线程检测端口
        self.m_thread = Thread_detect_port()
        self.m_thread._signal.connect(self.fill_ports_info)
        self.m_thread.start()

        # 收发串口数据
        self.m_serial.readyRead.connect(self.read_data)
        self.m_ui.pushButton_clear_read.clicked.connect(self.m_ui.textEdit_read.clear)
        self.m_ui.pushButton_clear_write.clicked.connect(self.m_ui.textEdit_write.clear)
        self.m_ui.pushButton_send_text.clicked.connect(self.send_textedit_data)

        # 固定指令按钮初始化
        self.m_ui.pushButton_ins1.clicked.connect(self.send_ins1)
        self.m_ui.pushButton_ins2.clicked.connect(self.send_ins2)
        self.m_ui.pushButton_ins3.clicked.connect(self.send_ins3)

        # 实时曲线
        self.chart = Chart()
        self.chart.setAnimationOptions(QChart.AllAnimations)
        self.chart_view = QChartView(self.chart)
        self.chart_view.setRenderHint(QPainter.Antialiasing)
        self.m_ui.verticalLayout_chart.addWidget(self.chart_view)
        self.m_ui.pushButton_ins4.clicked.connect(self.changeChartCollectState)

        # 拖动滑块事件
        self.m_ui.horizontalSlider_1.valueChanged.connect(
            lambda: self.chart.setPositionX(1, self.m_ui.horizontalSlider_1.value()))
        self.m_ui.horizontalSlider_2.valueChanged.connect(
            lambda: self.chart.setPositionX(2, self.m_ui.horizontalSlider_2.value()))
        self.m_ui.horizontalSlider_3.valueChanged.connect(
            lambda: self.chart.setPositionX(3, self.m_ui.horizontalSlider_3.value()))
        self.m_ui.horizontalSlider_4.valueChanged.connect(
            lambda: self.chart.setPositionX(4, self.m_ui.horizontalSlider_4.value()))
        self.m_ui.horizontalSlider_5.valueChanged.connect(
            lambda: self.chart.setPositionX(5, self.m_ui.horizontalSlider_5.value()))
        self.m_ui.horizontalSlider_6.valueChanged.connect(
            lambda: self.chart.setPositionX(6, self.m_ui.horizontalSlider_6.value()))

    @Slot()
    def update_label_val(self, param):
        if param == 1:
            self.m_ui.label_slider_id1.setText(f"{self.m_ui.horizontalSlider_1.value()}")
        if param == 2:
            self.m_ui.label_slider_id2.setText(f"{self.m_ui.horizontalSlider_2.value()}")
        if param == 3:
            self.m_ui.label_slider_id3.setText(f"{self.m_ui.horizontalSlider_3.value()}")
        if param == 4:
            self.m_ui.label_slider_id4.setText(f"{self.m_ui.horizontalSlider_4.value()}")
        if param == 5:
            self.m_ui.label_slider_id5.setText(f"{self.m_ui.horizontalSlider_5.value()}")
        if param == 6:
            self.m_ui.label_slider_id6.setText(f"{self.m_ui.horizontalSlider_6.value()}")

    @Slot()
    def fill_ports_info(self):
        self.m_ui.comboBox_port.clear()
        for info in QSerialPortInfo.availablePorts():
            self.m_ui.comboBox_port.addItem(info.portName())

    @Slot()
    def open_serial_port(self):
        # 获取配置
        self.m_serial.setPortName(self.m_ui.comboBox_port.currentText())
        self.m_serial.setBaudRate(self.m_ui.comboBox_baud.currentData())
        self.m_serial.setDataBits(self.m_ui.comboBox_data_bits.currentData())
        self.m_serial.setParity(self.m_ui.comboBox_parity.currentData())
        self.m_serial.setStopBits(self.m_ui.comboBox_stop_bits.currentData())
        self.m_serial.setFlowControl(QSerialPort.NoFlowControl)
        if self.m_serial.open(QIODeviceBase.ReadWrite):
            # 更换图标
            self.m_ui.label_start_stop_icon.setPixmap(QPixmap(u":/bg/Image/success.png"))
            self.m_ui.pushButton_start_port.setEnabled(False)
            self.m_ui.pushButton_close_port.setEnabled(True)
            self.show_status_message(f"Open {self.m_serial.portName()} success")
        else:
            QMessageBox.critical(self, "Error", self.m_serial.errorString())
            self.show_status_message("Open error")

    def show_status_message(self, message):
        self.m_status.setText(message)

    @Slot()
    def close_serial_port(self):
        if self.m_serial.isOpen():
            self.m_serial.close()
        self.m_ui.label_start_stop_icon.setPixmap(QPixmap(u":/bg/Image/failed.png"))
        self.m_ui.pushButton_start_port.setEnabled(True)
        self.m_ui.pushButton_close_port.setEnabled(False)
        self.show_status_message("Disconnected")

    @Slot()
    def add_act_frame(self):
        row = self.m_ui.tableWidget.rowCount()
        time = self.m_ui.comboBox_time_select.currentText()
        pos1 = self.m_ui.label_slider_id1.text()
        pos2 = self.m_ui.label_slider_id2.text()
        pos3 = self.m_ui.label_slider_id3.text()
        pos4 = self.m_ui.label_slider_id4.text()
        pos5 = self.m_ui.label_slider_id5.text()
        pos6 = self.m_ui.label_slider_id6.text()
        items = [f"{row + 1}", time, pos1, pos2, pos3, pos4, pos5, pos6]
        self.m_ui.tableWidget.insertRow(row)
        for i in range(8):
            item = QTableWidgetItem(items[i])
            self.m_ui.tableWidget.setItem(row, i, item)

    @Slot()
    def del_act_frame(self):
        selected_items = self.m_ui.tableWidget.selectedItems()
        size = len(selected_items)
        if size == 0:  # 说明没有选中任何行
            return
        # 因为只能一行一行的选择，故每次选择的item是8的倍数，跳越8获取每行第一个item，这样删除操作就不会重复
        for i in range(0, size, 8):
            row = self.m_ui.tableWidget.indexFromItem(selected_items[i]).row()
            self.m_ui.tableWidget.removeRow(row)
        # 编号需要更新
        for i in range(self.m_ui.tableWidget.rowCount()):
            # 表格行的索引从0开始，编号从1开始
            self.m_ui.tableWidget.setItem(i, 0, QTableWidgetItem(str(i + 1)))

    @Slot()
    def update_act_frame(self):
        selected_items = self.m_ui.tableWidget.selectedItems()

        if len(selected_items) == 0:  # 没有选择
            dlg = QMessageBox(self)
            dlg.setWindowTitle("提示")
            dlg.setText('请选择一行！')
            dlg.exec()
            return
        if len(selected_items) % 8 > 1:  # 超过一行
            dlg = QMessageBox(self)
            dlg.setWindowTitle("提示")
            dlg.setText('只能选择一行进行更新，你当前选择了多行！')
            dlg.exec()
            return
        row = self.m_ui.tableWidget.indexFromItem(selected_items[0]).row()
        time = self.m_ui.comboBox_time_select.currentText()
        pos1 = self.m_ui.label_slider_id1.text()
        pos2 = self.m_ui.label_slider_id2.text()
        pos3 = self.m_ui.label_slider_id3.text()
        pos4 = self.m_ui.label_slider_id4.text()
        pos5 = self.m_ui.label_slider_id5.text()
        pos6 = self.m_ui.label_slider_id6.text()
        items = [f"{row + 1}", time, pos1, pos2, pos3, pos4, pos5, pos6]
        for i in range(8):
            item = QTableWidgetItem(items[i])
            self.m_ui.tableWidget.setItem(row, i, item)

    @Slot()
    def send_textedit_data(self):
        self.write_data(self.m_ui.textEdit_write.toPlainText().encode("utf-8"))

    @Slot(bytearray)
    def write_data(self, data):
        self.m_serial.write(data)

    @Slot()
    def read_data(self):
        data = self.m_serial.readAll()
        try:
            self.m_ui.textEdit_read.insertPlainText(data.data().decode("utf-8"))
        except UnicodeDecodeError as e:
            print(e)

    @Slot()
    def send_ins1(self):
        self.write_data(bytes("ins1\n", encoding='utf-8'))

    @Slot()
    def send_ins2(self):
        self.write_data(bytes("ins2\n", encoding='utf-8'))

    @Slot()
    def send_ins3(self):
        self.write_data(bytes("ins3\n", encoding='utf-8'))

    @Slot()
    def changeChartCollectState(self):
        if self.m_ui.pushButton_ins4.text()[0] == "关":
            self.m_ui.pushButton_ins4.setText("开启角度采集")
            self.chart.closeCollect()
        else:
            self.m_ui.pushButton_ins4.setText("关闭角度采集")
            self.chart.startCollect()
