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
        self.calculation('plus', self.textEdit1.toPlainText(), self.textEdit2.toPlainText())

    def minus(self):
        self.calculation('minus', self.textEdit1.toPlainText(), self.textEdit2.toPlainText())

    def mul(self):
        self.calculation('mul', self.textEdit1.toPlainText(), self.textEdit2.toPlainText())

    def div(self):
        self.calculation('div', self.textEdit1.toPlainText(), self.textEdit2.toPlainText())

    def power(self):
        self.calculation('power', self.textEdit1.toPlainText(), self.textEdit2.toPlainText())

    def calculation(self, operation, arg1, arg2):
        try:
            a1 = float(arg1)
            a2 = float(arg2)
            if operation == 'plus':
                self.textEdit3.setText(str(a1 + a2))
            if operation == 'minus':
                self.textEdit3.setText(str(a1 - a2))
            if operation == 'mul':
                self.textEdit3.setText(str(a1 * a2))
            if operation == 'div':
                self.textEdit3.setText(str(a1 / a2))
            if operation == 'power':
                self.textEdit3.setText(str(a1 ** a2))
        except:
            self.textEdit3.setText('Неправильные данные')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = MainWindow()
    sys.exit(app.exec_())