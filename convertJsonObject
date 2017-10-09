import json
import os
from Orden import *

FILENAME = os.getcwd() + "\\orders.json"
jsonSampleString = '{"datetime": "2017-01-01 23:23:23", "request_id": "123-123-123", "orden": [{"part_id": "123-111","type": "taco","meat": "asada","quantity": 3,"ingredients": ["cebolla","salsa"]},{"part_id": "123-222","type": "mulita","meat": "asada","quantity": 1,"ingredients": [  ]}]}'

##
## Function that converts a json string to an Orden object
##

def crearOrden(jsonInputString):
    jsonObject = json.loads(jsonInputString)
    listaOrdenes = jsonObject["orden"]
    listaSubordenes = []
    for orden in listaOrdenes:
        s = subOrden(orden["part_id"], orden["type"],orden["meat"], orden["quantity"], orden["ingredients"])
        listSubordenes.append(s)
    return Orden(jsonObject["datetime"], jsonObject["request_id"],listaSubordenes)

##
## Function that converts an Orden object to a json string (Under develompent)
##

def serializeOrder(ordenObject):
    pass

##
## Function that reads all lines of a text file, traducing them to json strings
## and creating Orden objects 
##
def readOrdersFile(fileName):
    with open(fileName, 'r') as f:
        listaOrdenes = []
        while True:
            line = f.readline()
            if line != '':
                newOrder = crearOrden(line[:-1]) #Remove breaklines
                listaOrdenes.append(newOrder)
            else:
                break
        return listaOrdenes

###MAIN#####
listaOrdenes = readOrdersFile(FILENAME)
