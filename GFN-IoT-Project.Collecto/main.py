import time
import json
from api_client import API_Request
from sensor_client import Sensor_Read

LAST_DATA_FILE = "last_data.json"

def load_last_data() -> dict:
    try:
        with open(LAST_DATA_FILE, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {"humidity": None, "pressure": None, "temp": None, "airquality": None, "daynight": None}

def save_last_data(humidity: float, pressure: float, temp: float, airquality: float, daynight: int) -> None:
    with open(LAST_DATA_FILE, "w") as file:
        json.dump({
            "humidity": humidity,
            "pressure": pressure,
            "temp": temp,
            "airquality": airquality,
            "daynight": daynight
        }, file)

def data_measurement() -> None:
    last_data = load_last_data()

    temp, pres, humi = Sensor_Read.ReadTempSensor()
    LDR_DATA, _, _, MQ135_PPM = Sensor_Read.ReadAirSenor()

    updated_values = {
        "temp": (temp, f"{temp:.2f}"),
        "pressure": (pres, f"{pres:.2f}"),
        "humidity": (humi, humi),
        "airquality": (MQ135_PPM, f"{MQ135_PPM:.4f}"),
        "daynight": (LDR_DATA, LDR_DATA),
    }

    # Send updates only if values have changed
    data_changed = False
    for key, (current_value, formatted_value) in updated_values.items():
        if current_value != last_data[key]:
            send_func = getattr(API_Request, f"send_{key}", None)
            if send_func:
                send_func(formatted_value)
            data_changed = True

    if data_changed:
        save_last_data(humi, pres, temp, MQ135_PPM, LDR_DATA)

def main_loop() -> None:
    try:
        while True:
            data_measurement()
    except Exception as e:
        print(f"Übertragung Fehlgeschlagen! Fehler: {e}")

data_measurement()