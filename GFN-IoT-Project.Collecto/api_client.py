
import requests     # Zur Kommunikation mit der API
import config


class API_Request:

    def Feuchtigkeit(data):
        data = {"dataValue": 0}                                 # Sensordaten die gesendet werden sollen --> Feuchtigkeit

        headers = {"APIKey": config.auth_token,              # Authentifizierung nötig zur Eingabe von Daten
                   "Content-Type": "application/json"
    }
        
        response = requests.post(config.URL.web, json=data, headers=headers)  # Befehl zum Senden an die API
        if response.status_code == 200:                         # Bei Code 200 war Übertragung erfolgreich
            print("Übertragung erfolgreich!")
            print(response.json())
        if response.status_code == 403:                         # Bei Code 403 wurde falsche Code eingegeben
            print("Falscher Authentifizierungscode!")
        else:
            print("Keine Verbindung zum Server!")               # Bei anderen Codes, gibt es Serverprobleme


    def Luftdruck(data):
        data ={"dataValue": 0}                                  # Sensordaten die gesendet werden sollen -->  Luftdruck
        
        headers = {"APIKey": config.auth_token,                 # Authentifizierung nötig zur Eingabe von Daten
                   "Content-Type": "application/json"
    }
        
        response = requests.post(config.URL.web, json=data, headers=headers)  # Befehl zum Senden an die API
        if response.status_code == 200:                         # Bei Code 200 war Übertragung erfolgreich
            print("Übertragung erfolgreich!")
            print(response.json())
        if response.status_code == 403:                         # Bei Code 403 wurde falsche Code eingegeben
            print("Falscher Authentifizierungscode!")
        else:
            print("Keine Verbindung zum Server!")               # Bei anderen Codes, gibt es Serverprobleme

    def Temperatur(data):
        data = {"dataValue": 0}                                 # Sensordaten die gesendet werden sollen --> Temperatur

        headers = {"APIKey": config.auth_token,                 # Authentifizierung nötig zur Eingabe von Daten
                   "Content-Type": "application/json"
    }
        
        response = requests.post(config.URL.web, json=data, headers=headers)  # Befehl zum Senden an die API
        if response.status_code == 200:                         # Bei Code 200 war Übertragung erfolgreich
            print("Übertragung erfolgreich!")
            print(response.json())
        if response.status_code == 403:                         # Bei Code 403 wurde falsche Code eingegeben
            print("Falscher Authentifizierungscode!")
        else:
            print("Keine Verbindung zum Server!")               # Bei anderen Codes, gibt es Serverprobleme

    def Luftqualitaet(data):
        data = {"dataValue": 0}                                 # Sensordaten die gesendet werden sollen --> Luftqualitaet

        headers = {"APIKey": config.auth_token,                 # Authentifizierung nötig zur Eingabe von Daten
                   "Content-Type": "application/json"
    }
        
        response = requests.post(config.URL.web, json=data, headers=headers)  # Befehl zum Senden an die API
        if response.status_code == 200:                         # Bei Code 200 war Übertragung erfolgreich
            print("Übertragung erfolgreich!")
            print(response.json())
        if response.status_code == 403:                         # Bei Code 403 wurde falsche Code eingegeben
            print("Falscher Authentifizierungscode!")
        else:
            print("Keine Verbindung zum Server!")               # Bei anderen Codes, gibt es Serverprobleme


    def Lichtsensor(data):
        data = {"dataValue": 0}                                 # Sensordaten die gesendet werden sollen --> Tag oder Nacht

        headers = {"APIKey": config.auth_token,                 # Authentifizierung nötig zur Eingabe von Daten
                   "Content-Type": "application/json"
    }
        
        response = requests.post(config.URL.web, json=data, headers=headers)  # Befehl zum Senden an die API
        if response.status_code == 200:                         # Bei Code 200 war Übertragung erfolgreich
            print("Übertragung erfolgreich!")
            print(response.json())
        if response.status_code == 403:                         # Bei Code 403 wurde falsche Code eingegeben
            print("Falscher Authentifizierungscode!")
        else:
            print("Keine Verbindung zum Server!")               # Bei anderen Codes, gibt es Serverprobleme