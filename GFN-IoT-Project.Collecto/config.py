class API_SEND_DATA:

    API_WEB_ADRESS = 'https://sws.aclab.tech/'
    auth_token = "d2f8a9c4-3b6e-4f91-a2f7-8e5d1b4a6c3e"

class Client:
        SEND_TEMP_DATA = f"{API_SEND_DATA.API_WEB_ADRESS}WeatherStationAPI/SendTempData"
        SEND_HUMIDITY_DATA = f"{API_SEND_DATA.API_WEB_ADRESS}WeatherStationAPI/SendHumidityData"
        SEND_PRESSURE_DATA = f"{API_SEND_DATA.API_WEB_ADRESS}WeatherStationAPI/SendPressureData"
        SEND_AIRQUALITY_DATA = f"{API_SEND_DATA.API_WEB_ADRESS}WeatherStationAPI/SendAirQualityData"
        SEND_DAYNIGHT_DATA = f"{API_SEND_DATA.API_WEB_ADRESS}WeatherStationAPI/SendDayNightData"

class Sensor :
      ArduinoPort = '/dev/ttyACM0'         