import serial
import json
import time
from smbus import SMBus
from bme280 import BME280 
from  config import Sensor

class Sensor_Read:

    def ReadTempSensor():
        bus = SMBus(1)  # Use 1 for Raspberry Pi 4 I2C bus
        sensor = BME280(i2c_dev=bus)
        try:   
            temperature = sensor.get_temperature()
            pressure = sensor.get_pressure()
            humidity = sensor.get_humidity()
            return temperature, pressure, humidity
        except (IOError, ValueError) as e:
            print(f"Error reading temperature sensor: {e}")
            return None, None, None  # Return None for all values if there's an error

    def ReadAirSensor():
        LDR_DATA, MQ135_RAW, MQ135_R0, MQ135_PPM = None, None, None, None
        arduino = None
        try:
            arduino = serial.Serial(Sensor.ArduinoPort, 9600, timeout=1)  # Open serial port
            time.sleep(2)
            data = arduino.readline().decode().strip()  # Read line
            if data:
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
            # Ensure the connection is closed
            if arduino is not None and arduino.is_open:
                arduino.close()
        return LDR_DATA, MQ135_RAW, MQ135_R0, MQ135_PPM
    


