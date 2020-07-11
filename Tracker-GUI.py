from qtpy import QtWidgets, QtGui, QtCore
import sys, os, subprocess, datetime


class Label(QtWidgets.QLabel):
    def __init__(self, text):
        QtWidgets.QLabel.__init__(self)
        font = QtGui.QFont( "Arial", 16)
        self.setFont(font)
        self.setAlignment(QtCore.Qt.AlignTop)
        self.setMargin(30)
        self.setWordWrap(True)
        self.setStyleSheet("QLabel { background-color: #fff }")
        self.setText(text)
        #grip = QtWidgets.QSizeGrip(self)


class Window(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.width = 1280
        self.height = 720

        self.setup()

    def setup(self):
        """
        """

        self.grid = QtWidgets.QGridLayout()

        self.l_limits = Label("limits")
        self.l_buttons = Label("buttons")
        self.l_procs = Label("procs")
        self.l_stats = Label("stats")

        self.grid.addWidget(self.l_limits, 0, 0, 3, 1)
        self.grid.addWidget(self.l_buttons, 0, 1, 1, 1)
        self.grid.addWidget(self.l_procs, 1, 1, 1, 1)
        self.grid.addWidget(self.l_stats, 2, 1, 1, 1)

        self.grid.setSpacing(10)
        self.grid.setContentsMargins(10, 10, 10, 10)
        
        self.setLayout(self.grid)
        self.setStyleSheet("background-color: #0ff")
        self.resize(self.width, self.height)

        self.show()

            


def main():
    app = QtWidgets.QApplication(sys.argv)
    win = Window()
    app.exec_()

if __name__ == '__main__':
    main()