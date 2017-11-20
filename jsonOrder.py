import json
import statistics

FILENAME = "orders.json"
jsonSampleString = '{"datetime": "2017-01-01 23:23:23", "request_id": "123-123-123", "orden": [{"part_id": "123-111","type": "taco","meat": "asada","quantity": 3,"ingredients": ["cebolla","salsa"]},{"part_id": "123-222","type": "mulita","meat": "asada","quantity": 1,"ingredients": [  ]}]}'

##
## Function that reads all lines of a text file, converting them to json objects (dictionaries)
##
def readOrdersFile():
    with open(FILENAME, 'r') as f:
        listaOrdenes = []
        while True:
            line = f.readline()
            if line != '':
                newOrder = json.loads(line[:-1]) #Remove breaklines
                listaOrdenes.append(newOrder)
            else:
                break
        return listaOrdenes
    
"""Function that receives the string from SQS parsed to JSON object, and will add the answer's attributes """
def initializeResponse(inputJSON):
    pass

"""Function that receives a response JSON object, a string that describes the step´s state and
another one that describes the action done."""
def addStepToAnswer(responseJSON, stateString, actionString):
    pass

"""Function that sets the start and end attributes of the response JSON object to specified parameters"""
def setOrderTimes(responseJOSN, start, end):
    pass
    

