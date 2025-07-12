import sys
from qtpy import QtWidgets
from mainwindow import Ui_MainWindow

app = QtWidgets.QApplication(sys.argv)

class Main_Window(QtWidgets.QMainWindow):
    def __init__(self, parent = None):
        super().__init__(parent)

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.setWindowTitle("BMI Rechner")

        self.ui.label_3.hide()
        self.ui.label_4.hide()
        self.ui.calc.clicked.connect(self.calculate_BMI)


    def calculate_BMI(self):
        height = self.ui.height.value()
        weight = self.ui.weight.value()

        if height <= 0:
            self.ui.label_4.setText(" Error ")
        else:
            bmi = weight / (height) ** 2
            bmi = round(bmi, 2)
            self.ui.label_4.setText(str(bmi))
        

window = Main_Window()
window.show()
sys.exit(app.exec_())