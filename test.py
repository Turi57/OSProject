from jsonOrder import *
from saveOrder import *
from statistics import *

##### MAIN #####

# Read from orders.json and store the json strings in a list
listaOrdenes = readOrdersFile;

# Print a table of the current orders and their details
printTable(listaOrdenes)

# Graph different aspects of the current orders
tipos = obtainTacosByType(listaOrdenes)
carnes = obtainTacosByMeat(listaOrdenes)

graphTacosByType(tipos)
graphTacosByMeat(carnes)

#Wait to see the graphs
input("")
