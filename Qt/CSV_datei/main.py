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
    
        with open(r'C:\Users\amour\Desktop\Python\Qt\CSV_datei\students.csv', newline='', encoding="utf-8") as csvfile:
            namereader = csv.reader(csvfile, delimiter=';', quotechar='"')
            for row in namereader:
                self.ui.tableWidget.insertRow(Row)
                self.ui.tableWidget.setItem(Row, 0, QtWidgets.QTableWidgetItem(str(row[0])))
                self.ui.tableWidget.setItem(Row, 1, QtWidgets.QTableWidgetItem(str(row[1])))
                self.ui.tableWidget.setItem(Row, 2, QtWidgets.QTableWidgetItem(str(row[2])))


window = Main_Window()
window.show()
sys.exit(app.exec_())