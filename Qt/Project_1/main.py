import sys
import string
import random
import csv
from qtpy import QtWidgets
from PyQt5.QtWidgets import QMessageBox
from mainwindow import Ui_MainWindow

app = QtWidgets.QApplication(sys.argv)

class Main_Window(QtWidgets.QMainWindow):
    def __init__(self, parent = None):
        super().__init__(parent)

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.used_matriculation_numbers = set()

        self.setWindowTitle("Etudiants")

        self.ui.pushButton.clicked.connect(self.add_line)
        self.ui.pushButton_5.clicked.connect(self.remove_line)
        self.ui.pushButton_2.clicked.connect(self.generate_matricule)
        self.ui.pushButton_3.clicked.connect(self.save)
        self.ui.pushButton_4.clicked.connect(self.erase_database)

        self.generated_matricule = False

    def add_line(self):
        row = self.ui.tableWidget.rowCount()
        self.ui.tableWidget.insertRow(row)

    def remove_line(self):
        row = self.ui.tableWidget.rowCount()
        if row > 0:
            self.ui.tableWidget.removeRow(row - 1)

    def generate_matricule(self):
        row = self.ui.tableWidget.rowCount()

        if row == 0: # Verify if the table is empty.
            QMessageBox.warning(self, "Attention", "The Table is empty. Add lines in other to generate Matricules.")
            return

        letters = string.ascii_uppercase

        for i in range(row): # This part of Code allows to maintain existing matriculation numbers
            existing_matricule = self.ui.tableWidget.item(i, 0)
            if existing_matricule and existing_matricule.text(): # verifying if the item exists und if it already contains a matriculation number
                continue

            while True:
                matriculation_number = ''.join(random.choice(letters) for i in range(2)) +'-' +''.join(random.choice('0123456789') for i in range(5))
                # here we verify if the matriculation number has been already given to a Student. The given matriculation number are store in the database called 'used_matriculation_numbers'
                if matriculation_number not in self.used_matriculation_numbers:
                    self.used_matriculation_numbers.add(matriculation_number)
                    break
            self.ui.tableWidget.setItem(i, 0, QtWidgets.QTableWidgetItem(str(matriculation_number)))
        self.generated_matricule = True #Flag setzen, dass Matrikelnummern generiert wurden
        QMessageBox.information(self, "Success", "Matricules successfully generated.")

    def save(self):
        row = self.ui.tableWidget.rowCount()

        # In other to save there must be all Matriculation numbers and the table must be full
        if row == 0 : # Verify if the table is empty
            QMessageBox.information(self, "Attention", "You must fill the Table in other to save")
            return
        elif not self.generated_matricule: # Verify if there is all Matriculation numbers
            QMessageBox.information(self, "Attention", "First generate the Matricules")
            return


        with open("Project_1\students.csv", "a", newline="", encoding="utf-8") as file:
            writer = csv.writer(file, delimiter=";")

            row_count = self.ui.tableWidget.rowCount()
            column_count = self.ui.tableWidget.columnCount()

            # Functionality to write the headers of the table as headers in the database
            headers = [self.ui.tableWidget.horizontalHeaderItem(j).text() for j in range(column_count)]
            writer.writerow(headers) #write header line in the Database

            # Functionality to write the rest of the table in the Database
            for i in range(row_count):
                rowcontent = []
                for j in range(column_count):
                    item = self.ui.tableWidget.item(i, j)
                    if item is not None:
                        rowcontent.append(item.text())
                writer.writerow(rowcontent)
                    
            QMessageBox.information(self, "Success", "The Informations have been saved in the database.")
            self.ui.tableWidget.setRowCount(0)
            self.matricules_generated = False

    def erase_database(self):
        ans = QMessageBox.question(self, "Erase Database", "Do you really want to erase the database of this table ?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if ans == QMessageBox.Yes:
            with open("Project_1\students.csv", "w", newline="", encoding="utf-8") as file:
                pass
            QMessageBox.information(self, "Success", "The database of this table has been deleted")
        else:
            pass

window = Main_Window()
window.show()
sys.exit(app.exec_())