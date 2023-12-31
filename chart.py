# Copyright (C) 2022 The Qt Company Ltd.
# SPDX-License-Identifier: LicenseRef-Qt-Commercial OR BSD-3-Clause

import random

from PySide6.QtCharts import QChart, QSplineSeries, QValueAxis
from PySide6.QtCore import Qt, QTimer, Slot
from PySide6.QtGui import QPen, QColor


class Chart(QChart):
    def __init__(self, parent=None):
        super().__init__(QChart.ChartTypeCartesian, parent, Qt.WindowFlags())
        self._timer = QTimer()
        # 6条曲线
        self._series_id1 = QSplineSeries(self)
        self._series_id1.setName("id1")
        self._series_id2 = QSplineSeries(self)
        self._series_id2.setName("id2")
        self._series_id3 = QSplineSeries(self)
        self._series_id3.setName("id3")
        self._series_id4 = QSplineSeries(self)
        self._series_id4.setName("id4")
        self._series_id5 = QSplineSeries(self)
        self._series_id5.setName("id5")
        self._series_id6 = QSplineSeries(self)
        self._series_id6.setName("id6")
        # 轴
        self._axisX = QValueAxis()
        self._axisY = QValueAxis()
        self._axisX.setTickCount(11) # 水平轴分9格
        self._axisX.setRange(0, 30)
        self._axisY.setTickCount(11) # 水平轴分9格
        self._axisY.setRange(-10, 190)
        self.addAxis(self._axisX, Qt.AlignBottom)
        self.addAxis(self._axisY, Qt.AlignLeft)
        # 关节值
        self._cur_time = 0 # 时间
        self._y_id1 = 0
        self._y_id2 = 0
        self._y_id3 = 0
        self._y_id4 = 0
        self._y_id5 = 0
        self._y_id6 = 0
        # 定时器配置，1s钟调用一次
        self._timer.timeout.connect(self.handleTimeout)
        self._timer.setInterval(1000)
        # 笔刷配置
        color = QPen(Qt.red)
        color.setWidth(2)
        self._series_id1.setPen(color)
        color.setColor(Qt.blue)
        self._series_id2.setPen(color)
        color.setColor(QColor("#75dba7"))
        self._series_id3.setPen(color)
        color.setColor(Qt.magenta)
        self._series_id4.setPen(color)
        color.setColor(Qt.black)
        self._series_id5.setPen(color)
        color.setColor(Qt.lightGray)
        self._series_id6.setPen(color)
        # 初始值
        self._series_id1.append(self._cur_time, self._y_id1)
        self._series_id2.append(self._cur_time, self._y_id2)
        self._series_id3.append(self._cur_time, self._y_id3)
        self._series_id4.append(self._cur_time, self._y_id4)
        self._series_id5.append(self._cur_time, self._y_id5)
        self._series_id6.append(self._cur_time, self._y_id6)
        # 添加series
        self.addSeries(self._series_id1)
        self.addSeries(self._series_id2)
        self.addSeries(self._series_id3)
        self.addSeries(self._series_id4)
        self.addSeries(self._series_id5)
        self.addSeries(self._series_id6)
        # 绑定
        self._series_id1.attachAxis(self._axisX)
        self._series_id1.attachAxis(self._axisY)
        self._series_id2.attachAxis(self._axisX)
        self._series_id2.attachAxis(self._axisY)
        self._series_id3.attachAxis(self._axisX)
        self._series_id3.attachAxis(self._axisY)
        self._series_id4.attachAxis(self._axisX)
        self._series_id4.attachAxis(self._axisY)
        self._series_id5.attachAxis(self._axisX)
        self._series_id5.attachAxis(self._axisY)
        self._series_id6.attachAxis(self._axisX)
        self._series_id6.attachAxis(self._axisY)
        self._timer.start()

    def setPositionX(self, param, val):
        if param == 1:
            self._y_id1 = val
        if param == 2:
            self._y_id2 = val
        if param == 3:
            self._y_id3 = val
        if param == 4:
            self._y_id4 = val
        if param == 5:
            self._y_id5 = val
        if param == 6:
            self._y_id6 = val

    def closeCollect(self):
        self._timer.stop()

    def startCollect(self):
        self._timer.start()

    @Slot()
    def handleTimeout(self):
        # y = (self._axisX.max() - self._axisX.min()) / self._axisX.tickCount() #
        self._cur_time += 1
        plus = self._axisX.max() + self._axisX.min()
        dif = self._axisX.max() - self._axisX.min()
        if self._cur_time > (plus/2 + dif/4):
            self.scroll(self.plotArea().width() / 2, 0)  # x轴移动param1，y轴移动param2
        self._series_id1.append(self._cur_time, self._y_id1) # 添加数据
        self._series_id2.append(self._cur_time, self._y_id2) # 添加数据
        self._series_id3.append(self._cur_time, self._y_id3) # 添加数据
        self._series_id4.append(self._cur_time, self._y_id4) # 添加数据
        self._series_id5.append(self._cur_time, self._y_id5) # 添加数据
        self._series_id6.append(self._cur_time, self._y_id6) # 添加数据


