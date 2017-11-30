import time
import queue
import threading
from SQS import *

ingredientes = {"Guacamole": 500, "Cebolla": 500, "Cilantro": 500, "Frijoles": 500, "Salsa": 500}
responseTimes = {"Pequeño": [], "Mediano": [], "Grande": []}
tortillas = [500, 500, 500]

# Global queues
queue_asada_tripa = queue.Queue()
queue_adobada_lengua = queue.Queue()
queue_cabeza_suadero_veggie = queue.Queue()

orders_in_progress = {}
distributed_orders = {}
# Orders in progess format, see order_in_proges_format.txt in extras

# Thread resource lock
lock = threading.Lock()


def rellenarIngredientes(tiempo):
    while True:
        time.sleep(tiempo)
        lock.acquire()
        ingredientes[min(ingredientes, key=ingredientes.get)] += 50
        tortillas[0] += 50
        tortillas[1] += 50
        tortillas[2] += 50
        lock.release()


def mesero(listaOrdenes):
    """Takes orders and submits them to appropriate queue"""

    while True:
        print("Mesero", len(listaOrdenes))
        if len(listaOrdenes) > 0:
            orden = listaOrdenes.pop(0)
            distributed_orders[orden["request_id"]] = orden

            orders_in_progress[orden["request_id"]] = {
                "size": len(orden["orden"]),
                "start_time": orden["datetime"],
                "steps": [],
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
    meat_type = order["meat"]
    for ingrediente in order["ingredients"]:
        if ingredientes[ingrediente] < tacos_made:
            if meat_type == "Asada" or meat_type == "Tripa":
                if tortillas[0] < tacos_made:
                    addStep(order, 3)
                    return [order, False]
            elif meat_type == "Adobada" or meat_type == "Lengua":
                if tortillas[1] < tacos_made:
                    addStep(order, 3)
                    return [order, False]
            else:
                if tortillas[2] < tacos_made:
                    addStep(order, 3)
                    return [order, False]
            addStep(order, 3)
            return [order, False]  # Skips order, next one might not use the missing ingredient, minimizing downtime

    if meat_type == "Asada" or meat_type == "Tripa":
        lock.acquire()
        tortillas[0] -= tacos_made
        lock.release()
    elif meat_type == "Adobada" or meat_type == "Lengua":
        lock.acquire()
        tortillas[1] -= tacos_made
        lock.release()
    else:
        lock.acquire()
        tortillas[2] -= tacos_made
        lock.release()

    for ingrediente in order["ingredients"]:
        lock.acquire()
        ingredientes[ingrediente] -= tacos_made  # Use up 1 unit per taco
        lock.release()
    if orders_in_progress[order_id][suborder_id]["quantity"] > 0:  # Remove tacos from order
        if orders_in_progress[order_id][suborder_id]["quantity"] < tacos_made:
            orders_in_progress[order_id][suborder_id]["quantity"] = 0
        else:
            orders_in_progress[order_id][suborder_id]["quantity"] -= tacos_made

    if orders_in_progress[order_id][suborder_id]["quantity"] < 1:
        print("FINISHED ------------------")
        addStep(order, 4)
        print(orders_in_progress)
        order_id = order["part_id"][:36]
        lock.acquire()
        orders_in_progress[order_id]["size"] -= 1
        lock.release()

        if orders_in_progress[order_id]["size"] == 0:
            # Delete the order from SQS using the receipt handle
            receipt = distributed_orders[order_id]["ReceiptHandle"]
            distributed_orders[order_id]["ReceiptHandle"] = "Deleted"
            # deleteSQS(receipt)
            print("DELETE", receipt)

            sendResponse(order)
            lock.acquire()
            orders_in_progress.pop(order_id)
            lock.release()
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
    lock.acquire()
    next_step = len(orders_in_progress[order_id]["steps"]) + 1
    now = time.strftime("%Y-%m-%d %H:%M:%S")
    orders_in_progress[order_id]["steps"].append({
        "step": next_step,
        "state": current_state[0],
        "action": current_state[1],
        "part_id": suborder_id,
        "startTime": now
    })
    lock.release()
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
