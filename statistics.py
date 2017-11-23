import matplotlib.pyplot as plt; plt.rcdefaults()
import matplotlib.pyplot as plt
from jsonOrder import *
import numpy as np
import tabulate

def printTable(orderList):
    typeCount = {"Taco": 0, "Quesadilla": 0, "Mulita": 0, "Tostada": 0, "Vampiro": 0}
    for order in orderList:
        for suborder in order["orden"]:
            typeCount[suborder["type"]] += suborder["quantity"]
    print(tabulate.tabulate([list(typeCount.keys()), list(typeCount.values())],headers=["Quantity", "Type"]))

def graphBars(listaEtiquetas, listaValores, titulo):
    ### Here is the function to graph a list of values with a list of labels
    plt.bar(listaEtiquetas, listaValores)
    plt.ylabel("Quantity of items")
    plt.title(titulo)
    plt.xlabel("Item type")
    plt.show()

    
def obtainTacosByType(listaOrdenes):
    cantidadPorTipo = {"Taco": 0, "Quesadilla": 0, "Mulita": 0, "Tostada": 0, "Vampiro": 0}
    for orden in listaOrdenes:
        subordenes = orden["orden"]
        for i in range(len(subordenes)):
            currentType = subordenes[i]["type"]
            cantidadPorTipo[currentType] += subordenes[i]["quantity"]
    return cantidadPorTipo

def obtainTacosByMeat(listaOrdenes):
    cantidadPorCarne = {"Asada":0, "Adobada":0, "Cabeza":0, "Lengua":0, "Suadero":0, "Veggie":0, "Tripa":0}
    for orden in listaOrdenes:
        subordenes = orden["orden"]
        for i in range(len(subordenes)):
            currentMeat = subordenes[i]["meat"]
            cantidadPorCarne[currentMeat] += subordenes[i]["quantity"]
    return cantidadPorCarne

#Function to send directly a dictionary as a list of labels and values
def graphTacos(diccionario, titulo):
    graphBars(list(diccionario.keys()), list(diccionario.values()), titulo)
    

##TESTINT####
#listaOrdenes = readOrdersFile()
#tipos = obtainTacosByType(listaOrdenes)
#carnes = obtainTacosByMeat(listaOrdenes)

#graphTacos(tipos, "Tipos de taco")
#graphTacos(carnes, "Tipos de carne")
