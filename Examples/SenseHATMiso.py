"""
A simple monitoring station based on the Sense HAT
"""
import sys
from Miso.Stations.SenseHATStation import SenseHATStation

if len(sys.argv) < 2:
    print("Please provide a keyword")
    exit(1)

keyword = sys.argv[1]

# Create the station
station = SenseHATStation('Living Room',
                          "/home/pi/Projects/test.db",
                          '/var/www/html/test.html')

# Execute the requested action
if keyword == "init":
    station.CreateDatabase()
elif keyword == "dumpSensorValues":
    station.DumpSensorValues()
elif keyword == "generateCharts":
    station.GenerateCharts()
else:
    print("Error: unknown keyword %s"%keyword)
