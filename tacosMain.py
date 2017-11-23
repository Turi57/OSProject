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

thread_taquero1 = Thread(target=taquero1, args=[queue_asada_tripa])
thread_taquero1.start()

thread_taquero2 = Thread(target=taquero1, args=[queue_adobada_lengua])
thread_taquero2.start()

thread_taquero3 = Thread(target=taquero1, args=[queue_cabeza_suadero_veggie])
thread_taquero3.start()

while True:
    listaOrdenes.extend(readSQS())
    print(listaOrdenes)
    time.sleep(4)
    print(ingredientes)

