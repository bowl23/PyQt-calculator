# from PyQt5.QtCore import
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QGridLayout, QPushButton, QTextEdit


class Mywindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        layout = QGridLayout()
        editline = QTextEdit()
        btns = ['1', '2', '3','+', '4', '5', '6','-', '7', '8', '9','*','0','C','.','/']
        for i in range(len(btns)):
            btn = QPushButton(str(btns[i]))
            layout.addWidget(btn, i // 4, i % 4)
        self.setLayout(layout)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = Mywindow()
    w.show()
    app.exec()
