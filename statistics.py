import matplotlib.pyplot as plt; plt.rcdefaults()
import matplotlib.pyplot as plt
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
    
    y_pos = np.arange(len(listaEtiquetas))
    plt.bar(y_pos, listaValores, align='center', alpha=0.5)
    plt.xticks(y_pos, listaEtiquetas)
    plt.ylabel('Cantidad de Tacos')
    plt.title('Tacos "El Frank"')
    
    plt.show()
