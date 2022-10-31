import json
import requests
import tkinter as tk
import time

# from urllib3 import disable_warnings
# disable_warnings()


# Функция, запрашивающая данные с сервера и создающая JSON файл с полученными данными
def getdata():
    endpoint_device = 'https://api.openweathermap.org/data/3.0/onecall?lat=55.75&lon=37.62&exclude=current,minutely,hourly,daily&appid=c460366863a89c212e2710bc9882b143'
    r_dev = requests.get(endpoint_device, verify=False)
    j_dev = json.loads(r_dev.text)
    with open('weather.json', 'w') as f:
        json.dump(j_dev, f)


# getdata()

with open('weather.json', 'r') as f:
    d = json.loads(f.read())



window = tk.Tk()

lbl_now = tk.Label(text="Now", font='Times 30').grid(column=0, row=0)
lbl_now_temp_text = tk.Label(text="Temp:", font='Times 15').grid(column=0, row=1)
lbl_now_temp_val = tk.Label(text=str(int(d['current']['temp']-273))+' °C', font='Times 15').grid(column=1, row=1)
lbl_now_feels_text = tk.Label(text="Feels:", font='Times 15').grid(column=0, row=2)
lbl_now_feels_val = tk.Label(text=str(int(d['current']['feels_like']-273))+' °C', font='Times 15').grid(column=1, row=2)
lbl_now_pressure_text = tk.Label(text="Pressure:", font='Times 15').grid(column=0, row=3)
lbl_now_pressure_val = tk.Label(text=str(d['current']['pressure']*0.75)+' mmHg', font='Times 15').grid(column=1, row=3)
lbl_now_humidity_text = tk.Label(text="Humidity:", font='Times 15').grid(column=0, row=4)
lbl_now_humidity_val = tk.Label(text=str(d['current']['humidity'])+' %', font='Times 15').grid(column=1, row=4)
lbl_now_dewpoint_text = tk.Label(text="Dew point:", font='Times 15').grid(column=0, row=5)
lbl_now_dewpoint_val = tk.Label(text=str(int(d['current']['dew_point']-273))+' °C', font='Times 15').grid(column=1, row=5)
lbl_now_uvi_text = tk.Label(text="UV index:", font='Times 15').grid(column=0, row=6)
lbl_now_uvi_val = tk.Label(text=str(d['current']['uvi']), font='Times 15').grid(column=1, row=6)
lbl_now_clouds_text = tk.Label(text="Cloudiness:", font='Times 15').grid(column=0, row=7)
lbl_now_clouds_val = tk.Label(text=str(d['current']['clouds'])+' %', font='Times 15').grid(column=1, row=7)
lbl_now_visibility_text = tk.Label(text="Visibility:", font='Times 15').grid(column=0, row=8)
lbl_now_visibility_val = tk.Label(text=str(d['current']['visibility'])+' m', font='Times 15').grid(column=1, row=8)
lbl_now_windspeed_text = tk.Label(text="Wind speed:", font='Times 15').grid(column=0, row=9)
lbl_now_windspeed_val = tk.Label(text=str(d['current']['wind_speed'])+' m/s', font='Times 15').grid(column=1, row=9)
lbl_now_windgust_text = tk.Label(text="Wind gust:", font='Times 15').grid(column=0, row=10)
lbl_now_windgust_val = tk.Label(text=str(d['current']['wind_gust'])+' m/s', font='Times 15').grid(column=1, row=10)
lbl_now_winddeg_text = tk.Label(text="Wind direction:", font='Times 15').grid(column=0, row=11)
lbl_now_winddeg_val = tk.Label(text=str(d['current']['wind_deg'])+' °', font='Times 15').grid(column=1, row=11)
now_rain = d['current'].get('rain')
if now_rain == None:
    now_rain = 'N/A'
else:
    now_rain = str(now_rain)+' mm'
