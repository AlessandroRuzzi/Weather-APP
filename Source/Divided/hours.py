"""settin up the page for next hours function"""


class Ui_OtherWindow_hours(object):

    def __init__(self,name,forecast,location):
        self.curr_loc = name
        self.curr_loc_forecast = forecast
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

        self.label.setGeometry(QtCore.QRect(2,43, 400, 27))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label.setFont(font)
        self.label.setObjectName("label")


        self.label1 = QtWidgets.QLabel(self.centralwidget)
        self.label1.setGeometry(QtCore.QRect(2, 0, 400, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label1.setFont(font)
        self.label1.setObjectName("label1")

        self.label3 = QtWidgets.QLabel(self.centralwidget)
        self.label3.setGeometry(QtCore.QRect(45, 346, 30, 30))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.label3.setFont(font)
        self.label3.setObjectName("label3")

        self.label4 = QtWidgets.QLabel(self.centralwidget)
        self.label4.setGeometry(QtCore.QRect(155, 346, 30, 30))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.label4.setFont(font)
        self.label4.setObjectName("label4")

        self.label5 = QtWidgets.QLabel(self.centralwidget)
        self.label5.setGeometry(QtCore.QRect(265, 346, 30, 30))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.label5.setFont(font)
        self.label5.setObjectName("label5")

        self.label6 = QtWidgets.QLabel(self.centralwidget)
        self.label6.setGeometry(QtCore.QRect(375, 346, 30, 30))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.label6.setFont(font)
        self.label6.setObjectName("label6")

        self.label7 = QtWidgets.QLabel(self.centralwidget)
        self.label7.setGeometry(QtCore.QRect(485, 346, 30, 30))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.label7.setFont(font)
        self.label7.setObjectName("label7")

        self.label8 = QtWidgets.QLabel(self.centralwidget)
        self.label8.setGeometry(QtCore.QRect(595, 346, 30, 30))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.label8.setFont(font)
        self.label8.setObjectName("label8")

        self.label9 = QtWidgets.QLabel(self.centralwidget)
        self.label9.setGeometry(QtCore.QRect(705, 346, 30, 30))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.label9.setFont(font)
        self.label9.setObjectName("label9")

        self.label10 = QtWidgets.QLabel(self.centralwidget)
        self.label10.setGeometry(QtCore.QRect(10, 377, 100, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label10.setFont(font)
        self.label10.setObjectName("label10")

        self.label11 = QtWidgets.QLabel(self.centralwidget)
        self.label11.setGeometry(QtCore.QRect(120, 377, 100, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label11.setFont(font)
        self.label11.setObjectName("label11")

        self.label12 = QtWidgets.QLabel(self.centralwidget)
        self.label12.setGeometry(QtCore.QRect(230, 377, 100, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label12.setFont(font)
        self.label12.setObjectName("label12")

        self.label13 = QtWidgets.QLabel(self.centralwidget)
        self.label13.setGeometry(QtCore.QRect(340, 377, 100, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label13.setFont(font)
        self.label13.setObjectName("label13")

        self.label14 = QtWidgets.QLabel(self.centralwidget)
        self.label14.setGeometry(QtCore.QRect(450, 377, 100, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label14.setFont(font)
        self.label14.setObjectName("label14")

        self.label15 = QtWidgets.QLabel(self.centralwidget)
        self.label15.setGeometry(QtCore.QRect(560, 377, 100, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label15.setFont(font)
        self.label15.setObjectName("label15")

        self.label16 = QtWidgets.QLabel(self.centralwidget)
        self.label16.setGeometry(QtCore.QRect(670, 377, 100, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label16.setFont(font)
        self.label16.setObjectName("label16")

        self.label17 = QtWidgets.QLabel(self.centralwidget)
        self.label17.setGeometry(QtCore.QRect(0, 75, 300, 150))
        """font = QtGui.QFont()
        font.setPointSize(30)
        self.label17.setFont(font)"""
        self.label17.setStyleSheet("font: 90pt Arial Black")
        self.label17.setObjectName("label17")


        self.label2 = QtWidgets.QLabel(self.centralwidget)
        self.label2.setGeometry(QtCore.QRect(300, 70, 250, 190))
        pixmap = QtGui.QPixmap(str(self.curr_loc_forecast['hourly']['icon']) + '.jpg')
        self.label2.setPixmap(pixmap)


        self.btn_open = QtWidgets.QPushButton(self.centralwidget)
        self.btn_open.setGeometry(QtCore.QRect(10, 431, 40, 40))
        self.btn_open.setObjectName("btn_open")
        font = QtGui.QFont()
        font.setPointSize(26)
        self.btn_open.setFont(font)
        self.btn_open.clicked.connect(self.on_search)

        self.btn_open1 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_open1.setGeometry(QtCore.QRect(10, 290, 100, 51))
        self.btn_open1.setObjectName("btn_open1")

        self.btn_open2 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_open2.setGeometry(QtCore.QRect(120, 290, 100, 51))
        self.btn_open2.setObjectName("btn_open2")

        self.btn_open3 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_open3.setGeometry(QtCore.QRect(230, 290, 100, 51))
        self.btn_open3.setObjectName("btn_open3")

        self.btn_open4 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_open4.setGeometry(QtCore.QRect(340, 290, 100, 51))
        self.btn_open4.setObjectName("btn_open4")

        self.btn_open5 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_open5.setGeometry(QtCore.QRect(450, 290, 100, 51))
        self.btn_open5.setObjectName("btn_open5")

        self.btn_open6 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_open6.setGeometry(QtCore.QRect(560, 290, 100, 51))
        self.btn_open6.setObjectName("btn_open6")

        self.btn_open7 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_open7.setGeometry(QtCore.QRect(670, 290, 100, 51))
        self.btn_open7.setObjectName("btn_open7")

        OtherWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(OtherWindow)

        self.statusbar.setObjectName("statusbar")
        OtherWindow.setStatusBar(self.statusbar)

        self.retranslateUi(OtherWindow)
        QtCore.QMetaObject.connectSlotsByName(OtherWindow)

    def retranslateUi(self, OtherWindow):
        _translate = QtCore.QCoreApplication.translate
        OtherWindow.setWindowTitle(_translate("OtherWindow", "Next Hours"))
        d=get_dict_of_week()

#find the day of the week

        today = str(datetime.today().strftime('%A'))

        for day in d:
            if (day == today) :
                today = d[day]
                break

        self.label1.setText(_translate("OtherWindow",self.curr_loc[0]['name'] + "-> " + today))

        self.label3.setText(_translate("OtherWindow", "⇓"))
        self.label4.setText(_translate("OtherWindow", "⇓"))
        self.label5.setText(_translate("OtherWindow", "⇓"))
        self.label6.setText(_translate("OtherWindow", "⇓"))
        self.label7.setText(_translate("OtherWindow", "⇓"))
        self.label8.setText(_translate("OtherWindow", "⇓"))
        self.label9.setText(_translate("OtherWindow", "⇓"))

        conta = 0

        self.label10.setText(_translate("OtherWindow", "Temp-> " + str(int(int(((self.curr_loc_forecast['hourly']['data'][conta]['temperature']) -32) *5)/9 )) + "°C" +
                                        "\nPrec-> " + str((int(self.curr_loc_forecast['hourly']['data'][conta]['precipProbability'] *100))) + "%" ))
        conta +=3
        self.label11.setText(_translate("OtherWindow", "Temp-> " + str(int(int(((self.curr_loc_forecast['hourly']['data'][conta]['temperature']) - 32) * 5) / 9)) + "°C" +
                                        "\nPrec-> " + str((int(self.curr_loc_forecast['hourly']['data'][conta]['precipProbability'] * 100))) + "%"))
        conta += 3
        self.label12.setText(_translate("OtherWindow", "Temp-> " + str(int(int(((self.curr_loc_forecast['hourly']['data'][conta]['temperature']) - 32) * 5) / 9)) + "°C" +
                                        "\nPrec-> " + str((int(self.curr_loc_forecast['hourly']['data'][conta]['precipProbability'] * 100))) + "%"))
        conta += 3
        self.label13.setText(_translate("OtherWindow", "Temp-> " + str(int(int(((self.curr_loc_forecast['hourly']['data'][conta]['temperature']) - 32) * 5) / 9)) + "°C" +
                                        "\nPrec-> " + str((int(self.curr_loc_forecast['hourly']['data'][conta]['precipProbability'] * 100))) + "%"))
        conta += 3
        self.label14.setText(_translate("OtherWindow", "Temp-> " + str(int(int(((self.curr_loc_forecast['hourly']['data'][conta]['temperature']) - 32) * 5) / 9)) + "°C" +
                                        "\nPrec-> " + str((int(self.curr_loc_forecast['hourly']['data'][conta]['precipProbability'] * 100))) + "%"))
        conta += 3
        self.label15.setText(_translate("OtherWindow", "Temp-> " + str(int(int(((self.curr_loc_forecast['hourly']['data'][conta]['temperature']) - 32) * 5) / 9)) + "°C" +
                                        "\nPrec-> " + str((int(self.curr_loc_forecast['hourly']['data'][conta]['precipProbability'] * 100))) + "%"))
        conta += 3
        self.label16.setText(_translate("OtherWindow", "Temp-> " + str(int(int(((self.curr_loc_forecast['hourly']['data'][conta]['temperature']) - 32) * 5) / 9)) + "°C" +
                                        "\nPrec-> " + str((int(self.curr_loc_forecast['hourly']['data'][conta]['precipProbability'] * 100))) + "%"))

        self.label17.setText(_translate("OtherWindow", str(self.curr_loc_forecast.temperature) + "°"))



        self.label.setText(_translate("OtherWindow", self.curr_loc_forecast['hourly']['summary']))

        self.btn_open.setText(_translate("Current Weather", "⇐" ))

#find the hour in that moment

        intero = int(int(self.curr_loc_forecast.time[12])* 10 +int(self.curr_loc_forecast.time[13]))
        self.btn_open1.setText(_translate("Current Weather", str(intero) + ":00"))
        intero = ((intero +3)%24)
        self.btn_open2.setText(_translate("Current Weather", str(intero) + ":00"))
        intero = ((intero + 3) % 24)
        self.btn_open3.setText(_translate("Current Weather", str(intero) + ":00"))
        intero = ((intero + 3) % 24)
        self.btn_open4.setText(_translate("Current Weather", str(intero) + ":00"))
        intero = ((intero + 3) % 24)
        self.btn_open5.setText(_translate("Current Weather", str(intero) + ":00"))
        intero = ((intero + 3) % 24)
        self.btn_open6.setText(_translate("Current Weather", str(intero) + ":00"))
        intero = ((intero + 3) % 24)
        self.btn_open7.setText(_translate("Current Weather", str(intero) + ":00"))


"""end of setting"""
