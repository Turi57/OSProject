import time
import queue

ingredientes = {"Guacamole":500, "Cebolla":500, "Cilantro":500, "Frijoles":500, "Salsa":500}
queue_asada_tripa = queue.Queue()
queue_adobada_lengua = queue.Queue()
queue_cabeza_suadero_veggie = queue.Queue()

orders_in_progress = {}
# Orders in progess format, see order_in_proges_format.txt in extras

taco_lock = threading.Lock()
# Global lock that will delimit simultaneous resource access in threads

def rellenarIngredientes(tiempo):
    while True:
        time.sleep(tiempo)
        taco_lock.acquire() #Acquire LOCK
        ingredientes[min(ingredientes, key=ingredientes.get)] += 50
        taco_lock.release() #Release LOCK


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
                orders_in_progress[orden["request_id"]][suborder["part_id"]] = {
                    "finish_state": False,
                    "steps": []
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
    """Process order, add steps to response"""
    tacos_made = 5
    addStep(order, 1)
    for ingrediente in order["ingredients"]:
        if(ingredientes[ingrediente] < 1):
            addStep(order, 3)
            return [order, False]  # Skips order, next one might not use the missing ingredient, minimizing downtime

    for ingrediente in order["ingredients"]:
        taco_lock.acquire() #Obtain LOCK
        ingredientes[ingrediente] -= tacos_made # Use up 1 unit per taco
        taco_lock.release() #Release LOCK
        
    if order["quantity"] > 0: # Remove tacos from order
        if order["quantity"] < tacos_made:
            order["quantity"] = 0
        else:
            order["quantity"] -= tacos_made

    if order["quantity"] < 1:
        print("FINISHED ------------------")
        addStep(order, 4)
        order_id = order["part_id"][:36]
        orders_in_progress[order_id]["size"] -= 1
        if orders_in_progress[order_id]["size"] == 0:
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
    next_step = len(orders_in_progress[order_id][suborder_id]["steps"]) + 1
    now = time.strftime("%Y-%m-%d-%H-%M-%S")
    
    taco_lock.acquire() #Acquire LOCK
    orders_in_progress[order_id][suborder_id]["steps"].append({
        "step":next_step,
        "state":current_state[0],
        "action":current_state[1],
        "part_id":suborder_id,
        "startTime": now
    })
    taco_lock.release() #Release LOCK

    if next_step > 1:
        orders_in_progress[order_id][suborder_id]["steps"][next_step-2].update({"endTime":now})
    if state == 4:
        orders_in_progress[order_id][suborder_id]["steps"][next_step-1].update({"endTime":now})


def sendResponse(order):
    # TODO: Send response to sqs based on order in progress info
    pass
