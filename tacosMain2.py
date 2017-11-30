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

# Graph different aspects of the current orders using dictionaries
tipos = {"Taco":50, "Quesadilla":50, "Mulita":50, "Tostada":50, "Vampiro":50}
carnes = {"Asada":50, "Adobada":50, "Cabeza":50, "Lengua":50, "Suadero":50, "Veggie":50, "Tripa":50}
tamanos = {"Pequeno":20, "Mediano":20, "Grande":20}

def updateGraphDictionaries(dict_orders, dict_tipos, dict_carnes, dict_tamanos, sleep_time):
    while True:
        # Get a list of all the unfinished orders
        list_orders = []
        for k, order in dict_orders.items():
            if order["ReceiptHandle"] != "Deleted":
                list_orders.append(order)
   
        # Update dictionaries according to quantity by type, meat, etc
        obtainTacosByType(list_orders, dict_tipos)
        obtainTacosByMeat(list_orders, dict_carnes)
        obtainOrdenesBySize(list_orders, dict_tamanos)
        
        # Small delay
        time.sleep(sleep_time)

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

thread_grafica = Thread(target=graphThread, args=[[ingredientes, tipos, carnes, tamanos], ["ingredientes", "tipos", "carnes", "tamaños"]])
thread_grafica.start()

time.sleep(1)

thread_update = Thread(target=updateGraphDictionaries, args=[distributed_orders, tipos, carnes, tamanos, 0.1])
thread_update.start()

while True:
    #time.sleep(20)
   # print("DISTRIBUTED", distributed_orders)
    #print("TACOS", tipos)
    #print("CARNES", carnes)
    time.sleep(50)
    listaOrdenes.extend(readSQS())
    print(listaOrdenes)
    print(ingredientes)
    

