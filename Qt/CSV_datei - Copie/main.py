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

        self.setWindowTitle("Students")

        self.ui.newentry.clicked.connect(self.addEntry)
        self.ui.save.clicked.connect(self.saveEntry)
        self.ui.erase.clicked.connect(self.erase_database)
        self.ui.actionSave.triggered.connect(self.saveEntry)
        self.ui.actionErase_Database.triggered.connect(self.erase_database)
        

    def addEntry(self):
        """
        This function creates a new line on the table.
        """
        Row = self.ui.tableWidget.rowCount()
        self.ui.tableWidget.insertRow(Row)

        self.ui.tableWidget.setItem(Row, 0, QtWidgets.QTableWidgetItem(""))
        self.ui.tableWidget.setItem(Row, 1, QtWidgets.QTableWidgetItem(""))
        self.ui.tableWidget.setItem(Row, 2, QtWidgets.QTableWidgetItem(""))

        #cell_1 = self.ui.tableWidget.item(Row, 0)
        #self.ui.tableWidget.editItem(cell_1)
        #print(cell_1)

    def saveEntry(self):
        """
        This function saves the entries which was given by the User
        and after the entries will be delete.
        """
        with open("CSV_datei - Copie\students.csv", "a", newline="", encoding="utf-8") as file:
            writer = csv.writer(file, delimiter=";")

            Row = self.ui.tableWidget.rowCount()
            for i in range(0, Row):
                rowContent = [
                    self.ui.tableWidget.item(i, 0).text(),
                    self.ui.tableWidget.item(i, 1).text(),
                    self.ui.tableWidget.item(i, 2).text(),
                ]
                writer.writerow(rowContent)
        #self.ui.tableWidget.rowCount(0)

    def erase_database(self):
        with open("CSV_datei - Copie\students.csv", "w", newline="", encoding="utf-8") as file:
            pass
        print(f"Der Inhalt der Database wurde gelöscht")


window = Main_Window()
window.show()
sys.exit(app.exec_())