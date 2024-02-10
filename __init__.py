import sys
from PyQt5.QtWidgets import QApplication
from gui.main import Mywindow
def main():
    app=QApplication(sys.argv)
    window=Mywindow()
    window.show()
    app.exec()
if __name__=='__main__':
    main()
