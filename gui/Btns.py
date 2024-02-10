from PyQt5.QtWidgets import QPushButton, QGridLayout
from PyQt5.QtGui import QFont


class Btns_layout(QGridLayout):

    def __init__(self, input_box):
        super().__init__()

        numberBtns = ['1', '2', '3', '+', '4', '5', '6', '-', '7', '8', '9', '*', '0', '.', '/']
        for i in range(len(numberBtns)):
            btn = NumberBtn(numberBtns[i], input_box)

            # 这里的布局写的太好了，哈哈哈哈哈
            self.addWidget(btn, i // 4, i % 4)
        clearBtn=ClearBtn('C',input_box)
        self.addWidget(clearBtn)
        eqBtn=EqBtn('=',input_box)
        self.addWidget(eqBtn)
        removeBtn=RemoveBtn('<-',input_box)
        self.addWidget(removeBtn)

class Btn(QPushButton):
    Text = ''

    def __init__(self, value, input_box):
        super().__init__(str(value))
        font = QFont()
        font.setPointSize(20)
        self.setFont(font)
        self.value = value
        self.input_box = input_box


class NumberBtn(Btn):
    def __init__(self, value, input_box):
        super().__init__(value, input_box)
        self.clicked.connect(self.changeText)

    def changeText(self):
        Btn.Text += self.value
        self.input_box.setText(Btn.Text)
        print(Btn.Text)


class ClearBtn(Btn):
    def __init__(self, value, input_box):
        super().__init__(value, input_box)
        self.clicked.connect(self.clearText)

    def clearText(self):
        Btn.Text = ''
        self.input_box.setText(Btn.Text)
        print(Btn.Text)
class EqBtn(Btn):
    def __init__(self,value,input_box):
        super().__init__(value,input_box)
        self.clicked.connect(self.getResult)
    def getResult(self):
        Btn.Text=str(eval(Btn.Text))
        self.input_box.setText(Btn.Text)
        print(Btn.Text)
class RemoveBtn(Btn):
    def __init__(self,value,input_box):
        super().__init__(value,input_box)
        self.clicked.connect(self.remove)
    def remove(self):
        if Btn.Text!='':
            Btn.Text=Btn.Text[:-1]
        self.input_box.setText(Btn.Text)
        print(Btn.Text)
