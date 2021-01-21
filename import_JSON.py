# -*- coding: utf-8 -*-
"""
Created on Tue Jan 19 19:11:56 2021

@author: Julia Issajeva
"""

import json

sitename = "https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?json"

def import_JSON(sitename):
    jstring = ""
    fhand = urllib.request.urlopen(sitename)
    for line in fhand:
        jstring += line.decode()
    return json.loads(jstring)

def transform_JSON(jlist):
    for d in jlist:
        d.pop('r030')
        d['short_name'] = d.pop('cc')
        d['name'] = d.pop('txt')
        date = d.pop('exchangedate').split('.')
        d['date'] = date[2] + '-' + date[1] + '-' + date[0]
        