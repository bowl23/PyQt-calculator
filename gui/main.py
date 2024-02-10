from PyQt5.QtWidgets import QApplication, QWidget, QGridLayout, QPushButton, QLineEdit, QVBoxLayout, QSizePolicy
from PyQt5.QtGui import QFont

class Mywindow(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(400, 500)
        main_layout = QVBoxLayout()
        btns_layout = QGridLayout()
        btns = ['1', '2', '3', '+', '4', '5', '6', '-', '7', '8', '9', '*', '0', 'C', '.', '/']
        for i in range(len(btns)):
            btn = QPushButton(str(btns[i]))
            btns_layout.addWidget(btn, i // 4, i % 4)
        input_font=QFont()
        input_font.setPointSize(50)
        inputbox = QLineEdit()
        inputbox.setFont(input_font)
        inputbox.setFixedHeight(100)
        main_layout.addWidget(inputbox)
        main_layout.addLayout(btns_layout)
        self.setLayout(main_layout)



