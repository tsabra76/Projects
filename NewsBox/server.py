__author__ = 'tarek'

import pywapi as weather
import easygui as gui
from flask import Flask
from reboot import rebootModem
import weatherpics

app = Flask(__name__)

@app.route('/ny')
def nyweather():
    NYnoaa_result = weather.get_weather_from_noaa('KJFK')
    NYweather = str("<h1 style=\"text-align:center;\">New York: " + NYnoaa_result['weather'] + " and " + NYnoaa_result['temp_f'] + " F.</h1>\n")
    if NYnoaa_result['weather'] == "Fair":
        return NYweather + weatherpics.sunny
    elif NYnoaa_result['weather'] == "Partly Cloudy" or NYnoaa_result['weather'] == "A Few Clouds":
        return NYweather + weatherpics.partly_cloudy
    else:
        return NYweather + weatherpics.cloudy



@app.route('/sf')
def sfweather():
    SFnoaa_result = weather.get_weather_from_noaa('KSFO')
    SFweather = str("<h1 style=\"text-align:center;\">San Francisco: " + SFnoaa_result['weather'] + " and " + SFnoaa_result['temp_f'] + " F.</h1>\n")
    if SFnoaa_result['weather'] == "Fair":
        return SFweather + weatherpics.sunny
    elif SFnoaa_result['weather'] == "Partly Cloudy" or SFnoaa_result['weather'] == "A Few Clouds":
        return SFweather + weatherpics.partly_cloudy
    else:
        return SFweather + weatherpics.cloudy

@app.route('/rebootmodem')
def reboot():
    rebootModem()
    return """The modem is rebooting now..."""

if __name__ == '__main__':
    app.run(use_reloader=True, debug=True)   

