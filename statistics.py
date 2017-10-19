import matplotlib.pyplot as plt; plt.rcdefaults()
import matplotlib.pyplot as plt
from jsonOrder import *
import numpy as np
import tabulate

def printTable(orderList):
    orders = []
    for order in orderList:
        quantity = 0
        for suborder in order["orden"]:
            quantity += suborder["quantity"]
        orders.append([order["request_id"], quantity])

    print(tabulate.tabulate(orders, headers=["Request ID", "Quantity"]))

def graphBars(listaEtiquetas, listaValores):
    ### Here is the function to graph a list of values with a list of labels
    plt.ion()
    y_pos = np.arange(len(listaEtiquetas))

    plt.figure()
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

def graphTacosByType(diccionarioTipos):
    graphBars(list(diccionarioTipos.keys()), list(diccionarioTipos.values()))
    

def obtainTacosByMeat(listaOrdenes):
    cantidadPorCarne = {"asada":0, "adobada":0, "cabeza":0, "lengua":0, "suadero":0, "veggie":0, "tripa":0}
    for orden in listaOrdenes:
        subordenes = orden["orden"]
        for i in range(len(subordenes)):
            currentMeat = subordenes[i]["meat"]
            cantidadPorCarne[currentMeat] += subordenes[i]["quantity"]
    return cantidadPorCarne

def graphTacosByMeat(diccionarioCarnes):
    graphBars(list(diccionarioCarnes.keys()), list(diccionarioCarnes.values()))

#listaOrdenes = readOrdersFile()
#tipos = obtainTacosByType(listaOrdenes)
#carnes = obtainTacosByMeat(listaOrdenes)

#graphTacosByType(tipos)
#graphTacosByMeat(carnes)
