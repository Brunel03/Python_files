import sys
from qtpy import QtWidgets
from mainwindow import Ui_MainWindow

app = QtWidgets.QApplication(sys.argv)

class Main_Window(QtWidgets.QMainWindow):
    def __init__(self, parent = None):
        super().__init__(parent)

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.setWindowTitle("Table")

        self.ui.changeinfo.clicked.connect(self.onButtonClick)
        self.ui.addline.clicked.connect(self.add_line)
        self.ui.addcolumn.clicked.connect(self.add_column)

    def onButtonClick(self):
        row = self.ui.tableWidget.rowCount()
        self.ui.tableWidget.insertRow(row)
        self.ui.tableWidget.setItem(row, 0, QtWidgets.QTableWidgetItem("0061784410"))
        self.ui.tableWidget.setItem(row, 4, QtWidgets.QTableWidgetItem("Bagangte"))

    def add_line(self):
        self.ui.tableWidget.insertRow(self.ui.tableWidget.rowCount())

    def add_column(self):
        self.ui.tableWidget.insertColumn(self.ui.tableWidget.columnCount())


window = Main_Window()
window.show()
sys.exit(app.exec_())