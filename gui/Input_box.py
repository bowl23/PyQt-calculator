from PyQt5.QtWidgets import QWidget,QLineEdit
from PyQt5.QtGui import QFont
class Input_box(QLineEdit):
    def __init__(self):
        super().__init__()
        font = QFont()
        font.setPointSize(50)
        # input_box = QLineEdit()
        self.setFont(font)
        self.setFixedHeight(100)
