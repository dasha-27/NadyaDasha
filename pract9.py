import sys
from enum import Enum

from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication


class Operation(Enum):
    plus = 1
    minus = 2
    mul = 3
    div = 4
    power = 5

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
        self.calculation(Operation.plus)

    def minus(self):
        self.calculation(Operation.minus)

    def mul(self):
        self.calculation(Operation.mul)

    def div(self):
        self.calculation(Operation.div)

    def power(self):
        self.calculation(Operation.power)

    def calculation(self, operation):
        try:
            a1 = float(self.txtArgument1.toPlainText())
            a2 = float(self.txtArgument2.toPlainText())
            if operation == Operation.plus:
                self.txtResult.setText(str(a1 + a2))
            if operation == Operation.minus:
                self.txtResult.setText(str(a1 - a2))
            if operation == Operation.mul:
                self.txtResult.setText(str(a1 * a2))
            if operation == Operation.div:
                self.txtResult.setText(str(a1 / a2))
            if operation == Operation.power:
                self.txtResult.setText(str(a1 ** a2))
        except:
            self.txtResult.setText('Неправильные данные')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = MainWindow()
    sys.exit(app.exec_())