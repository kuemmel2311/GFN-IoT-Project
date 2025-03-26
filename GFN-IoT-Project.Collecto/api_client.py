
import requests     # Zur Kommunikation mit der API
import config       # Einfuegen der config-Datei


class API_Request:

    def Statuscode(code):
        if code == 200:
            print("Übertragung erfolgreich!")
        elif code == 403:
            print("Falscher Authentifizierungscode!")
        elif code == 404:
            print("Seite wurde nicht gefunden!")
        elif code == 500:
            print("HTTP Fehler: Interner Serverfehler!")
        else:
            print(f"Statuscode: {code}")    


    def send_humidity(data):
        try:

            dataValue = {"dataValue": data}                                                             # Sensordaten die gesendet werden sollen --> Feuchtigkeit

            headers = {"APIKey": config.API_SEND_DATA.auth_token,                                       # Authentifizierung nötig zur Eingabe von Daten
                    "Content-Type": "application/json"}
        
            response = requests.post(config.Client.SEND_HUMIDITY_DATA, json=dataValue, headers=headers) # Befehl zum Senden an die API
                                                                                                        
            API_Request.Statuscode(response.status_code)
        except requests.exceptions.RequestException as e:
            API_Request.Statuscode(e.response.status_code)


    def send_pressure(data):
        try:

            dataValue = {"dataValue": data}                                                             # Sensordaten die gesendet werden sollen -->  Luftdruck
        
            headers = {"APIKey": config.API_SEND_DATA.auth_token,                                       # Authentifizierung nötig zur Eingabe von Daten
                   "Content-Type": "application/json"}
        
            response = requests.post(config.Client.SEND_PRESSURE_DATA, json=dataValue, headers=headers) # Befehl zum Senden an die API
        
            API_Request.Statuscode(response.status_code)
        except requests.exceptions.RequestException as e:
            API_Request.Statuscode(e.response.status_code)

    def send_temp(data):
        try:

            dataValue = {"dataValue": data}                                                             # Sensordaten die gesendet werden sollen --> Temperatur

            headers = {"APIKey": config.API_SEND_DATA.auth_token,                                       # Authentifizierung nötig zur Eingabe von Daten
                   "Content-Type": "application/json"}
        
            response = requests.post(config.Client.SEND_TEMP_DATA, json=dataValue, headers=headers)     # Befehl zum Senden an die API

            API_Request.Statuscode(response.status_code)
        except requests.exceptions.RequestException as e:
            API_Request.Statuscode(e.response.status_code)

    def send_airquality(data):
        try:
            dataValue = {"dataValue": data}                                                             # Sensordaten die gesendet werden sollen --> Luftqualitaet

            headers = {"APIKey": config.API_SEND_DATA.auth_token,                                       # Authentifizierung nötig zur Eingabe von Daten
                   "Content-Type": "application/json"}
        
            response = requests.post(config.Client.SEND_AIRQUALITY_DATA, json=dataValue, headers=headers) # Befehl zum Senden an die API

            API_Request.Statuscode(response.status_code)
        except requests.exceptions.RequestException as e:
            API_Request.Statuscode(e.response.status_code)


    def send_daynight(data):
        try:

            dataValue = {"dataValue": data}                                                             # Sensordaten die gesendet werden sollen --> Tag oder Nacht

            headers = {"APIKey": config.API_SEND_DATA.auth_token,                                       # Authentifizierung nötig zur Eingabe von Daten
                   "Content-Type": "application/json"}
        
            response = requests.post(config.Client.SEND_DAYNIGHT_DATA, json=dataValue, headers=headers) # Befehl zum Senden an die API

            API_Request.Statuscode(response.status_code)
        except requests.exceptions.RequestException as e:
            API_Request.Statuscode(e.response.status_code)