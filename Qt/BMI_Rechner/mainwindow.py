# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '../BMI_Rechner\mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(646, 389)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.formLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.formLayoutWidget.setGeometry(QtCore.QRect(140, 40, 241, 161))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label.setFont(font)
        #self.label.setTextFormat(QtCore.Qt.Qt::TextFormat::AutoText)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.label_2 = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_2.setFont(font)
        #self.label_2.setTextFormat(QtCore.Qt.Qt::TextFormat::AutoText)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.height = QtWidgets.QDoubleSpinBox(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.height.setFont(font)
        self.height.setMaximum(2.5)
        self.height.setSingleStep(0.01)
        self.height.setObjectName("height")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.height)
        self.weight = QtWidgets.QDoubleSpinBox(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.weight.setFont(font)
        self.weight.setObjectName("weight")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.weight)
        self.calc = QtWidgets.QPushButton(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.calc.setFont(font)
        self.calc.setObjectName("calc")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.calc)
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(180, 220, 153, 21))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_3 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_3.setEnabled(True)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(13)
        font.setKerning(False)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)
        self.label_4 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_4.setEnabled(True)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setKerning(False)
        self.label_4.setFont(font)
        self.label_4.setAutoFillBackground(False)
        #self.label_4.setInputMethodHints(QtCore.Qt.Qt::InputMethodHint::ImhNone)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout.addWidget(self.label_4)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 646, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.calc.clicked.connect(self.label_3.show) # type: ignore
        self.calc.clicked.connect(self.label_4.show) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Height (in m): "))
        self.label_2.setText(_translate("MainWindow", "Weight (in Kg): "))
        self.calc.setText(_translate("MainWindow", "Calculate BMI"))
        self.label_3.setText(_translate("MainWindow", "Your BMI : "))
        self.label_4.setText(_translate("MainWindow", "TextLabel"))
