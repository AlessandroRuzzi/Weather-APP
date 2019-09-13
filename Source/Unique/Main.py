"""""***********************************************************************
* Project           : WEATHER APP 2019
*
* Program name      : main.py
*
* Author            : Alessandro Ruzzi
*
* Date created      : 09/09/2019
*
* Purpose           : using Dark Sky API for forecast and PYQT5 for Graphic visualization
                      to implement a Weather app

                      Main function:
                        -Current Position's Weather Forecast
                        -Next days function
                        -Next hours function
                        -Search function
                        -Error Handling
*
* Revision History  :
*
* Date          Author        Ref    Revision (13/09/2019)
* 13/09/2019    A. Ruzzi      4      Correct the key insertion and commented the code properly
*
***********************************************************************"""



try:

    from PyQt5 import QtWidgets, QtGui, QtCore
    import requests
    import reverse_geocoder as rg
    import sys
    from datetime import datetime
    import json
    import geocoder
    from darksky import forecast
    from geopy.geocoders import Nominatim
    from tzwhere import tzwhere
    from pytz import timezone


except:
    print("error with libraries")

""" Functions"""


# convert time to adpat to different time zone

def get_time(now_time):
    if(int(now_time.month) <10 ):
        time ="0" + str(now_time.month) + "/"
    else:
        time = str(now_time.month) + "/"
    if (int(now_time.day) < 10):
        time += "0" + str(now_time.day) + "/"
    else:
        time += str(now_time.day) + "/"
    time +=str(now_time.year) + ", "

    if (int(now_time.hour) < 10):
        time += "0" + str(now_time.month) + ":"
    else:
        time += str(now_time.hour) + ":"
    if (int(now_time.minute) < 10):
        time += "0" + str(now_time.minute) + ":"
    else:
        time += str(now_time.minute) + ":"
    if (int(now_time.second) < 10):
        time += "0" + str(now_time.second)
    else:
        time += str(now_time.second)
    return time


#get latitude and longitude of the requested cities

def get_lat_and_long(name):
    geolocator = Nominatim()
    location = geolocator.geocode((name))
    return location


#create a lis of the next five days after today

def get_next_5_days():
    d = get_dict_of_week()

    today = str(datetime.today().strftime('%A'))

    l = []
    count = 0
    count2 = 0

    for day in d:
        count += 1
        if (day == today):
            break

    for i in range(5):
        pos = count % 7
        count2 = 0
        for day in d:
            pos_day = day
            if (count2 == pos):
                break
            count2 += 1
        l.append(d[pos_day])
        count += 1

    return l


#create a dictionary to translate from italian to english, change the italian words with your language traduction

def get_dict_of_week():
    d = {'lunedì':'Monday', 'martedì':'Tuesday' , 'mercoledì':'Wednesday', 'giovedì':'Thursday','venerdì':'Friday','sabato':'Saturday','domenica':'Sunday'}
    return d


#get the forecast of the current location with the Dark Sky API

def get_forecast():

    myloc = geocoder.ip('me')

    current_loc_forecast = forecast(key, myloc.latlng[0], myloc.latlng[1])

    # conversion of location,time and temperatures:
    curr_loc = get_location_name(list(myloc.latlng))
    current_loc_forecast.time = convert_time(current_loc_forecast.time)
    current_loc_forecast.temperature = convert_temperatures(current_loc_forecast.temperature)
    current_loc_forecast.apparentTemperature = convert_temperatures(current_loc_forecast.apparentTemperature)
    # end of conversion
    return current_loc_forecast,curr_loc


#get the forecast of the searched cities with the Dark Sky API

def get_forecast_search(location):

    current_loc_forecast = forecast(key, location.latitude, location.longitude)

    # conversion of location,time and temperatures:
    l1 = []
    l1.append(location.latitude)
    l1.append(location.longitude)
    curr_loc = get_location_name(l1)
    current_loc_forecast.time = convert_time(current_loc_forecast.time)
    current_loc_forecast.temperature = convert_temperatures(current_loc_forecast.temperature)
    current_loc_forecast.apparentTemperature = convert_temperatures(current_loc_forecast.apparentTemperature)
    # end of conversion
    return current_loc_forecast,curr_loc


#get the name of a city guven latitude and longitude

def get_location_name(coordinates):
    result = rg.search(coordinates)
    return result


#convert time in the right format

def convert_time(time):
    date_time = datetime.fromtimestamp(time)
    return date_time.strftime("%m/%d/%Y, %H:%M:%S")


