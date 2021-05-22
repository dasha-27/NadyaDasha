import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('calculator.ui', self)
        self.initUI()
        self.plus_Button.clicked.connect(self.plus)
        self.minus_Button.clicked.connect(self.minus)
        self.mul_Button.clicked.connect(self.mul)
        self.div_Button.clicked.connect(self.div)
        self.power_Button.clicked.connect(self.power)

    def initUI(self):
        self.setWindowTitle('Калькулятор')
        self.show()

    def plus(self):
        try:
            arg1 = float(self.textEdit1.toPlainText())
            arg2 = float(self.textEdit2.toPlainText())
            result = arg1 + arg2
            self.textEdit3.setText(str(result))
        except Exception:
            self.textEdit3.setText('Неправильные данные')

    def minus(self):
        try:
            arg1 = float(self.textEdit1.toPlainText())
            arg2 = float(self.textEdit2.toPlainText())
            result = arg1 - arg2
            self.textEdit3.setText(str(result))
        except Exception:
            self.textEdit3.setText('Неправильные данные')

    def mul(self):
        try:
            arg1 = float(self.textEdit1.toPlainText())
            arg2 = float(self.textEdit2.toPlainText())
            result = arg1 * arg2
            self.textEdit3.setText(str(result))
        except Exception:
            self.textEdit3.setText('Неправильные данные')

    def div(self):
        try:
            arg1 = float(self.textEdit1.toPlainText())
            arg2 = float(self.textEdit2.toPlainText())
            result = arg1 / arg2
            self.textEdit3.setText(str(result))
        except Exception:
            self.textEdit3.setText('Неправильные данные')

    def power(self):
        try:
            arg1 = float(self.textEdit1.toPlainText())
            arg2 = float(self.textEdit2.toPlainText())
            result = arg1 ** arg2
            self.textEdit3.setText(str(result))
        except Exception:
            self.textEdit3.setText('Неправильные данные')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = MainWindow()
    sys.exit(app.exec_())