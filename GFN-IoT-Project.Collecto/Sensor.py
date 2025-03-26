import serial 

class Sensor_Luftqualität:
    def__init__(self, port, baudrate=9600,) 

    self.port = port
    self.baudrate = baudrate 

    try:
        self.serial_conn = serial.Serial(port, baudrate)
        print(f"Verbindung zu {port} hergestellt.")

    except Exception as e :
        print(f"Fehler beim Verbindung mit {port}: {e}")

    def lese_daten(self):
        if self.serial_conn.is_open:
            try:
                daten = self.serial_conn.readline().decode('utf-8').strip()
                return daten
            except Exception as e:
                print(f"Fehler beim lesen der Daten: {e}")
                return None
        
        else:
            print("Serielle Verbindung nicht geöffnet.")
            return None
        
    
class Sensoren:
    def__init__(self, Temperatur, Luftfeuchtigkeit, Luftdruck, Tag-Nacht-Zeit)
    self.Temperatur = Temperatur
    self.Luftfeuchtigkeit = Luftfeuchtigkeit
    self.Luftdruck = Luftdruck
    self.Tag-Nacht-Zeit = Tag-Nacht-Zeit

    def info(self)
        return f"{self.Temperatur}{ self.Luftfeuchtigkeit}{self.Luftdruck}{ self.Tag-Nacht-Zeit}"
    

main 



