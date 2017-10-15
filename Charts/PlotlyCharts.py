"""
Define some functions to create charts using plotly
"""
import plotly
from plotly.graph_objs import Scatter, Layout
from datetime import datetime

def GenerateOfflineChart(dates, values, field_name, units):
    """
    Generate plot
    """
    return plotly.offline.plot({"data": [Scatter(x=dates, y=values)],
                                "layout": Layout(title=field_name, height=450, yaxis=dict(title=units))},
                               output_type='div', filename=field_name+'.html',
                               #image_height = 450, image_width = 200,
                               include_plotlyjs=False)


def GenerateOnlineChart(dates, values, field_name, units):
    """
    Generate an online chat
    """

    return plotly.plotly.plot({"data": [Scatter(x=dates, y=values, name=field_name),
                                        Scatter(x=date, y=temperature, name='temperature'),
                                        Scatter(x=date, y=humidity, name = 'humidity')]},
                              filename='pressure', fileopt='overwrite', auto_open=False)


def HTMLTemplate(hostname, subPage):
    """
    Returns the template for the HTML page
    """
    return """
<html>
<head>
<script src="plotly-latest.min.js"></script>
<title>%s</title> 
<style>    
   body {         
      width: 1024px;         
      margin: 0 auto;         
      font-family: Tahoma, Verdana, Arial, sans-serif;     
      } 
</style> 
</head>
<body>
<h1> Sensors values </h1>
<p> Last update: %s </p>
%s
</body>
</html>
""" % (hostname, datetime.now().strftime("%d-%m-%Y %H:%M:%S"), subPage)
