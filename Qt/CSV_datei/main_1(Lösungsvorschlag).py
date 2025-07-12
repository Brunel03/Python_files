import sys
from qtpy import QtWidgets
from mainwindow import Ui_MainWindow
import csv

app = QtWidgets.QApplication(sys.argv)

class Main_Window(QtWidgets.QMainWindow):
    def __init__(self, parent = None):
        super().__init__(parent)

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.setWindowTitle("Table")

        self.ui.pushButton.clicked.connect(self.onPushButton)
        

    def onPushButton(self):
        Row = self.ui.tableWidget.rowCount()
        

window = Main_Window()
window.show()
sys.exit(app.exec_())