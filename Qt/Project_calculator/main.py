import sys
from qtpy import QtWidgets
from PyQt5.QtWidgets import QMessageBox
from mainwindow import Ui_MainWindow

app = QtWidgets.QApplication(sys.argv)

class Main_Window(QtWidgets.QMainWindow):
    def __init__(self, parent = None):
        super().__init__(parent)

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle("Calculatrice")

        # numeric buttons
        self.ui.pushButton_9.clicked.connect(self.one)
        self.ui.pushButton_10.clicked.connect(self.two)
        self.ui.pushButton_11.clicked.connect(self.three)
        self.ui.pushButton_5.clicked.connect(self.four)
        self.ui.pushButton_6.clicked.connect(self.five)
        self.ui.pushButton_7.clicked.connect(self.six)
        self.ui.pushButton.clicked.connect(self.seven)
        self.ui.pushButton_2.clicked.connect(self.eight)
        self.ui.pushButton_3.clicked.connect(self.nine)
        self.ui.pushButton_14.clicked.connect(self.zero)

        #operation buttons
        self.ui.pushButton_12.clicked.connect(self.add)
        self.ui.pushButton_15.clicked.connect(self.sub)
        self.ui.pushButton_4.clicked.connect(self.mul)
        self.ui.pushButton_8.clicked.connect(self.div)
        self.ui.pushButton_16.clicked.connect(self.egal)
        self.ui.pushButton_13.clicked.connect(self.delete)

        self.ui.actionQuit.triggered.connect(self.Quit)
 
    def one(self):
        txt = self.ui.lineEdit.text()
        self.ui.lineEdit.setText(txt + "1")
    
    def two(self):
        txt = self.ui.lineEdit.text()
        self.ui.lineEdit.setText(txt + "2")

    def three(self):
        txt = self.ui.lineEdit.text()
        self.ui.lineEdit.setText(txt + "3")

    def four(self):
        txt = self.ui.lineEdit.text()
        self.ui.lineEdit.setText(txt + "4")

    def five(self):
        txt = self.ui.lineEdit.text()
        self.ui.lineEdit.setText(txt + "5")

    def six(self):
        txt = self.ui.lineEdit.text()
        self.ui.lineEdit.setText(txt + "6")

    def seven(self):
        txt = self.ui.lineEdit.text()
        self.ui.lineEdit.setText(txt + "7")

    def eight(self):
        txt = self.ui.lineEdit.text()
        self.ui.lineEdit.setText(txt + "8")

    def nine(self):
        txt = self.ui.lineEdit.text()
        self.ui.lineEdit.setText(txt + "9")

    def zero(self):
        txt = self.ui.lineEdit.text()
        self.ui.lineEdit.setText(txt + "0")

    def add(self):
        txt = self.ui.lineEdit.text()
        self.ui.lineEdit.setText(txt + " + ")

    def sub(self):
        txt = self.ui.lineEdit.text()
        self.ui.lineEdit.setText(txt + " - ")

    def mul(self):
        txt = self.ui.lineEdit.text()
        self.ui.lineEdit.setText(txt + " x ")

    def div(self):
        txt = self.ui.lineEdit.text()
        self.ui.lineEdit.setText(txt + " / ")

    def egal(self):
        operation = self.ui.lineEdit.text()
        if not operation:
            self.ui.lineEdit.setText("0")
        else:
            ans  = eval(operation)
            self.ui.lineEdit.setText(str(ans))

    def delete(self):
        txt = self.ui.lineEdit.text()
        self.ui.lineEdit.setText(txt[:len(txt)-1])

    def Quit(self):
        rep = QMessageBox.question(self, "Quit", "Do you really want to quit the calculator ?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if rep == QMessageBox.Yes:
            QtWidgets.QWidget.close(self)
        else:
            pass

window = Main_Window()
window.show()
sys.exit(app.exec_())