#convert temperature from fahrenheit to celsius

def convert_temperatures(temperature):
    return int(((temperature-32)*5)/9)


"""End of Functions"""











"""setting up the page for the current location forecast"""


class Ui_OtherWindow(object):

#next days functions

    def on_day(self,number):
        self.window = QtWidgets.QMainWindow()
        l = get_next_5_days()
        self.l = l
        day = self.l[number]
        loc2 = str(self.curr_loc[0]['name'] + "," + self.curr_loc[0]['cc'])
        location = get_lat_and_long(loc2)
        self.location = location
        self.ui = Ui_OtherWindow_day(self.curr_loc, self.curr_loc_forecast, self.location,day,number)
        self.ui.setupUi(self.window)
        self.Otherwindow.hide()
        self.window.show()

#next hours function

    def on_hour(self):
        self.window = QtWidgets.QMainWindow()
        loc2 = str(self.curr_loc[0]['name'] + "," + self.curr_loc[0]['cc'])
        location = get_lat_and_long(loc2)
        self.ui = Ui_OtherWindow_hours(self.curr_loc,self.curr_loc_forecast,location)
        self.ui.setupUi(self.window)
        self.Otherwindow.hide()
        self.window.show()

#search function

    def on_search(self):
        try:
            textbox_value = self.textbox.text()
            location = get_lat_and_long(textbox_value)
            self.location = location
            self.window = QtWidgets.QMainWindow()
            self.ui = Ui_OtherWindow_search(location)
            self.ui.setupUi(self.window)
            self.Otherwindow.hide()
            self.window.show()

        except:
            loc2 = str(self.curr_loc[0]['name'] + "," + self.curr_loc[0]['cc'])
            location = get_lat_and_long(loc2)
            self.window = QtWidgets.QMainWindow()
            self.ui = Ui_OtherWindow_back(location)
            self.ui.setupUi(self.window)
            self.Otherwindow.hide()
            self.window.show()


    def setupUi(self, OtherWindow):
        self.Otherwindow = OtherWindow
        OtherWindow.setObjectName("OtherWindow")
        OtherWindow.resize(800, 500)
        current_loc_forecast, curr_loc = get_forecast()
        self.curr_loc = curr_loc
        self.curr_loc_forecast =current_loc_forecast
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
        print(current_loc_forecast.icon)
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
        self.textbox.setStyleSheet("QLineEdit { background: rgb(255y, 255, 255); selection-background-color: rgb(233, 99, 0); }")


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


        l = get_next_5_days()

        self.label.setText(_translate("OtherWindow","Current Location: " + (curr_loc[0]['name']) + "(" + curr_loc[0]['admin1'] + "," + curr_loc[0]['cc'] + ")" +

                                                     "\nCurrent Time: " + str(current_loc_forecast.time) +
                                                     "\nCurrent Temperature: " + str(current_loc_forecast.temperature) + " °C" +
                                                     "\nPerceived Temperature: " + str(current_loc_forecast.apparentTemperature) + " °C" +
                                                     "\nHumidity: " + str(int(current_loc_forecast.humidity * 100)) + "%"
                                                     "\nSummary: " + str(current_loc_forecast.summary) +
                                                     "\nPrecipitation Probability: " + str(int(current_loc_forecast.precipProbability*100)) + "%"
                                                     "\nWind Speed: " + str(current_loc_forecast.windSpeed) + " Km/h" ))
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

"""end of setting"""










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










"""setting up the page for the next days functions"""


class Ui_OtherWindow_day(object):

    def __init__(self,name,forecast,location,day,number):
        self.curr_loc = name
        self.curr_loc_forecast = forecast
        self.location = location
        self.day =day
        self.number = number

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

        self.label.setGeometry(QtCore.QRect(2,43,400 , 27))
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
        self.label17.setStyleSheet("font: 57pt Arial Black")
        self.label17.setObjectName("label17")


        self.label2 = QtWidgets.QLabel(self.centralwidget)
        self.label2.setGeometry(QtCore.QRect(300, 70, 250, 190))
        pixmap = QtGui.QPixmap(str(self.curr_loc_forecast['daily']['data'][(self.number +1)]['icon']) + '.jpg')
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
        OtherWindow.setWindowTitle(_translate("OtherWindow", self.day))

        self.label1.setText(_translate("OtherWindow",self.curr_loc[0]['name'] + "-> " + self.day))


        self.label3.setText(_translate("OtherWindow", "⇓"))
        self.label4.setText(_translate("OtherWindow", "⇓"))
        self.label5.setText(_translate("OtherWindow", "⇓"))
        self.label6.setText(_translate("OtherWindow", "⇓"))
        self.label7.setText(_translate("OtherWindow", "⇓"))
        self.label8.setText(_translate("OtherWindow", "⇓"))
        self.label9.setText(_translate("OtherWindow", "⇓"))

        intero = int(int(self.curr_loc_forecast.time[12]) * 10 + int(self.curr_loc_forecast.time[13]))

        conta = 24 -intero

        conta = conta +(24 * self.number)

