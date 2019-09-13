
"""Setting up the first page of the application"""


class Ui_MainWindow(object):

#fucntion to open the main window

    def openWindow(self):
        self.window = QtWidgets.QMainWindow()
        global key
        key = self.textbox.text()
        self.ui = Ui_OtherWindow()
        self.ui.setupUi(self.window)
        MainWindow.hide()
        self.window.show()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 500)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.centralwidget.setStyleSheet("QWidget {background-color: rgba(0,41,59,255);} QScrollBar:horizontal {width: 1px; height: 1px;"
                           "background-color: rgba(0,41,59,255);} QScrollBar:vertical {width: 1px; height: 1px;"
                           "background-color: rgba(0,41,59,255);}")
        self.btn_open = QtWidgets.QPushButton(self.centralwidget)
        self.btn_open.setGeometry(QtCore.QRect(465, 235, 43, 43))
        self.btn_open.setObjectName("btn_open")

        self.btn_open.clicked.connect(self.openWindow)


        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(225, 20, 370, 41))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.label.setFont(font)
        self.label.setObjectName("label")

        self.label1 = QtWidgets.QLabel(self.centralwidget)
        self.label1.setGeometry(QtCore.QRect(250, 75, 370, 150))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label1.setFont(font)
        self.label1.setObjectName("label1")

        self.label2 = QtWidgets.QLabel(self.centralwidget)
        self.label2.setGeometry(QtCore.QRect(340, 390, 110, 45))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label2.setFont(font)
        self.label2.setObjectName("label2")

        self.label3 = QtWidgets.QLabel(self.centralwidget)
        self.label3.setGeometry(QtCore.QRect(320, 423, 200, 45))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.label3.setFont(font)
        self.label3.setObjectName("label3")

        self.textbox = QtWidgets.QLineEdit(self.centralwidget)
        self.textbox.setGeometry(QtCore.QRect(286, 235, 171, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.textbox.setFont(font)
        self.textbox.setStyleSheet(
            "QLineEdit { background: rgb(255, 255, 255); selection-background-color: rgb(233, 99, 0); }")

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("Get Your Weather", "Get Your Weather"))
        self.btn_open.setText(_translate("Current Weather", "🔍"))
        self.label.setText(_translate("Current Weather", "Get Your Weather App"))
        self.label1.setText(_translate("Current Weather", "♦Please, Subscribe Here\n                    ⇓\n    https://darksky.net/dev\n\n♦Insert Your Code:"))
        self.textbox.setPlaceholderText("Code...")
        self.label2.setText(_translate("Current Weather", "Powered by"))
        self.label3.setText(_translate("Current Weather","©Dark Sky"))

"""end of setting"""



"""main function that open the first page of the application"""

if __name__ == "__main__":


    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())


