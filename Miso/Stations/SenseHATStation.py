"""
Create a station based on the sensehat
"""
from socket import gethostname
from Miso.Sensors.SenseHAT import SenseHATSensors
from Miso.Databases.DBInterface import DBInterface
from Miso.Stations.BasicStation import BasicStation

class SenseHATStation(BasicStation):
    
    def __init__(self, location, database, webpage):
                
        # Create the list of sensors
        sensors = SenseHATSensors(location)        

        # interface to the sense hat
        self.sensehat = sensors.sensehat
        
        sensors_list = [sensors.TemperatureSensor(), sensors.PressureSensor(), sensors.HumiditySensor()]

        # Call the BasicStation constructor
        super().__init__(sensors_list, location, database, webpage, 'SenseHATStation')

    def DumpSensorValues(self):

        super().DumpSensorValues()

        # Write that everything went well
        self.sensehat.show_message("DB Written", scroll_speed=0.1, text_colour = [255, 255, 255])
        self.sensehat.clear()

    def GenerateCharts(self):

        super().GenerateCharts()
        
        # Write that everything went well
        self.sensehat.show_message("Webpage updated", scroll_speed=0.1, text_colour = [0, 255, 0])
        self.sensehat.clear()
        