#extend hourly to get the next days forecast

        self.curr_loc_forecast.refresh( extend = 'hourly')

        self.label10.setText(_translate("OtherWindow", "Temp-> " + str(int(int(((self.curr_loc_forecast['hourly']['data'][conta]['temperature']) -32) *5)/9 )) + "°C" +
                                        "\nPrec-> " + str((int(self.curr_loc_forecast['hourly']['data'][conta]['precipProbability'] *100))) + "%" ))
        conta +=4

        self.label11.setText(_translate("OtherWindow", "Temp-> " + str(int(int(((self.curr_loc_forecast['hourly']['data'][conta]['temperature']) - 32) * 5) / 9)) + "°C" +
                                        "\nPrec-> " + str((int(self.curr_loc_forecast['hourly']['data'][conta]['precipProbability'] * 100))) + "%"))
        conta += 4

        self.label12.setText(_translate("OtherWindow", "Temp-> " + str(int(int(((self.curr_loc_forecast['hourly']['data'][conta]['temperature']) - 32) * 5) / 9)) + "°C" +
                                        "\nPrec-> " + str((int(self.curr_loc_forecast['hourly']['data'][conta]['precipProbability'] * 100))) + "%"))
        conta += 4

        self.label13.setText(_translate("OtherWindow", "Temp-> " + str(int(int(((self.curr_loc_forecast['hourly']['data'][conta]['temperature']) -32) *5)/9 )) + "°C" +
                                        "\nPrec-> " + str((int(self.curr_loc_forecast['hourly']['data'][conta]['precipProbability'] *100))) + "%" ))

        self.label14.setText(_translate("OtherWindow", "Temp-> " + str(int(int(((self.curr_loc_forecast['hourly']['data'][conta]['temperature']) - 32) * 5) / 9)) + "°C" +
                                        "\nPrec-> " + str((int(self.curr_loc_forecast['hourly']['data'][conta]['precipProbability'] * 100))) + "%"))
        conta += 4

        self.label15.setText(_translate("OtherWindow", "Temp-> " + str(int(int(((self.curr_loc_forecast['hourly']['data'][conta]['temperature']) - 32) * 5) / 9)) + "°C" +
                                        "\nPrec-> " + str((int(self.curr_loc_forecast['hourly']['data'][conta]['precipProbability'] * 100))) + "%"))
        conta += 4

        self.label16.setText(_translate("OtherWindow", "Temp-> " + str(int(int(((self.curr_loc_forecast['hourly']['data'][conta]['temperature']) - 32) * 5) / 9)) + "°C" +
                                        "\nPrec-> " + str((int(self.curr_loc_forecast['hourly']['data'][conta]['precipProbability'] * 100))) + "%"))

        self.label17.setText(_translate("OtherWindow", str(int(int(((self.curr_loc_forecast['daily']['data'][(self.number +1)]['temperatureMax']) -32) *5) /9)) + "°" + "/" +
                                        str(int(int(((self.curr_loc_forecast['daily']['data'][(self.number +1)]['temperatureMin']) -32) *5) /9)) + "°" ))


        self.label.setText(_translate("OtherWindow", self.curr_loc_forecast['daily']['data'][(self.number+1)]['summary']))

        self.btn_open.setText(_translate("Current Weather", "⇐" ))
                                                                 

        self.btn_open1.setText(_translate("Current Weather", "00:00"))

        self.btn_open2.setText(_translate("Current Weather",  "04:00"))

        self.btn_open3.setText(_translate("Current Weather", "08:00"))

        self.btn_open4.setText(_translate("Current Weather", "12:00"))

        self.btn_open5.setText(_translate("Current Weather", "16:00"))

        self.btn_open6.setText(_translate("Current Weather", "20:00"))

        self.btn_open7.setText(_translate("Current Weather", "00:00"))

"""end of setting"""










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


