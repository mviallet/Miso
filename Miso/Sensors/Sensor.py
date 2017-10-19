"""
Defines the sensor class
"""

class Sensor(object):
    """
    An abstract class that describes a sensor
    """

    def __init__(self, info, measure):
        self.info = info
        self.measure = measure

    def GetMeasure(self):
        return self.measure()
