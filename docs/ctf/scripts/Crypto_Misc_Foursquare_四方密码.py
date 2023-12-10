#!/bin/python2

from pycipher import Foursquare
 
fs = Foursquare('zgptfoihmuwdrcnykeqaxvsbl','mfnbdcrhsaxyogvituewlqzkp')
 
print fs.encipher('HELLOWORLD')
print fs.decipher('UNWXDKDECM')
