import time
from smbus import SMBus
from bme280 import BME280  # Importing the BME280 class from the bme280 library

# Initialise the I2C bus
bus = SMBus(1)  # Use 1 for Raspberry Pi 4 I2C bus
sensor = BME280(i2c_dev=bus)  # Create an instance of BME280

# Discard the first reading to avoid garbage data
temperature = sensor.get_temperature()
pressure = sensor.get_pressure()
humidity = sensor.get_humidity()

# Delay before starting the main loop to allow sensor to stabilize
time.sleep(1)

while True:
    # Read the sensor values
    temperature = sensor.get_temperature()
    pressure = sensor.get_pressure()
    humidity = sensor.get_humidity()

    # Print the readings
    print('{:05.2f}*C {:05.2f}hPa {:05.2f}%'.format(temperature, pressure, humidity))

    # Delay between readings (1 second)
    time.sleep(1)