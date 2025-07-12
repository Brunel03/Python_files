import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QFileDialog, QMessageBox # Importiere QFileDialog und QMessageBox
from mainwindow import Ui_MainWindow
import csv

class Main_Window(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle("CSV Tabellenanzeige") # Aussagekräftigerer Fenstertitel

        self.ui.pushButton.clicked.connect(self.onPushButton)

    def onPushButton(self):
        """
        Wird aufgerufen, wenn der Button geklickt wird.
        Öffnet einen Dateiauswahl-Dialog, liest eine CSV-Datei
        und zeigt die Daten in der Tabelle an.
        """
        # Dateiauswahl-Dialog öffnen
        file_dialog = QFileDialog()
        file_path, _ = file_dialog.getOpenFileName(self, "CSV-Datei öffnen", "", "CSV Dateien (*.csv)")

        if file_path: # Überprüfen, ob ein Dateipfad ausgewählt wurde
            try:
                with open(file_path, 'r', newline='', encoding="utf-8") as csvfile:
                    csv_reader = csv.reader(csvfile, delimiter=';', quotechar='"')

                    self.ui.tableWidget.setRowCount(0) # Tabelle leeren

                    header = next(csv_reader) # Erste Zeile als Header lesen
                    if header:
                        self.ui.tableWidget.setColumnCount(len(header))
                        self.ui.tableWidget.setHorizontalHeaderLabels(header)

                    for row_index, row in enumerate(csv_reader): # row_index für Zeilennummerierung
                        self.ui.tableWidget.insertRow(row_index)
                        for col_index, cell_data in enumerate(row):
                            item = QtWidgets.QTableWidgetItem(str(cell_data))
                            self.ui.tableWidget.setItem(row_index, col_index, item)

            except FileNotFoundError:
                QMessageBox.critical(self, "Fehler", "CSV-Datei nicht gefunden.")
            except Exception as e: # Allgemeine Fehlerbehandlung
                QMessageBox.critical(self, "Fehler", f"Fehler beim Lesen der CSV-Datei: {e}")


if __name__ == "__main__": # Standard für Python-Skripte, die direkt ausgeführt werden
    app = QtWidgets.QApplication(sys.argv)
    window = Main_Window()
    window.show()
    sys.exit(app.exec_())