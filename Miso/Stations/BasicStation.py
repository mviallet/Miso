"""
Basic environmental monitoring station
"""
from socket import gethostname
from datetime import datetime
import pytz
from tzlocal import get_localzone
from Miso.Charts.PlotlyCharts import GenerateOfflineChart, GenerateOnlineChart, HTMLTemplate
from Miso.Databases.DBInterface import DBInterface

class BasicStation(object):
    """
    Main class for environment monitoring
    - Establish connection with the database
    - Read the sensors
    - Commit readings to the database
    - Generate Charts
    """

    def __init__(self, sensors, location, database, webpage, name='BasicStation'):

        # webpage
        self.webpage = webpage
        
        # Location of the station
        self.location = location

        # Get station timezone
        self.timezone = get_localzone()

        # Name of the database
        self.database = database

        # Name of the station
        self.name = name

        # Name of the host
        self.hostname = gethostname()

        # Initialise sensor list
        self.sensors = sensors

        self.field_names = ['today', 'timeofday'] + [sensor.info["name"] for sensor in self.sensors] + ['location', 'device']
        self.field_types = ['DATE', 'TIME'] + [sensor.info["type"] for sensor in self.sensors] + ['TEXT']*2

    def DumpSensorValues(self):

        # Get the values of all sensors
        values = [round(sensor.GetMeasure(), 2) for sensor in self.sensors]

        # Connect to the database
        db = DBInterface(self.database)

        # Write the data
        db.Execute("INSERT INTO %s VALUES(date('now'), time('now'), ?, ?, ?, ?, ?)"%self.name, values + [self.location, self.hostname])

        # Commit the changes and close
        db.Commit()
        db.Close()

    def CreateDatabase(self):

        db = DBInterface(self.database)

        db.Execute("CREATE TABLE %s (%s %s, %s %s, %s %s, %s %s, %s %s, %s %s, %s %s);"% 
                   tuple([self.name] + [item for i in zip(self.field_names, self.field_types) for item in i]))

        db.Commit()
        db.Close()

    def GenerateCharts(self):
        """
        Generate charts
        """

        # Read values from database
        db = DBInterface(self.database)
        results = db.Execute("SELECT today, timeofday, pressure, temperature, humidity FROM %s;"%self.name)

        date = []
        pressure = []
        temperature = []
        humidity = []
        for today, time, pre, temp, hum in results:
            date.append( datetime.strptime("%s %s" %(today, time), '%Y-%m-%d %H:%M:%S').replace(tzinfo=pytz.utc).astimezone(self.timezone) )
            pressure.append(pre)
            temperature.append(temp)
            humidity.append(hum)

        # Generate plots
        pressureGraph = GenerateOfflineChart(date, pressure, "Pressure", "hPa")
        temperatureGraph = GenerateOfflineChart(date, temperature, "Temperature", "Celsus")
        humidityGraph = GenerateOfflineChart(date, humidity, "Humidity", "%")

        #pressureOnlineGraph = GenerateOnlineChart

        #
        # Create the HTML page
        #
        subPage = """
        %s
        %s
        %s
        """ % (pressureGraph, temperatureGraph, humidityGraph)

        # DOM
        body = HTMLTemplate(self.hostname, subPage)

        index = open(self.webpage, 'w')
        index.writelines(body)
        index.close()
