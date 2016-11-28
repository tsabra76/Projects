# Regarding future.py:
#Although Python's thread syntax is nicer than in many
#languages, it can still be a pain if all one wants to
# do is run a time-consuming function in a separate thread,
# while allowing the main thread to continue uninterrupted.
# A Future provides a legible and intuitive way to achieve
# such an end.

import easygui as gui #gui
import pywapi as weather #weather api
from main import SBweather
#import future from future.py
import urllib
import json

#NY weather from the NOAA
NYnoaa_result = weather.get_weather_from_noaa('KJFK')

#SF weather
SFnoaa_result = weather.get_weather_from_noaa('KSFO')

#ElC_noaa_result = weather.get_weather_from_weather_com('10001')


#convert objects to strings

NYweather = str("New York: " + NYnoaa_result['weather'] + " and " + NYnoaa_result['temp_f'] + "F now.\n")
SFweather = str("San Francisco: " + SFnoaa_result['weather'] + " and " + SFnoaa_result['temp_f'] + "F now.\n")
#Eweather = str("El Cerrito: " + ElC_noaa_result['weather']+" and "+ElC_noaa_result['temp_f'] + "F now.")

#show weather in text boxes
gui.msgbox(NYweather + "\n" + SFweather + "\n")
SBweather()


