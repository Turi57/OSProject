import time
diccionarioIngredientes = {"Aguacate":50, "Cebolla":5, "Cilantro":500, "Frijoles":60, "Salsa":300}

def rellenarIngredientes(diccionarioIngredientes, ingrediente, tiempo):
    time.sleep(tiempo)
    diccionarioIngredientes[ingrediente] = 500
print(diccionarioIngredientes)
    
for ingrediente in list(diccionarioIngredientes.keys()):
        rellenarIngredientes(diccionarioIngredientes,ingrediente,1)
print(diccionarioIngredientes)
