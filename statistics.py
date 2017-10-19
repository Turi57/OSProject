import matplotlib.pyplot as plt; plt.rcdefaults()
import matplotlib.pyplot as plt
from jsonOrder import *
import numpy as np
import tabulate

def printTable(orderList):
    typeCount = {"taco": 0, "quesadilla": 0, "mulita": 0, "tostada": 0, "vampiro": 0}
    for order in orderList:
        for suborder in order["orden"]:
            typeCount[suborder["type"]] += suborder["quantity"]
    print(tabulate.tabulate([list(typeCount.keys()), list(typeCount.values())],headers=["Quantity", "Type"]))

def graphBars(listaEtiquetas, listaValores, titulo):
    ### Here is the function to graph a list of values with a list of labels
    plt.ion()
    y_pos = np.arange(len(listaEtiquetas))

    plt.figure()
    plt.title(titulo)
    plt.xticks(y_pos, listaEtiquetas)
    plt.bar(y_pos, listaValores, align='center', alpha=0.5)
    
def obtainTacosByType(listaOrdenes):
    cantidadPorTipo = {"taco":0, "quesadilla":0, "mulita":0, "tostada":0, "vampiro":0}
    for orden in listaOrdenes:
        subordenes = orden["orden"]
        for i in range(len(subordenes)):
            currentType = subordenes[i]["type"]
            cantidadPorTipo[currentType] += subordenes[i]["quantity"]
    return cantidadPorTipo

def obtainTacosByMeat(listaOrdenes):
    cantidadPorCarne = {"asada":0, "adobada":0, "cabeza":0, "lengua":0, "suadero":0, "veggie":0, "tripa":0}
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
