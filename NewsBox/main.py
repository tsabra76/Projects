__author__ = 'tarek'

import pywapi as weather
import easygui as gui
from pylms.server import Server
from pylms.player import Player


sc = Server(hostname="192.168.0.25", port='9090')
sc.connect()

sqPCroom = sc.get_player("00:04:20:2a:70:77") #computer room SB

NYnoaa_result = weather.get_weather_from_noaa('KJFK')
SFnoaa_result = weather.get_weather_from_noaa('KSFO')

NYweather = str("New York: " + NYnoaa_result['weather'] + " and " + NYnoaa_result['temp_f'] + "F.\n")
SFweather = str("San Francisco: " + SFnoaa_result['weather'] + " and " + SFnoaa_result['temp_f'] + "F.\n")

gui.msgbox(SFweather + "\n" + NYweather)
#sqPCroom.show(line1=SFweather, line2=NYweather, duration=2, brightness=4, font='standard', centered=False)
if gui.msgbox:
    exit()
