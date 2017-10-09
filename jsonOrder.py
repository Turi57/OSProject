import json
import statistics

FILENAME = "orders.json"
jsonSampleString = '{"datetime": "2017-01-01 23:23:23", "request_id": "123-123-123", "orden": [{"part_id": "123-111","type": "taco","meat": "asada","quantity": 3,"ingredients": ["cebolla","salsa"]},{"part_id": "123-222","type": "mulita","meat": "asada","quantity": 1,"ingredients": [  ]}]}'

##
## Function that converts a json string to an Orden json Object
##

def parseJSON(jsonInputString):
    jsonObject = json.loads(jsonInputString)
    return jsonObject


##
## Function that reads all lines of a text file, converting them to json objects (dictionaries)
##
def readOrdersFile():
    with open(FILENAME, 'r') as f:
        listaOrdenes = []
        while True:
            line = f.readline()
            if line != '':
                newOrder = parseJSON(line[:-1]) #Remove breaklines
                listaOrdenes.append(newOrder)
            else:
                break
        return listaOrdenes

###MAIN#####
requestList = readOrdersFile()


statistics.printTable(requestList)

