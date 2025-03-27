import serial
import json
import time

# Set correct COM port (check in Arduino IDE)
arduino = serial.Serial("/dev/ttyACM0", 9600, timeout=1)
time.sleep(2)  # Wait for connection

while True:
    try:
        data = arduino.readline().decode().strip()  # Read line
        if data:
            try:
                sensor_data = json.loads(data)  # Parse JSON
                print(f"LDR: {sensor_data['LDR_RAW']} | MQ135 Raw: {sensor_data['MQ135_RAW']} | MQ135 ppm: {sensor_data['MQ135_PPM']}")
            except json.JSONDecodeError:
                print("Invalid JSON received:", data)
    except KeyboardInterrupt:
        print("Exiting...")
        break