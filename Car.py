from AutoTransmission import *
from Engine import *
from Doors import *
from Convertible import *
from CarColour import *
class Car:
    def __init__(self, engine = "Petrol", transmissionType = "Manual"):
        self.engine = Engine(engine)
        self.gearBoxType = transmissionType
        if engine != "Electric":
            self.changeGearBox(transmissionType)
        else:
            self.gearBoxType = engine

    def changeGearBox(self, transmissionType):
        self.gearBoxType = transmissionType
        if self.gearBoxType == "Automatic":
            self.transmission = AutoTransmission()
        elif self.gearBoxType == "Manual":
            self.transmission = Transmission()
        else:
            print("Error: Unsupported Transmission type: ", transmissionType)

    def changeNumberDoors(self, doors = "4"):
        self.doors = Doors(doors)

    def changeConvertibleType(self, convertible = "OFF"):
        self.convertible = Convertible(convertible)

    def changeCarColour(self, colour = "Black"):
        self.colour = CarColour(colour)