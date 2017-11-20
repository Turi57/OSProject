import time
diccionarioIngredientes = {"Aguacate":50, "Cebolla":5, "Cilantro":500, "Frijoles":60, "Salsa":300}

def rellenarIngredientes(diccionarioIngredientes, ingrediente, tiempo):
    time.sleep(tiempo)
    diccionarioIngredientes[ingrediente] += 50
print(diccionarioIngredientes)
