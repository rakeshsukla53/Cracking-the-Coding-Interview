__author__ = 'rakesh'

import urllib2
import json

house = raw_input("Enter the house number")
street = raw_input("Enter the street number")
borough = raw_input("Enter the borough")

fullAddress = 'https://api.cityofnewyork.us/geoclient/v1/address.json?houseNumber=' + str(house) + '&street=' + str(street) + '&borough=' + str(borough) + '&app_id=e7df1765&app_key=bb80a97381a0fa916bb860768fa71b8f'

a = urllib2.urlopen(fullAddress)

location = json.load(a)['address']

latitude = location['latitude']
longitude = location['longitude']

communityDistrict = location['communityDistrict']

bbl = location['bbl']

print " "
print " "

print "latitude = %s\nlongitude = %s\nDistrict = %s\nBBL = %s" % (latitude, longitude, communityDistrict, bbl)

























