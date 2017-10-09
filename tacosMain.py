from jsonOrder import *
from saveOrder import *
from statistics import *

##### MAIN #####

# Read from SQS and save all orders to orders.json
saveOrder();

# Read orders.json and create a list with all orders as json objects (dictionaries)
listaOrdenes = readOrdersFile()

# Print a table of the current orders and their details
printTable(listaOrdenes)

# (UNDER DEVELOPMENT) Graph different aspects of the current orders
