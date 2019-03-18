# <p class="myforecast-current-lrg">53&deg;F</p>
import requests, bs4

res = requests.get('http://forecast.weather.gov/MapClick.php?lat=40.84657741711521&lon=-73.99479746642913&site=all&smap=1#.VW6lmkYVX78')

try:
    res.raise_for_status()
except Exception as exc:
        print "Status is %s is:" % exc
        

exampleSoup = bs4.BeautifulSoup(res.text)

#elems = noStarchSoup.select('<p class="myforecast-current-lrg">.+?</p>')

elems_temp = exampleSoup.select('p')[4]
elems_cond = exampleSoup.select('p')[3]
elems_humidity = exampleSoup.select('td')[1]
elems_windspeed = exampleSoup.select('td')[3]
elems_barometer = exampleSoup.select('td')[5]
elems_dewpoint = exampleSoup.select('td')[7]
elems_visibility = exampleSoup.select('td')[9]
elems_windchill = exampleSoup.select('td')[11]
elems_lastupdate = exampleSoup.select('td')[13]


##print elems
##print type(elems)

##print len(elems)
###print type(elems[0])
print "The current temperature in 07650 is %s" % elems_temp.getText()
print "The current condition is %s" % elems_cond.getText()
print "The current wind speed is %s" % elems_windspeed.getText()
print "The barometer reading is %s" % elems_barometer.getText()
print "The dew point is %s" % elems_dewpoint.getText()
print "Visibility is %s" % elems_visibility.getText()
print "Wind chill is %s" % elems_windchill.getText()
print "The last update was on %s" % elems_lastupdate.getText()

##
########print str(elems_temp)
########print str(elems_cond)
########print str(elems_humidity)
########print str(elems_windspeed)
########print str(elems_barometer)
########print str(elems_dewpoint)
########print str(elems_visibility)
########print str(elems_lastupdate)

##print elems[0].attrs



