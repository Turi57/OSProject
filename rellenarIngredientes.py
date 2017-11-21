import time
diccionarioIngredientes = {"Guacamole":500, "Cebolla":500, "Cilantro":500, "Frijoles":500, "Salsa":500}

def rellenarIngredientes(tiempo):
    while True:
        time.sleep(tiempo)
        diccionarioIngredientes[min(diccionarioIngredientes, key=diccionarioIngredientes.get)] += 50
