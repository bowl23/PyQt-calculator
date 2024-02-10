from PyQt5.QtWidgets import QApplication, QWidget, QGridLayout, QPushButton, QLineEdit, QVBoxLayout, QSizePolicy
from PyQt5.QtGui import QFont
from .Input_box import Input_box
from .Btns import Btns_layout

class Mywindow(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(400, 500)
        self.setWindowTitle("bowl's calculator")
        main_layout = QVBoxLayout()
        inputbox = Input_box()
        btns_layout=Btns_layout(inputbox)
        main_layout.addWidget(inputbox)
        main_layout.addLayout(btns_layout)
        self.setLayout(main_layout)



