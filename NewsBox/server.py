__author__ = 'tarek'

import pywapi as weather
import easygui as gui
from flask import Flask
from reboot import rebootModem

app = Flask(__name__)

@app.route('/ny')
def nyweather():
	NYnoaa_result = weather.get_weather_from_noaa('KJFK')
	NYweather = str("New York: " + NYnoaa_result['weather'] + " and " + NYnoaa_result['temp_f'] + "F.\n")
	return NYweather


@app.route('/sf')
def sfweather():
    SFnoaa_result = weather.get_weather_from_noaa('KSFO')
    SFweather = str("San Francisco: " + SFnoaa_result['weather'] + " and " + SFnoaa_result['temp_f'] + "F.")
    return SFweather

@app.route('/rebootmodem')
def reboot():
    rebootModem()
    return """The modem is rebooting now..."""

if __name__ == '__main__':
    app.run(use_reloader=True, debug=True)   

