from jsonOrder import *
from saveOrder import *
from statistics import *

##### MAIN #####

# Read from SQS and store the json strings in a list
listaOrdenes = readSQS();

# Read orders.json and create a list with all orders as json objects (dictionaries)
#listaOrdenes = readOrdersFile()

# Print a table of the current orders and their details
printTable(listaOrdenes)

# Graph different aspects of the current orders
tipos = obtainTacosByType(listaOrdenes)
carnes = obtainTacosByMeat(listaOrdenes)

graphTacosByType(tipos)
graphTacosByMeat(carnes)
