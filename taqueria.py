import time
import queue

ingredientes = {"Guacamole":500, "Cebolla":500, "Cilantro":500, "Frijoles":500, "Salsa":500}
queue_asada_tripa = queue.Queue()
queue_adobada_lengua = queue.Queue()
queue_cabeza_suadero_veggie = queue.Queue()

orders_in_progress = {}
# Orders in progess format
# {order_id> {suborder_id dict> [done_status, start, end, {steps}]}}

# {
#   "123": {                        Order ID
#     "123-1": [                    Suborder ID
#       false,                      Finish status
#       "2017-01-01 20:21:03",      Start date
#       "2017-01-01 20:26:39",      End date
#       {                           Step list
#         "step1": "Working on it",
#         "step2": "Paused",
#         "step3": "Working on it",
#         "step4": "Finished"
#       }
#     ],
#     "123-2": [                    Suborder ID
#       true,                       Finish Status
#       "2017-01-01 20:21:39",      Start date
#       "2017-01-01 20:25:39",      End date
#       {                           Step list
#         "step1": "Working on it",
#         "step2": "Paused",
#         "step3": "Working on it",
#         "step4": "Finished"
#       }
#     ]
#   }
# }


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
    for ingrediente in order["ingredients"]:
        if(ingredientes[ingrediente] < 1):
            return [order, False]

    for ingrediente in order["ingredients"]:
        ingredientes[ingrediente] -= 1

    if order["quantity"] > 0:
        order["quantity"] -= 1
    if order["quantity"] == 0:
        #look for pair order, if it is finished too, send response
        addStep(order, 1)
        return [order, True]

    return [order, False]

def addStep(order, step):
    order_id = order["part_id"][:36]
    suborder_id = order["part_id"]

