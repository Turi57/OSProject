import time
import queue

ingredientes = {"Guacamole":500, "Cebolla":500, "Cilantro":500, "Frijoles":500, "Salsa":500}
queue_asada_tripa = queue.Queue()
queue_adobada_lengua = queue.Queue()
queue_cabeza_suadero_veggie = queue.Queue()



def rellenarIngredientes(tiempo):
    while True:
        time.sleep(tiempo)
        ingredientes[min(ingredientes, key=ingredientes.get)] += 50

def taquero1():
    """Este taquero se encarga de la asada y tripa"""
    pass

def taquero2():
    """Este taquero se encarga de adobada y lengua"""
    pass

def taquero3():
    """Este taquero se encarga de cabeza, suadero y veggie"""
    pass