lbl_now_rain_text = tk.Label(text="Rain:", font='Times 15').grid(column=0, row=12)
lbl_now_rain_val = tk.Label(text=now_rain, font='Times 15').grid(column=1, row=12)
now_snow = d['current'].get('snow')
if now_snow == None:
    now_snow = 'N/A'
else:
    now_snow = str(now_snow)+' mm'
lbl_now_snow_text = tk.Label(text="Snow:", font='Times 15').grid(column=0, row=13)
lbl_now_snow_val = tk.Label(text=now_snow, font='Times 15').grid(column=1, row=13)

lbl_separator1 = tk.Label(text="        ", font='Times 30').grid(column=3, row=0)
lbl_inonehour = tk.Label(text="In one hour", font='Times 30').grid(column=4, row=0)
lbl_inonehour_temp_text = tk.Label(text="Temp:", font='Times 15').grid(column=4, row=1)
lbl_inonehour_temp_val = tk.Label(text=str(int(d['hourly'][0]['temp']-273))+' °C', font='Times 15').grid(column=5, row=1)
lbl_inonehour_feels_text = tk.Label(text="Feels:", font='Times 15').grid(column=4, row=2)
lbl_inonehour_feels_val = tk.Label(text=str(int(d['hourly'][0]['feels_like']-273))+' °C', font='Times 15').grid(column=5, row=2)
lbl_inonehour_pressure_text = tk.Label(text="Pressure:", font='Times 15').grid(column=4, row=3)
lbl_inonehour_pressure_val = tk.Label(text=str(d['hourly'][0]['pressure']*0.75)+' mmHg', font='Times 15').grid(column=5, row=3)
lbl_inonehour_humidity_text = tk.Label(text="Humidity:", font='Times 15').grid(column=4, row=4)
lbl_inonehour_humidity_val = tk.Label(text=str(d['hourly'][0]['humidity'])+' %', font='Times 15').grid(column=5, row=4)
lbl_inonehour_dewpoint_text = tk.Label(text="Dew point:", font='Times 15').grid(column=4, row=5)
lbl_inonehour_dewpoint_val = tk.Label(text=str(int(d['hourly'][0]['dew_point']-273))+' °C', font='Times 15').grid(column=5, row=5)
lbl_inonehour_uvi_text = tk.Label(text="UV index:", font='Times 15').grid(column=4, row=6)
lbl_inonehour_uvi_val = tk.Label(text=str(d['hourly'][0]['uvi']), font='Times 15').grid(column=5, row=6)
lbl_inonehour_clouds_text = tk.Label(text="Cloudiness:", font='Times 15').grid(column=4, row=7)
lbl_inonehour_clouds_val = tk.Label(text=str(d['hourly'][0]['clouds'])+' %', font='Times 15').grid(column=5, row=7)
lbl_inonehour_visibility_text = tk.Label(text="Visibility:", font='Times 15').grid(column=4, row=8)
lbl_inonehour_visibility_val = tk.Label(text=str(d['hourly'][0]['visibility'])+' m', font='Times 15').grid(column=5, row=8)
lbl_inonehour_windspeed_text = tk.Label(text="Wind speed:", font='Times 15').grid(column=4, row=9)
lbl_inonehour_windspeed_val = tk.Label(text=str(d['hourly'][0]['wind_speed'])+' m/s', font='Times 15').grid(column=5, row=9)
lbl_inonehour_windgust_text = tk.Label(text="Wind gust:", font='Times 15').grid(column=4, row=10)
lbl_inonehour_windgust_val = tk.Label(text=str(d['hourly'][0]['wind_gust'])+' m/s', font='Times 15').grid(column=5, row=10)
lbl_inonehour_winddeg_text = tk.Label(text="Wind direction:", font='Times 15').grid(column=4, row=11)
lbl_inonehour_winddeg_val = tk.Label(text=str(d['hourly'][0]['wind_deg'])+' °', font='Times 15').grid(column=5, row=11)
inonehour_rain = d['hourly'][0].get('rain')
if inonehour_rain == None:
    inonehour_rain = 'N/A'
