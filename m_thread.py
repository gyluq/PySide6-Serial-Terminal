import time

from PySide6.QtCore import QThread, Signal
from PySide6.QtSerialPort import QSerialPortInfo


class Thread_detect_port(QThread):
    _signal = Signal()

    def __init__(self):
        super().__init__()
        self.port_num = 0

    def run(self):
        while True:
            # 端口数量发送变化时才发送信号
            num = len(QSerialPortInfo.availablePorts())
            if num != self.port_num:
                self._signal.emit()
                self.port_num = num
            time.sleep(2)  # 休眠
