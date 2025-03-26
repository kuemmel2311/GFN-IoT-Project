
import requests     # Zur Kommunikation mit der API
import json         # JavaScript Object Notation --> für Datenaustausch
import datetime     # Format fuer Datum & Zeit
import config


class API_Request:

    def Feuchtigkeit(data):
        url = "UNSERE_API_URL"                                  # API Adresse einfuegen
        data = {"dataValue": 0}                                 # Sensordaten die gesendet werden sollen --> Feuchtigkeit

        headers = {"x-api-key": "{auth_token}",                 # Authentifizierung nötig zur Eingabe von Daten
                   "Content-Type": "application/json"
    }
        
        response = requests.post("UNSERE_API_URL", json=data,)  # Befehl zum Senden an die API
        if response.status_code == 200:                         # Bei Code 200 war Übertragung erfolgreich
            print("Übertragung erfolgreich!")
            print(response.json())
        if response.status_code == 403:                         # Bei Code 403 wurde falsche Code eingegeben
            print("Falscher Authentifizierungscode!")
        else:
            print("Keine Verbindung zum Server!")               # Bei anderen Codes, gibt es Serverprobleme


    def Luftdruck(data):
        url = "UNSERE_API_URL"                                  # API Adresse einfuegen
        data ={"dataValue": 0}                                  # Sensordaten die gesendet werden sollen -->  Luftdruck
        
        headers = {"x-api-key": "{auth_token}",                 # Authentifizierung nötig zur Eingabe von Daten
                   "Content-Type": "application/json"
    }
        
        response = requests.post("UNSERE_API_URL", json=data,)  # Befehl zum Senden an die API
        if response.status_code == 200:                         # Bei Code 200 war Übertragung erfolgreich
            print("Übertragung erfolgreich!")
            print(response.json())
        if response.status_code == 403:                         # Bei Code 403 wurde falsche Code eingegeben
            print("Falscher Authentifizierungscode!")
        else:
            print("Keine Verbindung zum Server!")               # Bei anderen Codes, gibt es Serverprobleme

    def Temperatur(data):
        url = "UNSERE_API_URL"                                  # API Adresse einfuegen
        data = {"dataValue": 0}                                 # Sensordaten die gesendet werden sollen --> Temperatur

        headers = {"x-api-key": "{auth_token}",                 # Authentifizierung nötig zur Eingabe von Daten
                   "Content-Type": "application/json"
    }
        
        response = requests.post("UNSERE_API_URL", json=data,)  # Befehl zum Senden an die API
        if response.status_code == 200:                         # Bei Code 200 war Übertragung erfolgreich
            print("Übertragung erfolgreich!")
            print(response.json())
        if response.status_code == 403:                         # Bei Code 403 wurde falsche Code eingegeben
            print("Falscher Authentifizierungscode!")
        else:
            print("Keine Verbindung zum Server!")               # Bei anderen Codes, gibt es Serverprobleme

    def Luftqualitaet(data):
        url = "UNSERE_API_URL"                                  # API Adresse einfuegen
        data = {"dateValue": 0}                                 # Sensordaten die gesendet werden sollen --> Luftqualitaet

        headers = {"x-api-key": "{auth_token}",                 # Authentifizierung nötig zur Eingabe von Daten
                   "Content-Type": "application/json"
    }
        
        response = requests.post("UNSERE_API_URL", json=data,)  # Befehl zum Senden an die API
        if response.status_code == 200:                         # Bei Code 200 war Übertragung erfolgreich
            print("Übertragung erfolgreich!")
            print(response.json())
        if response.status_code == 403:                         # Bei Code 403 wurde falsche Code eingegeben
            print("Falscher Authentifizierungscode!")
        else:
            print("Keine Verbindung zum Server!")               # Bei anderen Codes, gibt es Serverprobleme


    def Lichtsensor(data):

        url = "UNSERE_API_URL"                                  # API Adresse einfuegen
        data = {"dateValue": 0}                                 # Sensordaten die gesendet werden sollen --> Tag oder Nacht

        headers = {"x-api-key": "{auth_token}",                 # Authentifizierung nötig zur Eingabe von Daten
                   "Content-Type": "application/json"
    }
        
        response = requests.post("UNSERE_API_URL", json=data,)  # Befehl zum Senden an die API
        if response.status_code == 200:                         # Bei Code 200 war Übertragung erfolgreich
            print("Übertragung erfolgreich!")
            print(response.json())
        if response.status_code == 403:                         # Bei Code 403 wurde falsche Code eingegeben
            print("Falscher Authentifizierungscode!")
        else:
            print("Keine Verbindung zum Server!")               # Bei anderen Codes, gibt es Serverprobleme