else:
    inonehour_rain = str(inonehour_rain)+' mm'
lbl_inonehour_rain_text = tk.Label(text="Rain:", font='Times 15').grid(column=4, row=12)
lbl_inonehour_rain_val = tk.Label(text=inonehour_rain, font='Times 15').grid(column=5, row=12)
inonehour_snow = d['hourly'][0].get('snow')
if inonehour_snow == None:
    inonehour_snow = 'N/A'
else:
    inonehour_snow = str(inonehour_snow)+' mm'
lbl_inonehour_snow_text = tk.Label(text="Snow:", font='Times 15').grid(column=4, row=13)
lbl_inonehour_snow_val = tk.Label(text=inonehour_snow, font='Times 15').grid(column=5, row=13)

lbl_separator2 = tk.Label(text="        ", font='Times 30').grid(column=6, row=0)
lbl_today = tk.Label(text="Today", font='Times 30').grid(column=7, row=0)
lbl_today_sunrise_text = tk.Label(text="Sunrise:", font='Times 15').grid(column=7, row=1)
lbl_today_sunrise_val = tk.Label(text=time.strftime("%H:%M:%S", time.localtime(int(d['daily'][0]['sunrise']))), font='Times 15').grid(column=8, row=1)
lbl_today_sunset_text = tk.Label(text="Sunset:", font='Times 15').grid(column=7, row=2)
lbl_today_sunset_val = tk.Label(text=time.strftime("%H:%M:%S", time.localtime(int(d['daily'][0]['sunset']))), font='Times 15').grid(column=8, row=2)
today_phase = str
match(int(d['daily'][0]['moon_phase']*7+1)):
    case 1:
        today_phase = 'New moon'
    case 2:
        today_phase = 'Young moon'
    case 3:
        today_phase = 'First quarter'
    case 4:
        today_phase = 'Waking moon.'
    case 5:
        today_phase = 'Full moon'
    case 6:
        today_phase = 'Waning moon.'
    case 7:
        today_phase = 'Last quarter'
    case 8:
        today_phase = 'Old moon.'
lbl_today_moonphase_text = tk.Label(text="Moon phase:", font='Times 15').grid(column=7, row=3)
lbl_today_moonphase_val = tk.Label(text=today_phase, font='Times 15').grid(column=8, row=3)
lbl_today_pressure_text = tk.Label(text="Pressure:", font='Times 15').grid(column=7, row=4)
lbl_today_pressure_val = tk.Label(text=str(d['daily'][0]['pressure']*0.75)+' mmHg', font='Times 15').grid(column=8, row=4)
lbl_today_humidity_text = tk.Label(text="Humidity:", font='Times 15').grid(column=7, row=5)
lbl_today_humidity_val = tk.Label(text=str(d['daily'][0]['humidity'])+' %', font='Times 15').grid(column=8, row=5)
lbl_today_dewpoint_text = tk.Label(text="Dew point:", font='Times 15').grid(column=7, row=6)
lbl_today_dewpoint_val = tk.Label(text=str(int(d['daily'][0]['dew_point']-273))+' °C', font='Times 15').grid(column=8, row=6)
lbl_today_uvi_text = tk.Label(text="UV index:", font='Times 15').grid(column=7, row=7)
lbl_today_uvi_val = tk.Label(text=str(d['daily'][0]['uvi']), font='Times 15').grid(column=8, row=7)
lbl_today_clouds_text = tk.Label(text="Cloudiness:", font='Times 15').grid(column=7, row=8)
lbl_today_clouds_val = tk.Label(text=str(d['daily'][0]['clouds'])+' %', font='Times 15').grid(column=8, row=8)
lbl_today_pop_text = tk.Label(text="Probability of precipitation:", font='Times 15').grid(column=7, row=9)
lbl_today_pop_val = tk.Label(text=str(float(d['daily'][0]['pop'])*100)+' %', font='Times 15').grid(column=8, row=9)
lbl_today_windspeed_text = tk.Label(text="Wind speed:", font='Times 15').grid(column=7, row=10)
lbl_today_windspeed_val = tk.Label(text=str(d['daily'][0]['wind_speed'])+' m/s', font='Times 15').grid(column=8, row=10)
lbl_today_windgust_text = tk.Label(text="Wind gust:", font='Times 15').grid(column=7, row=11)
lbl_today_windgust_val = tk.Label(text=str(d['daily'][0]['wind_gust'])+' m/s', font='Times 15').grid(column=8, row=11)
lbl_today_winddeg_text = tk.Label(text="Wind direction:", font='Times 15').grid(column=7, row=12)
lbl_today_winddeg_val = tk.Label(text=str(d['daily'][0]['wind_deg'])+' °', font='Times 15').grid(column=8, row=12)
today_rain = d['daily'][0].get('rain')
if today_rain == None:
    today_rain = 'N/A'
