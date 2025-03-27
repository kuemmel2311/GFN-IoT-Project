import requests
import config


class API_Request:

    def Statuscode(code):
        messages = {
            200: "Übertragung erfolgreich!",
            403: "Falscher Authentifizierungscode!",
            404: "Seite wurde nicht gefunden!",
            500: "HTTP Fehler: Interner Serverfehler!"
        }
        print(messages.get(code, f"Statuscode: {code}"))

    def send_data(endpoint, data):
        try:
            dataValue = {"dataValue": data}
            headers = {
                "APIKey": config.API_SEND_DATA.auth_token,
                "Content-Type": "application/json"
            }
            response = requests.post(endpoint, json=dataValue, headers=headers)
            API_Request.Statuscode(response.status_code)
        except requests.exceptions.RequestException as e:
            print(f"Request error: {e}")

    def send_humidity(data):
        API_Request.send_data(config.Client.SEND_HUMIDITY_DATA, data)

    def send_pressure(data):
        API_Request.send_data(config.Client.SEND_PRESSURE_DATA, data)

    def send_temp(data):
        API_Request.send_data(config.Client.SEND_TEMP_DATA, data)

    def send_airquality(data):
        API_Request.send_data(config.Client.SEND_AIRQUALITY_DATA, data)

    def send_daynight(data):
        API_Request.send_data(config.Client.SEND_DAYNIGHT_DATA, data)
