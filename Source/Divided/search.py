"""Setting up the page for requested cities"""


class Ui_OtherWindow_search(object):

    def __init__(self,location):
         self.location = location
        
#next hours function

    def on_hour(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_OtherWindow_hours(self.curr_loc,self.curr_loc_forecast,self.location)
        self.ui.setupUi(self.window)
        self.OtherWindow.hide()
        self.window.show()
        
#next days function

    def on_day(self,number):
        self.window = QtWidgets.QMainWindow()
        l = get_next_5_days()
        self.l = l
        day = self.l[number]
        self.ui = Ui_OtherWindow_day(self.curr_loc, self.curr_loc_forecast, self.location,day,number)
        self.ui.setupUi(self.window)
        self.OtherWindow.hide()
        self.window.show()

#search functions

    def on_search(self):
        try:
           textbox_value = self.textbox.text()
           location = get_lat_and_long(textbox_value)
           self.location = location
           self.window = QtWidgets.QMainWindow()
           self.ui = Ui_OtherWindow_search(location)
           self.ui.setupUi(self.window)
           self.OtherWindow.hide()
           self.window.show()

        except:
            loc2 = str(self.curr_loc[0]['name'] + "," + self.curr_loc[0]['cc'])
            location = get_lat_and_long(loc2)
            self.location = location
            self.window = QtWidgets.QMainWindow()
            self.ui = Ui_OtherWindow_back(location)
            self.ui.setupUi(self.window)
            self.OtherWindow.hide()
            self.window.show()

    def setupUi(self, OtherWindow):
        self.OtherWindow = OtherWindow
        OtherWindow.setObjectName("OtherWindow")
        OtherWindow.resize(800, 500)
        location = self.location
        current_loc_forecast, curr_loc = get_forecast_search(location)
        self.curr_loc = curr_loc
        self.curr_loc_forecast = current_loc_forecast
        self.centralwidget = QtWidgets.QWidget(OtherWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.centralwidget.setStyleSheet(
            "QWidget {background-color: rgba(0,41,59,255);} QScrollBar:horizontal {width: 1px; height: 1px;"
            "background-color: rgba(0,41,59,255);} QScrollBar:vertical {width: 1px; height: 1px;"
            "background-color: rgba(0,41,59,255);}")

        self.label.setGeometry(QtCore.QRect(30,5, 300, 300))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")


        self.label1 = QtWidgets.QLabel(self.centralwidget)
        self.label1.setGeometry(QtCore.QRect(0, 0, 300, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label1.setFont(font)
        self.label1.setObjectName("label1")

        self.label2 = QtWidgets.QLabel(self.centralwidget)
        self.label2.setGeometry(QtCore.QRect(350, 70, 250, 190))
        pixmap = QtGui.QPixmap(str(current_loc_forecast.icon) + '.jpg')
        self.label2.setPixmap(pixmap)

        self.label3 = QtWidgets.QLabel(self.centralwidget)
        self.label3.setGeometry(QtCore.QRect(0, 270, 300, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label3.setFont(font)
        self.label3.setObjectName("label3")

        self.label4 = QtWidgets.QLabel(self.centralwidget)
        self.label4.setGeometry(QtCore.QRect(470, 0, 300, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label4.setFont(font)
        self.label4.setObjectName("label4")


        self.btn_open1 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_open1.setGeometry(QtCore.QRect(10, 330, 141, 51))
        self.btn_open1.setObjectName("btn_open1")
        self.btn_open1.clicked.connect(lambda: self.on_day(0))

        self.btn_open2 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_open2.setGeometry(QtCore.QRect(171, 330, 141, 51))
        self.btn_open2.setObjectName("btn_open2")
        self.btn_open2.clicked.connect(lambda: self.on_day(1))


        self.btn_open3 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_open3.setGeometry(QtCore.QRect(332, 330, 141, 51))
        self.btn_open3.setObjectName("btn_open3")
        self.btn_open3.clicked.connect(lambda: self.on_day(2))

        self.btn_open4 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_open4.setGeometry(QtCore.QRect(493, 330, 141, 51))
        self.btn_open4.setObjectName("btn_open4")
        self.btn_open4.clicked.connect(lambda: self.on_day(3))

        self.btn_open5 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_open5.setGeometry(QtCore.QRect(654, 330, 141, 51))
        self.btn_open5.setObjectName("btn_open5")
        self.btn_open5.clicked.connect(lambda: self.on_day(4))


        self.btn_open6 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_open6.setGeometry(QtCore.QRect(640, 140, 141, 51))
        self.btn_open6.setObjectName("btn_open6")
        self.btn_open6.clicked.connect(self.on_hour)

        self.btn_open7 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_open7.setGeometry(QtCore.QRect(746, 5, 40, 41))
        self.btn_open7.setObjectName("btn_open7")
        self.btn_open7.clicked.connect(self.on_search)

        self.textbox = QtWidgets.QLineEdit(self.centralwidget)
        self.textbox.setGeometry(QtCore.QRect(570,5,171,41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.textbox.setFont(font)
        self.textbox.setStyleSheet("QLineEdit { background: rgb(255, 255, 255); selection-background-color: rgb(233, 99, 0); }")


        OtherWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(OtherWindow)

        self.statusbar.setObjectName("statusbar")
        OtherWindow.setStatusBar(self.statusbar)

        self.retranslateUi(OtherWindow,current_loc_forecast,curr_loc)
        QtCore.QMetaObject.connectSlotsByName(OtherWindow)

    def retranslateUi(self, OtherWindow,current_loc_forecast,curr_loc):
        _translate = QtCore.QCoreApplication.translate
        OtherWindow.setWindowTitle(_translate("OtherWindow", "Current Weather"))
        self.label1.setText(_translate("OtherWindow","Current Forecast: "))
        self.label4.setText(_translate("OtherWindow", "Search: "))
        
        """handling with different time zone"""
        loc2 = str(self.curr_loc[0]['name'] + "," + self.curr_loc[0]['cc'])

        location = get_lat_and_long(loc2)
        tz = tzwhere.tzwhere()
        timeZoneStr = tz.tzNameAt(location.latitude, location.longitude)
        timeZoneObj = timezone(timeZoneStr)
        now_time = datetime.now(timeZoneObj)
        time =get_time(now_time)
        self.curr_loc_forecast.time = time
        """end of error handling"""
        
        l = get_next_5_days()
        self.l = l
        self.label.setText(_translate("OtherWindow","Current Location: " + (curr_loc[0]['name']) + "(" + curr_loc[0]['admin1'] + "," + curr_loc[0]['cc'] + ")" +

                                                     "\nCurrent Time: " + str(self.curr_loc_forecast.time) +
                                                     "\nCurrent Temperature: " + str(current_loc_forecast.temperature) + " °C" +
                                                     "\nPerceived Temperature: " + str(current_loc_forecast.apparentTemperature) + " °C" +
                                                     "\nHumidity: " + str(int(current_loc_forecast.humidity * 100)) + "%"
                                                     "\nSummary: " + str(current_loc_forecast.summary) +
                                                     "\nPrecipitation Probability: " + str(int(current_loc_forecast.precipProbability*100)) + "%"
                                                     "\nWind Speed: " + str(current_loc_forecast.windSpeed) + " Km/h"))
        self.label3.setText(_translate("OtherWindow", "Next Days: "))
        count = 0
        self.btn_open1.setText(_translate("Current Weather", str(l[count])))
        count+=1
        self.btn_open2.setText(_translate("Current Weather", str(l[count])))
        count += 1
        self.btn_open3.setText(_translate("Current Weather", str(l[count])))
        count+=1
        self.btn_open4.setText(_translate("Current Weather", str(l[count])))
        count += 1
        self.btn_open5.setText(_translate("Current Weather", str(l[count])))

        self.btn_open6.setText(_translate("Current Weather", "Next Hours"))

        self.btn_open7.setText(_translate("Current Weather", "🔍"))

        self.textbox.setPlaceholderText("Example: Milan,IT")
        

"""end of setting """
