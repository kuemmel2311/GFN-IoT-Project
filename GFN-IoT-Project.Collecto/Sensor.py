import time
from smbus import SMBus
from bme280 import BME280 
import serial
import json

class Read-Sensoren:
    def temperaturSensor()
        bus = SMBus(1)  # Use 1 for Raspberry Pi 4 I2C bus
        sensor = BME280(i2c_dev=bus)
    
        temperature = sensor.get_temperature()
        pressure = sensor.get_pressure()
        humidity = sensor.get_humidity()

        return temperature,,pressure, humidity

    def airSensor():
        arduino = serial.Serial("COM6", 9600, timeout=1)
        time.sleep(2)  # Wait for connection 
        try:
            data = arduino.readline().decode().strip()  # Read line
            if data:
                try:
                    sensor_data = json.loads(data)  # Parse JSON
                    LDR_DATA = sensor_data['LDR_RAW']
                except json.JSONDecodeError:
                    print("Invalid JSON received:", data)
        except KeyboardInterrupt:
            print("Exiting...")

