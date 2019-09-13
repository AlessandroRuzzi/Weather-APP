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
