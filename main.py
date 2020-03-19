from design import Ui_Form as Design
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtCore import QTimer
from PyQt5.QtGui import QCursor
import sys
from random import randint


class App(QWidget, Design):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.timer = QTimer()
        self.timer.timeout.connect(self.check)
        self.timer.start(1)

    def check(self):
        if QCursor.pos().x() - 584 in range(self.pushButton.pos().x() - 20, self.pushButton.pos().x() + 20) or \
                QCursor.pos().y() - 264 in range(self.pushButton.pos().y() - 20, self.pushButton.pos().y() + 20):
            count = 0
            while count == 0:
                x = randint(15, 765)
                y = randint(15, 525)
                if QCursor.pos().x() - 584 in range(x - 20, x + 20) or QCursor.pos().y() - 264 in range(y - 20, y + 20):
                    pass
                else:
                    self.pushButton.move(x, y)
                    count += 1


app = QApplication(sys.argv)
ex = App()
ex.show()
sys.exit(app.exec_())