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
