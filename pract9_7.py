import sys
from PyQt5.QtCore import QSize, Qt
from PyQt5.QtGui import QPainter, QPen, QPainterPath, QImage
from PyQt5.QtWidgets import QFileDialog, QWidget, QPushButton, QVBoxLayout, QApplication


class Form(QWidget):
    def mousePressEvent(self, event):
        self.path.moveTo(event.pos())

    def mouseMoveEvent(self, event):
        self.path.lineTo(event.pos())
        Painter = QPainter(self.image)
        Painter.setPen(QPen(Qt.red, 5, Qt.SolidLine, Qt.RoundCap, Qt.RoundJoin))
        Painter.drawPath(self.path)
        Painter.end()
        self.update()

    def setPatch(self):
        self.e = QFileDialog.getOpenFileNames(self, "D:\\", "D:\\", "'(*.png)'")[0][0]
        self.loadImage()

    def loadImage(self):
        self.path = QPainterPath()
        self.image.load(str(self.e), "*.png")
        self.update()

    def sizeHint(self):
        return QSize(600, 600)

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.drawImage(event.rect(), self.image, self.rect())

    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self.setAttribute(Qt.WA_StaticContents)
        self.image = QImage(300, 300, QImage.Format_RGB32)
        self.path = QPainterPath()
        self.setPatch()

app = QApplication(sys.argv)
Widget = QWidget()
BtnSave = QPushButton("Save")
BtrClear = QPushButton("Clear")
BtnOpen = QPushButton("Open file")
drawer = Form()
BtnSave.clicked.connect(lambda: drawer.image.save(drawer.e, "PNG"))
BtrClear.clicked.connect(drawer.loadImage)
BtnOpen.clicked.connect(drawer.setPatch)
Widget.setLayout(QVBoxLayout())
Widget.layout().addWidget(BtnSave)
Widget.layout().addWidget(BtrClear)
Widget.layout().addWidget(BtnOpen)
Widget.layout().addWidget(drawer)
Widget.show()
sys.exit(app.exec_())
