import serial
import json
import time
from smbus import SMBus
from bme280 import BME280 
from config import Sensor  # Ensure this file has Sensor.ArduinoPort defined

class Sensor_Read:
    
    @staticmethod
    def ReadTempSensor():
        try:
            bus = SMBus(1)  # Use I2C bus 1 for Raspberry Pi
            sensor = BME280(i2c_dev=bus)

            temperature = sensor.get_temperature()
            pressure = sensor.get_pressure()
            humidity = sensor.get_humidity()
            
            return temperature, pressure, humidity

        except Exception as e:
            print(f"Error reading BME280 sensor: {e}")
            return None, None, None  # Ensure function always returns 3 values

    @staticmethod
    def ReadAirSensor():
        LDR_DATA = MQ135_RAW = MQ135_R0 = MQ135_PPM = None  # Default values

        try:
            with serial.Serial(Sensor.ArduinoPort, 9600, timeout=1) as arduino:
                time.sleep(2)  # Wait for connection
                data = arduino.readline().decode().strip()  # Read line from Arduino
                
                if data:
                    try:
                        sensor_data = json.loads(data)  # Parse JSON
                        LDR_DATA = sensor_data.get('LDR_RAW', 0)
                        MQ135_RAW = sensor_data.get('MQ135_RAW', 0)
                        MQ135_R0 = sensor_data.get('MQ135_R0', 0)
                        MQ135_PPM = sensor_data.get('MQ135_PPM', 0)
                    except json.JSONDecodeError:
                        print(f"Invalid JSON received: {data}")
        
        except serial.SerialException as e:
            print(f"Serial connection error: {e}")
        except Exception as e:
            print(f"Unexpected error reading air sensor: {e}")

        return LDR_DATA, MQ135_RAW, MQ135_R0, MQ135_PPM  # Always return values

