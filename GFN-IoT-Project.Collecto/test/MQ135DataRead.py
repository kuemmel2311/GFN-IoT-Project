import serial
import time

# Set your correct COM port
arduino = serial.Serial("COM6", 9600, timeout=1)
time.sleep(2)  # Wait for connection

while True:
    try:
        data = arduino.readline().decode().strip()
        if data.isnumeric():
            light_value = int(data)
            print(f"Sensor Value: {light_value}")
    except KeyboardInterrupt:
        print("Exiting...")
        break