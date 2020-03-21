import random
import sys
from PyQt5 import QtCore, QtWidgets, QtGui
from files.gui import Ui_tombola

class Tombola(QtWidgets.QMainWindow, Ui_tombola):

    def __init__(self) -> None:
        QtWidgets.QMainWindow.__init__(self)
        self.setupUi(self)

        self.lne_num.setValidator(QtGui.QIntValidator())
        self.lbl_num.setText('0')

        self.num = 0
        self.count = QtCore.QTimer()

        self.pb_start.clicked.connect(self.start)
        self.lne_num.returnPressed.connect(self.start)
        self.count.timeout.connect(self.add_count)

    def start(self) -> None:
        if not self.count.isActive():
            self.num = 0
            self.count.start(1)

        QtCore.QTimer.singleShot(random.randint(1000, 5001), lambda: self.stop())

    def add_count(self) -> None:
        self.num += 1

        if self.num > int(self.lne_num.text()):
            self.num = 0

        self.lbl_num.setText( str(self.num) )

    def stop(self) -> None:
        self.count.stop()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    app.setStyle(u"Fusion")
    tom = Tombola()
    tom.show()
    sys.exit(app.exec_())