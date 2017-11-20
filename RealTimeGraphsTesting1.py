import pylab as plt
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import threading
import time
import random

def main():
    tiempoPorTipo = {"taco":30, "quesadilla":30, "mulita":30, "tostada":30, "vampiro":30}
    tiempoPorCarne = {"asada":30, "adobada":30, "cabeza":30, "lengua":30, "suadero":30, "veggie":30, "tripa":30}
    tiempoPorTamañoOrden = {"pequeño":30, "mediano":40, "grande":60}
    ingredientesRestantes = {"cebolla":500, "salsa":400, "cilantro":200, "aguacate":170, "frijoles":390}

    t = threading.Thread(target=graphThread, args=([tiempoPorTipo, tiempoPorCarne, tiempoPorTamañoOrden, ingredientesRestantes],))
    t.start()
    while True:
        time.sleep(1)
        updateValue(tiempoPorTipo)
        updateValue(tiempoPorCarne)
        updateValue(tiempoPorTamañoOrden)
        updateValue(ingredientesRestantes)

def updateValue(dictionary):
    for k, v in dictionary.items():
        dictionary[k] -= random.randint(0,5)
        
    
def graphThread(dataDictionaryList):
    # Instantiate the matplotlib window for graphing
    fig=plt.figure()
    
    # Create subplots and barCollections
    barCollectionsList = []
    for i, dataDictionary in enumerate(dataDictionaryList):
        fig.add_subplot(2, 2, i + 1)
        barcollec = plt.bar(list(dataDictionary.keys()), list(dataDictionary.values()))
        barCollectionsList.append(barcollec)
    
    # Number of frames
    n=100

    # Function used by FuncAnimation to animate the graphs
    def animate(i):
        for graphNumber, dataDictionary in enumerate(dataDictionaryList):
            y = list(dataDictionary.values())
            for i, b in enumerate(barCollectionsList[graphNumber]):
                b.set_height(y[i])
        

    anim=animation.FuncAnimation(fig,animate,repeat=True,blit=False,frames=n,
                                 interval=100)
    plt.show()
    

if __name__ == "__main__":
    main()
