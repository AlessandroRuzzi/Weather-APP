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