else:
    today_rain = str(today_rain)+' mm'
lbl_today_rain_text = tk.Label(text="Rain:", font='Times 15').grid(column=7, row=13)
lbl_today_rain_val = tk.Label(text=today_rain, font='Times 15').grid(column=8, row=13)
today_snow = d['daily'][0].get('snow')
if today_snow == None:
    today_snow = 'N/A'
else:
    today_snow = str(today_snow)+' mm'
lbl_today_snow_text = tk.Label(text="Snow:", font='Times 15').grid(column=7, row=14)
lbl_today_snow_val = tk.Label(text=today_snow, font='Times 15').grid(column=8, row=14)
lbl_todaytemp = tk.Label(text="Today temperature", font='Times 20').grid(column=7, row=15)
lbl_todayfacttemp = tk.Label(text="Fact", font='Times 20').grid(column=8, row=16)
lbl_todayfeeltemp = tk.Label(text="Feel", font='Times 20').grid(column=9, row=16)
lbl_today_temp_morn_text = tk.Label(text="Morning:", font='Times 15').grid(column=7, row=17)
lbl_today_temp_morn_val = tk.Label(text=str(int(d['daily'][0]['temp']['morn'])-273)+' °C', font='Times 15').grid(column=8, row=17)
lbl_today_feels_morn_val = tk.Label(text=str(int(d['daily'][0]['feels_like']['morn'])-273)+' °C', font='Times 15').grid(column=9, row=17)
lbl_today_temp_day_text = tk.Label(text="Day:", font='Times 15').grid(column=7, row=18)
lbl_today_temp_day_val = tk.Label(text=str(int(d['daily'][0]['temp']['day'])-273)+' °C', font='Times 15').grid(column=8, row=18)
lbl_today_feels_day_val = tk.Label(text=str(int(d['daily'][0]['feels_like']['day'])-273)+' °C', font='Times 15').grid(column=9, row=18)
lbl_today_temp_eve_text = tk.Label(text="Evening:", font='Times 15').grid(column=7, row=19)
lbl_today_temp_eve_val = tk.Label(text=str(int(d['daily'][0]['temp']['eve'])-273)+' °C', font='Times 15').grid(column=8, row=19)
lbl_today_feels_eve_val = tk.Label(text=str(int(d['daily'][0]['feels_like']['eve'])-273)+' °C', font='Times 15').grid(column=9, row=19)
lbl_today_temp_night_text = tk.Label(text="Night:", font='Times 15').grid(column=7, row=20)
lbl_today_temp_night_val = tk.Label(text=str(int(d['daily'][0]['temp']['night'])-273)+' °C', font='Times 15').grid(column=8, row=20)
lbl_today_feels_night_val = tk.Label(text=str(int(d['daily'][0]['feels_like']['night'])-273)+' °C', font='Times 15').grid(column=9, row=20)










window.mainloop()