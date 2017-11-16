ingredientsList = ["cebolla", "salsa", "cilantro", "aguacate", "frijoles"]
tacoTypesList = ["taco", "quesadilla", "mulita", "tostada", "vampiro"]
meatTypesList = ["asada", "adobada", "cabeza", "lengua", "suadero", "veggie", "tripa"]

class Orden:
    def __init__(self, datetime, request_id, subOrdenes):
        self.datetime = datetime #String
        self.request_id = request_id #String
        self.subOrdenes = subOrdenes #List of subOrden objects
        self.startTime = -1
        self.endTime = -1
        self.steps = [] #List of stepObjects that will be inserted

    def addNewStep(step):
        this.steps.append(step)

    def getLastStep():
        n = len(this.steps)
        if n > 0:
            return this.steps[n-1]
        else:
            return -1

class subOrden:
    def __init__(self, part_id, tacoType, meatType, quantity, ingredients):
        self.part_id = part_id #String
        self.tacoType = tacoType #String
        self.meatType = meatType #String
        self.quantity = quantity #Integer
        self.ingredients = ingredients #List of strings
        self.remainingTacos = quantity #Integer (Counter to keep track of remaining tacos)

class Step:
    def __init__(self, stepNumber, startTime, action):
        self.stepNumber = stepNumber #Integer
        self.startTime = startTime #String
        self.action = action #String
        self.endTime = -1 #Integer (undefined when the object is created)

