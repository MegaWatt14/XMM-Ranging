# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'XMM.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(529, 123)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.Calculate = QtGui.QPushButton(self.centralwidget)
        self.Calculate.setGeometry(QtCore.QRect(430, 20, 75, 23))
        self.Calculate.setObjectName(_fromUtf8("Calculate"))
        self.Clear = QtGui.QPushButton(self.centralwidget)
        self.Clear.setGeometry(QtCore.QRect(430, 50, 75, 23))
        self.Clear.setObjectName(_fromUtf8("Clear"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 20, 111, 21))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(230, 20, 111, 21))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(60, 50, 81, 21))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_4 = QtGui.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(230, 50, 101, 21))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.Hourly = QtGui.QLineEdit(self.centralwidget)
        self.Hourly.setGeometry(QtCore.QRect(150, 50, 51, 20))
        self.Hourly.setObjectName(_fromUtf8("Hourly"))
        self.Seconds = QtGui.QLineEdit(self.centralwidget)
        self.Seconds.setGeometry(QtCore.QRect(340, 50, 71, 20))
        self.Seconds.setObjectName(_fromUtf8("Seconds"))
        self.StartTime = QtGui.QDoubleSpinBox(self.centralwidget)
        self.StartTime.setGeometry(QtCore.QRect(150, 20, 62, 22))
        self.StartTime.setObjectName(_fromUtf8("StartTime"))
        self.StartTime.setDecimals(2)
        self.EndTime = QtGui.QDoubleSpinBox(self.centralwidget)
        self.EndTime.setGeometry(QtCore.QRect(340, 20, 62, 22))
        self.EndTime.setObjectName(_fromUtf8("EndTime"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 529, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "XMM RANGING", None))
        self.Calculate.setText(_translate("MainWindow", "CALCULATE", None))
        self.Clear.setText(_translate("MainWindow", "CLEAR", None))
        self.label.setText(_translate("MainWindow", "RANGING START TIME", None))
        self.label_2.setText(_translate("MainWindow", "RANGING END TIME", None))
        self.label_3.setText(_translate("MainWindow", "HOURLY RNGS:", None))
        self.label_4.setText(_translate("MainWindow", "CONTINUOUS SECS.", None))

        self.StartTime.valueChanged.connect(self.rng_start)
        self.Calculate.clicked.connect(self.button_state)
        self.Clear.clicked.connect(self.clear_it)

    def rng_start(self):
        hrs = (int(self.StartTime.value()))
        mins = (str(self.StartTime.value())[3] + str(self.StartTime.value())[4])
        mins = eval(mins)
        print (hrs)
        print(mins)


    def button_state(self):
        if self.Calculate.clicked:
            self.Hourly.setText("32")

    def clear_it(self):
        if self.Clear.clicked:
            self.Hourly.setText("")

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

