import json
from api_client import API_Request
from sensor_client import Sensor_Read

def load_last_data():
    try:
        with open("last_data.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {"humidity": None, "pressure": None, "temp": None, "airquality": None, "daynight": None}

def save_last_data(humidity, pressure, temp, airquality, daynight):
    with open("last_data.json", "w") as file:
        json.dump({"humidity": humidity,
                   "pressure": pressure,
                   "temp": temp,
                   "airquality": airquality,
                   "daynight": daynight})



def data_measurement():

    last_data = load_last_data()

    data_changed = False

    temp, pres, humi = Sensor_Read.ReadTempSensor()

    if temp != last_Temp:
        API_Request.send_temp(temp)
        last_Temp = temp
        data_changed = True

    if pres != last_Pressure:
        API_Request.send_pressure(pres)
        last_Pressure = pres
        data_changed= True

    if humi != last_Humidity:
        API_Request.send_humidity(humi)
        last_Humidity = humi
        data_changed = True

    airquality, daynight = Sensor_Read.ReadAirSenor()

    if airquality != last_AirQuality:
        API_Request.send_airquality(airquality)
        last_AirQuality = airquality
        data_changed = True

    if daynight != last_DayNight:
        API_Request.send_daynight(daynight)
        last_DayNight = daynight
        data_changed = True

    if data_changed:
        save_last_data(last_Humidity, last_Pressure, last_Temp, last_AirQuality, last_DayNight)

data_measurement()