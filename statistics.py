import tabulate

def printTable(orderList):
    orders = []
    for order in orderList:
        quantity = 0
        for suborder in order["orden"]:
            quantity += suborder["quantity"]
        orders.append([order["request_id"], quantity])

    print(tabulate.tabulate(orders, headers=["Request ID", "Quantity"]))
