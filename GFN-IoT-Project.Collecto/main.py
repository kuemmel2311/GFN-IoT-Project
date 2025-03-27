import time
import json
from api_client import API_Request
from sensor_client import Sensor_Read

def load_last_data():
    try:
        with open("last_data.json", "r") as file:
            return json.load(file)   
    except (FileNotFoundError, json.JSONDecodeError):
        return {"humidity": None, "pressure": None, "temp": None, "airquality": None, "daynight": None}

def save_last_data(humidity, pressure, temp, airquality, daynight):
    with open("last_data.json", "w") as file:
        json.dump({"humidity": humidity,
                   "pressure": pressure,
                   "temp": temp,
                   "airquality": airquality,
                   "daynight": daynight}, file)

def data_measurement():
    last_data = load_last_data()
    data_changed = False

    temp, pres, humi = Sensor_Read.ReadTempSensor()
    LDR_DATA, _, _, MQ135_PPM = Sensor_Read.ReadAirSensor()  

    # Check if any sensor data is None
    if temp is None or pres is None or humi is None or LDR_DATA is None or MQ135_PPM is None:
        print("Error: Sensor data is None. Skipping update.")
        return
    
    if last_data['temp'] is None or temp != last_data['temp']:
        API_Request.send_temp(f"{temp:.2f}")
        data_changed = True
        print("Temp Updated")

    if last_data['pressure'] is None or pres != last_data['pressure']:
        API_Request.send_pressure(f"{pres:.2f}")
        data_changed= True
        print("Pressure Updated")

    if last_data['humidity'] is None or humi != last_data['humidity']:
        API_Request.send_humidity(humi)
        data_changed = True
        print("Humidity Updated")

    if last_data['airquality'] is None or MQ135_PPM != last_data['airquality']:
        API_Request.send_airquality(f"{MQ135_PPM:.4f}")
        data_changed = True
        print("Air Quality Updated")

    if last_data['daynight'] is None or LDR_DATA != last_data['daynight']:
        API_Request.send_daynight(LDR_DATA)
        data_changed = True
        print("DayNight Updated")

    if data_changed:
        save_last_data(humi, pres, temp, MQ135_PPM, LDR_DATA)

def main_loop():
    try:
        while True:
            data_measurement()
            time.sleep(1)
    except KeyboardInterrupt:
        print("Messung gestoppt.")
    except Exception as e:
        print(f"Übertragung Fehlgeschlagen! Fehler: {e}")

main_loop()
