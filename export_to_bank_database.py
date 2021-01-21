# -*- coding: utf-8 -*-
"""
Created on Tue Jan 19 22:19:37 2021

@author: Julia Issajeva
"""


import mysql.connector
import import_XML
#import_JSON
import traceback

database_connection_info = ["root", "swan0000", "127.0.0.1", "bank"]

def format_record(record):
    s = "("
    i = 0
    for element in record.values():
        if i !=0:
            s +=", "
        if type(element) == str:
            s += "\"" + element + "\""
        else:
            s += str(element)
        i += 1
    s += ")"
    return s

def export_data(cursor):
    try:
        data = import_XML.import_XML(import_XML.sitename)
        #data = import_JSON.import_JSON(import_JSON.sitename)
        import_XML.transform_XML(data)
        #import_JSON.transform_JSON(data)
    except:
        print("Failed to import data from site", file=sys.stderr)
        quit()
    for d in data:
        cur.execute('INSERT INTO currency_rates (short_name, name, rate, date) VALUES ' 
                + format_record(d) + ' ON DUPLICATE KEY UPDATE rate = ' + str(d['rate']) + ', date = \"' + d['date'] + '\"')

try:
    conn = mysql.connector.connect(user = database_connection_info[0], 
                               password = database_connection_info[1], 
                               host = database_connection_info[2], 
                               database = database_connection_info[3])
except:
    print("Failed to connect to the database", file=sys.stderr)
    quit()
       
cur = conn.cursor()

try:
    export_data(cur)
    conn.commit()
except Exception:
    traceback.print_exc()

conn.close()