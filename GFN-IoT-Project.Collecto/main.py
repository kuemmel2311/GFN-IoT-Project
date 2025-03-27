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
                   "daynight": daynight}, file)


def data_measurement():

    last_data = json.loads(load_last_data())

    data_changed = False

    temp, pres, humi = Sensor_Read.ReadTempSensor()

    if temp != last_data['temp']:
        API_Request.send_temp(temp)
        data_changed = True

    if pres != last_data['pressure']:
        API_Request.send_pressure(pres)
        data_changed= True

    if humi != last_data['humidity']:
        API_Request.send_humidity(humi)
        data_changed = True

    airquality, daynight = Sensor_Read.ReadAirSenor()

    if airquality != last_data['airquality']:
        API_Request.send_airquality(airquality)
        data_changed = True

    if daynight != last_data['daynight']:
        API_Request.send_daynight(daynight)
        data_changed = True

    if data_changed:
        save_last_data(humi, pres, temp, airquality, daynight)

data_measurement()