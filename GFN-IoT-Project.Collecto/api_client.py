
import requests     # Zur Kommunikation mit der API
import json         # JavaScript Object Notation --> für Datenaustausch
import datetime     # Format fuer Datum & Zeit

class API_Request:

    def Feuchtigkeit(data):
        url = # API Adresse einfuegen
        data = {"dateAndTime": {},  "dataValue": 0}   # Sensordaten die gesendet werden sollen --> Feuchtigkeit

        response = requests.post(url..., json=data) # Befehl zum Senden an die API

        print(response.json())


    def Luftdruck(data):
        url = # API Adresse einfuegen
        data ={"dateandtime": {}, "dataValue": 0}   # Sensordaten die gesendet werden sollen -->  Luftdruck

        response = requests.post(url..., json=data) # Befehl zum Senden an die API

        print(response.json())


    def Temperatur(data):
        url = # API Adresse einfuegen
        data = {"dateAndTime": {}, "dataValue": 0}  # Sensordaten die gesendet werden sollen --> Temperatur

        response = requests.post(url..., json=data) # Befehl zum Senden an die API

        print(response.json())


    def Luftqualitaet(data):
        url = # API Adresse einfuegen
        data = {"dateAndTime": {}, "dateValue": 0}  # Sensordaten die gesendet werden sollen --> Luftqualitaet

        response = requests.post(url..., json=data) # Befehl zum Senden an die API

        print(response.json())


    def Lichtsensor(data):

        url = # API Adresse einfuegen
        data = {"dateAndTime": {}, "dateValue": 0}  # Sensordaten die gesendet werden sollen --> Tag oder Nacht

        response = requests.post(url..., json=data) # Befehl zum Senden an die API

        print(response.json())