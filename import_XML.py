# -*- coding: utf-8 -*-
"""
Created on Tue Jan 19 22:17:17 2021

@author: Julia Issajeva
"""

import urllib
import xml.etree.ElementTree as ET

sitename = "https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange"


def import_XML(sitename):
    xstring = ""
    fhand = urllib.request.urlopen(sitename)
    for line in fhand:
        xstring += line.decode()
    tree = ET.fromstring(xstring)
    result = []
    for cur in tree.findall('currency'):
        currency = dict()
        currency['short_name'] = cur.find('cc').text
        currency['name'] = cur.find('txt').text
        currency['rate'] = cur.find('rate').text
        currency['date'] = cur.find('exchangedate').text
        result.append(currency)
    return result

def transform_XML(xlist):
    for d in xlist:
        d['rate'] = float(d['rate'])
        date = d['date'].split('.')
        d['date'] = date[2] + '-' + date[1] + '-' + date[0]
    