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

def graphThread(dataDictionaryList, graphTitlesList):
    """Function that graphs the current values of a list of dictionaries using matplotlib in real time. It has another parameter
    for passing in the titles of the dictionaries´ graphs"""
    
    # Instantiate the matplotlib window for graphing
    fig=plt.figure()
    
    # Create subplots and barCollections
    barCollectionsList = []
    for i, dataDictionary in enumerate(dataDictionaryList):
        sub = fig.add_subplot(2, 3, i + 1)
        sub.set_title(graphTitlesList[i])
        sub.tick_params(labelsize=10)
        barcollec = plt.bar(list(dataDictionary.keys()), list(dataDictionary.values()))
        barCollectionsList.append(barcollec)
    
    # Number of frames
    n=100

    # Function used by FuncAnimation to animate the graphs
    def animate(i):
        for graphNumber, dataDictionary in enumerate(dataDictionaryList):
            y = list(dataDictionary.values())
            for i, b in enumerate(barCollectionsList[graphNumber]):
                b.set_height(y[i])
        

    anim=animation.FuncAnimation(fig,animate,repeat=True,blit=False,frames=n,
                                 interval=100)
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
