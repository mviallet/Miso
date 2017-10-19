"""
Provide an interface with sensors on the Sense HAT
"""
from Miso.Sensors.Sensor import Sensor
import sense_hat

class SenseHATSensors(object):
    """
    Provides an interface with the SenseHAT sensors
    """

    def __init__(self, location):

        self.location = location
        self.sensehat = sense_hat.SenseHat()
        
    def PressureSensor(self):
        """
        Interface with the sensehat pressure sensor
        """
        return Sensor({'name':'pressure', 'unit':'hPa', 'type':'NUMERIC', 'location':self.location}, self.sensehat.get_pressure)

    def TemperatureSensor(self):
        """
        Interface with the sensehat temperature sensor
        """
        return Sensor({'name':'temperature', 'unit':'Celsus', 'type':'NUMERIC', 'location':self.location}, self.sensehat.get_temperature)
    
    def HumiditySensor(self):
        """
        Interace with the sensehat humidity sensor
        """
        return Sensor({'name':'humidity', 'unit':'%', 'type':'NUMERIC', 'location':self.location}, self.sensehat.get_humidity)
