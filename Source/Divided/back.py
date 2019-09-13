"""setting up the page for error handling for wrong cities"""


class Ui_OtherWindow_back(object):

    def __init__(self,location):
        self.location = location

#search function to turn back

    def on_search(self):
        location = self.location
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_OtherWindow_search(location)
        self.ui.setupUi(self.window)
        self.Otherwindow.hide()
        self.window.show()


    def setupUi(self, OtherWindow):
        self.Otherwindow = OtherWindow
        OtherWindow.setObjectName("OtherWindow")
        OtherWindow.resize(800, 500)
        self.centralwidget = QtWidgets.QWidget(OtherWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.centralwidget.setStyleSheet(
            "QWidget {background-color: rgba(0,41,59,255);} QScrollBar:horizontal {width: 1px; height: 1px;"
            "background-color: rgba(0,41,59,255);} QScrollBar:vertical {width: 1px; height: 1px;"
            "background-color: rgba(0,41,59,255);}")

        self.label.setGeometry(QtCore.QRect(190,70, 450, 130))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.label.setFont(font)
        self.label.setObjectName("label")


        self.btn_open1 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_open1.setGeometry(QtCore.QRect(340, 195, 141, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.btn_open1.setFont(font)
        self.btn_open1.setObjectName("btn_open1")
        self.btn_open1.clicked.connect(self.on_search)

        OtherWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(OtherWindow)

        self.statusbar.setObjectName("statusbar")
        OtherWindow.setStatusBar(self.statusbar)

        self.retranslateUi(OtherWindow)
        QtCore.QMetaObject.connectSlotsByName(OtherWindow)

    def retranslateUi(self, OtherWindow):
        _translate = QtCore.QCoreApplication.translate
        OtherWindow.setWindowTitle(_translate("OtherWindow", "Error"))
        self.label.setText(_translate("OtherWindow","OPS...We cannot find your city."))
        self.btn_open1.setText(_translate("OtherWindow", "Back"))

"""end of setting"""
