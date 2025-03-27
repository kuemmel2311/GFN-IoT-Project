import time
import json
import serial
import json
import time
from  config import Sensor
from api_client import API_Request
from sensor_client import Sensor_Read
import os

arduino = serial.Serial("/dev/ttyACM0", 9600, timeout=1)  # Open serial port
time.sleep(2)

def ReadAirSensor():
    LDR_DATA, MQ135_RAW, MQ135_R0, MQ135_PPM = None, None, None, None
    try:     
        data = arduino.readline().decode().strip() # Read line
        try:
            sensor_data = json.loads(data)  # Parse JSON
            LDR_DATA = sensor_data['LDR_RAW']
            MQ135_RAW = sensor_data['MQ135_RAW']
            MQ135_R0 = sensor_data['MQ135_R0']
            MQ135_PPM = sensor_data['MQ135_PPM']
        except json.JSONDecodeError:
            print("Invalid JSON received:", data)             
    except serial.SerialException as e:
            print(f"Error reading from Arduino: {e}")
    finally:
        return LDR_DATA, MQ135_RAW, MQ135_R0, MQ135_PPM

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
    LDR_DATA, _, _, MQ135_PPM = ReadAirSensor()

    # Check if any sensor data is None
    if temp is None or pres is None or humi is None or LDR_DATA is None or MQ135_PPM is None:
        print("Error: Sensor data is None. Skipping update.")
        print(f"Temp {temp}, Pres {pres} humi {humi} LDR {LDR_DATA}, PPM: {MQ135_PPM}")
        return
    
    if  LDR_DATA != last_data['daynight']:
        API_Request.send_daynight(LDR_DATA)
        data_changed = True
        print("DayNight Updated")

    if temp != last_data['temp']:
        API_Request.send_temp(temp)
        data_changed = True
        print("Temp Updated")

    if  pres != last_data['pressure']:
        API_Request.send_pressure(pres)
        data_changed= True
        print("Pressure Updated")

    if  humi != last_data['humidity']:
        API_Request.send_humidity(humi)
        data_changed = True
        print("Humidity Updated")

    if  MQ135_PPM != last_data['airquality']:
        API_Request.send_airquality(MQ135_PPM)
        data_changed = True
        print("Air Quality Updated")

    if data_changed:
        save_last_data(humi, pres, temp, MQ135_PPM, LDR_DATA)

def main_loop():
    try:
        os.remove("last_data.json")
    except:
        print("")
    try:
        while True:
            data_measurement()
            time.sleep(1)
    except KeyboardInterrupt:
        print("Messung gestoppt.")
    except Exception as e:
        print(f"Übertragung Fehlgeschlagen! Fehler: {e}")

main_loop()
