import time
from smbus import SMBus
from bme280 import BME280 
import serial
import json

class Read_Sensoren:
    def temperaturSensor():
        bus = SMBus(1)  # Use 1 for Raspberry Pi 4 I2C bus
        sensor = BME280(i2c_dev=bus)
        try:   
            temperature = sensor.get_temperature()
            pressure = sensor.get_pressure()
            humidity = sensor.get_humidity()
        except:
            print("Error")
        return temperature, pressure, humidity

    def airSensor():
        arduino = serial.Serial("COM6", 9600, timeout=1)
        time.sleep(2)  # Wait for connection 
        try:
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
        except KeyboardInterrupt:
            print("Exiting...")
        return LDR_DATA, MQ135_RAW, MQ135_R0, MQ135_PPM


