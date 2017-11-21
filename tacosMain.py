from jsonOrder import *
from SQS import *
from statistics import *
from taqueria import *
from threading import Thread

##### MAIN #####

# Read from SQS and store the json strings in a list
listaOrdenes = []
listaOrdenes.extend(readSQS())

# Read orders.json and create a list with all orders as json objects (dictionaries)
# listaOrdenes2 = readOrdersFile()

print(listaOrdenes)
# print(listaOrdenes2)
# Print a table of the current orders and their details
printTable(listaOrdenes)

# Graph different aspects of the current orders
tipos = obtainTacosByType(listaOrdenes)
carnes = obtainTacosByMeat(listaOrdenes)

graphTacos(tipos, "Tipos")
graphTacos(carnes, "Carnes")

t1 = Thread(target=rellenarIngredientes,args=[1])
t1.start()



t1.join()
