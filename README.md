# Weather APP
Weather APP is a desktop app that use [Dark Sky API](https://darksky.net/dev) to obtain weather forecast, and [PyQT 5](https://pypi.org/project/PyQt5/) for the GUI.
<br/><br/><br/><br/>
![alt text](Docs/DarkSky.jpg?raw=true)
![alt text](Docs/qt.png?raw=true)
<br/><br/><br/><br/>
<br/>There are 6 Different functions: 

1. Starting Page
2. Currenct location forecast.<br/>
3. Search for specific countries'forecast.<br/>
4. Next hours forecast for both current location and searched location.<br/>
5. Next 5 days forecast for both current location and searched location.<br/>
6. Error Handling when searchin for wrong countries.<br/>

# How It Works
### 1. Starting page:

![alt text](Docs/Main.png?raw=true)
<br/><br/><br/><br/>
:small_blue_diamond: At the beginning you have to subscribe to to linked site to obtain your code for weather forecast and you can click on the search button to obtain the forecast of your current location.
<br/><br/><br/><br/>

### 2. Currenct location forecast:
![alt text](Docs/Curr_loc.png?raw=true)
<br/><br/><br/><br/>
:small_blue_diamond: Here are showed all the information about the current position in that moment,then there is the search bar to look for other cities and also next hours button and next days buttons
<br/><br/><br/><br/>

### 3. Search for specific countries'forecast:
![alt text](Docs/Search.png?raw=true)
<br/><br/><br/><br/>
:small_blue_diamond: Here are showed all the information about the current position in that moment for the requested city,then there is the search bar to look for other cities and also next hours button and next days buttons
<br/><br/><br/><br/>
### 4. Next hours forecast for both current location and searched location:
![alt text](Docs/next_hours.png?raw=true)
<br/><br/><br/><br/>
:small_blue_diamond: Here are showed the temperature and the precipitation probability for the next hours for the current location or for the requested city and also the current temperature(the big one),then there is the back button to return to the previous page.
<br/><br/><br/><br/>
### 5. Next 5 days forecast for both current location and searched location:
![alt text](Docs/next_days.png?raw=true)
<br/><br/><br/><br/>
:small_blue_diamond: Here are showed the temperature and the precipitation probability for alle the hours of the selected for the current location or for the requested city and also the Max. and Min. temperatures of the day(the big one),then there is the back button to return to the previous page.
### 6. Error Handling when searchin for wrong countries:
![alt text](Docs/error.png?raw=true)
<br/><br/><br/><br/>
:small_blue_diamond: If the user try to search for a non exisiting country, then this error page will be displayed.
<br/><br/><br/><br/>


# License
:books: This project is distributed under the terms of the Apache License v2.0. See file [LICENSE](LICENSE) for further reference.
