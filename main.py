# Copyright (C) 2022 The Qt Company Ltd.
# SPDX-License-Identifier: LicenseRef-Qt-Commercial OR BSD-3-Clause
# -*- coding: utf-8 -*-
import sys

from PySide6.QtWidgets import QApplication

from mainwindow import MainWindow


if __name__ == "__main__":
    a = QApplication(sys.argv)
    w = MainWindow()
    w.show()
    sys.exit(a.exec())

