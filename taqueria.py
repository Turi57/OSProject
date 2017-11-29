import time
import queue
from SQS import *

ingredientes = {"Guacamole":500, "Cebolla":500, "Cilantro":500, "Frijoles":500, "Salsa":500}
responseTimes = {"Pequeño":[], "Mediano":[], "Grande":[]}

queue_asada_tripa = queue.Queue()
queue_adobada_lengua = queue.Queue()
queue_cabeza_suadero_veggie = queue.Queue()

orders_in_progress = {}
distributed_orders = {}
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
            distributed_orders[orden["request_id"]] = orden


            orders_in_progress[orden["request_id"]] = {
                "size":len(orden["orden"]),
                "start_time": orden["datetime"],
                "steps": [],
                "start_time":orden["datetime"],
            }

            for suborder in orden["orden"]:
                orders_in_progress[orden["request_id"]][suborder["part_id"]] = {
                    "finish_state": False,
                    "quantity": suborder["quantity"]
                }
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
        if not processed_order[1]:
            orderQueue.put(processed_order[0])
        time.sleep(2)


def processOrder(order):
    order_id = order["part_id"][:36]
    suborder_id = order["part_id"]
    """Process order, add steps to response"""
    tacos_made = 5
    addStep(order, 1)
    for ingrediente in order["ingredients"]:
        if(ingredientes[ingrediente] < 1):
            addStep(order, 3)
            return [order, False]  # Skips order, next one might not use the missing ingredient, minimizing downtime

    for ingrediente in order["ingredients"]:
        ingredientes[ingrediente] -= tacos_made # Use up 1 unit per taco
    if orders_in_progress[order_id][suborder_id]["quantity"] > 0: # Remove tacos from order
        if orders_in_progress[order_id][suborder_id]["quantity"] < tacos_made:
            orders_in_progress[order_id][suborder_id]["quantity"] = 0
        else:
            orders_in_progress[order_id][suborder_id]["quantity"] -= tacos_made

    if orders_in_progress[order_id][suborder_id]["quantity"] < 1:
        print("FINISHED ------------------")
        addStep(order, 4)
        print(orders_in_progress)
        order_id = order["part_id"][:36]
        orders_in_progress[order_id]["size"] -= 1
        if orders_in_progress[order_id]["size"] == 0:
            # Remove the receiptHandle from the json order
            receipt = distributed_orders[order_id]["ReceiptHandle"]
            del distributed_orders[order_id]["ReceiptHandle"]
            deleteSQS(receipt)
            print("DELETE", receipt)
            #deleteSQS(receipt)
            receipt = orders_in_progress[order_id]["ReceiptHandle"]
            del orders_in_progress[order_id]["ReceiptHandle"]
 #           deleteSQS(receipt)

            # Send response to SQS
            sendResponse(order)
            orders_in_progress.pop(order_id)

        return [order, True]

    addStep(order, 2)
    return [order, False]


def addStep(order, state):
    # 1 - Running, 2 - Paused, 3 - Missing ingredient, 4 - Finished
    current_state = []
    if state == 1:
        current_state = ["Running", "Working on order"]
    elif state == 2:
        current_state = ["Suspended", "Next order"]
    elif state == 3:
        current_state = ["Suspended", "Waiting on ingredient"]
    elif state == 4:
        current_state = ["Finished", "Order finished"]
    else:
        current_state = ["Unknown", "Unknown"]

    order_id = order["part_id"][:36]
    suborder_id = order["part_id"]
    next_step = len(orders_in_progress[order_id]["steps"]) + 1
    now = time.strftime("%Y-%m-%d %H:%M:%S")
    orders_in_progress[order_id]["steps"].append({
        "step":next_step,
        "state":current_state[0],
        "action":current_state[1],
        "part_id":suborder_id,
        "startTime": now
    })

    if next_step > 1:
        orders_in_progress[order_id]["steps"][next_step-2].update({"endTime":now})
    if state == 4:
        orders_in_progress[order_id]["steps"][next_step-1].update({"endTime":now})


def sendResponse(order):
    # TODO: Send response to sqs based on order in progress info
    print()
    order_stats = orders_in_progress[order["part_id"][:36]]
    message = {"answer":{
        "start_time":order_stats["start_time"],
        "end_date": order_stats["steps"][-1]["endTime"],
        "steps":order_stats["steps"]
    }}
    message.update(distributed_orders[order["part_id"][:36]])
    print(message)
    message = json.dumps(message)
    # putSQS(message)
