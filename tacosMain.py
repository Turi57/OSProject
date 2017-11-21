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

thread_ingredientes = Thread(target=rellenarIngredientes, args=[1])
thread_ingredientes.start()

thread_mesero = Thread(target=mesero, args=[listaOrdenes])
thread_mesero.start()

while True:
    listaOrdenes.extend(readSQS())
    time.sleep(10)

thread_mesero.join()
thread_ingredientes.join()


