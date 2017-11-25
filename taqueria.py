import time
import queue

ingredientes = {"Guacamole":500, "Cebolla":500, "Cilantro":500, "Frijoles":500, "Salsa":500}
queue_asada_tripa = queue.Queue()
queue_adobada_lengua = queue.Queue()
queue_cabeza_suadero_veggie = queue.Queue()

orders_in_progress = {}
# Orders in progess format, see order_in_proges_format.txt in extras



def rellenarIngredientes(tiempo):
    while True:
        time.sleep(tiempo)
        ingredientes[min(ingredientes, key=ingredientes.get)] += 50


def mesero(listaOrdenes):
    """Takes orders and submits them to appropriate queue"""

    while True:
        print("Mesero", len(listaOrdenes))
        if len(listaOrdenes) > 0:
            orden = listaOrdenes.pop(0)

            orders_in_progress[orden["request_id"]] = {
                "size":len(orden["orden"]),
                "start_time":orden["datetime"]
            }

            for suborder in orden["orden"]:
                meat_type = suborder["meat"]
                print(meat_type)
                if meat_type == "Asada" or meat_type == "Tripa":
                    queue_asada_tripa.put(suborder)
                elif meat_type == "Adobada" or meat_type == "Lengua":
                    queue_adobada_lengua.put(suborder)
                else:
                    queue_cabeza_suadero_veggie.put(suborder)


        time.sleep(1)


def taquero1(orderQueue):
    """Takes orders from correspoding queue and processes them."""
    while True:
        processed_order = processOrder(orderQueue.get())
        if processed_order[1]:
            orderQueue.put(processed_order[0])
        time.sleep(2)


def processOrder(order):
    """Process order, add steps to response"""
    order_id = order["part_id"][:36]
    suborder_id = order["part_id"]
    if suborder_id not in orders_in_progress[order_id]:
        orders_in_progress[order_id][suborder_id] = {
            "finish_state": False,
            "steps": []
        }
    addStep(order, 1)
    for ingrediente in order["ingredients"]:
        if(ingredientes[ingrediente] < 1):
            addStep(order, 3)
            return [order, False]  # Skips order, next one might not use the missing ingredient, minimizing downtime

    for ingrediente in order["ingredients"]:
        ingredientes[ingrediente] -= 1

    if order["quantity"] > 0:
        order["quantity"] -= 1

    if order["quantity"] == 0:
        # TODO: look for pair suborders, if it is finished too, send response
        addStep(order, 1, 4)
        return [order, True]

    addStep(order, 3)
    return [order, False]


def addStep(order, state):
    # 1 - Running
    # 2 - Paused
    # 3 - Missing ingredient
    # 4 - Finished
    order_id = order["part_id"][:36]
    suborder_id = order["part_id"]
    next_step = len(orders_in_progress[order_id][suborder_id]["steps"]) + 1
    # TODO: Add steps to orders_in_progess
    pass