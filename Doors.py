class Doors:
    def __init__(self, number_doors = "4"):
        self.number_doors = number_doors
        if self.number_doors == "4":
            print("Number of Doors: 4")
        elif self.number_doors == "2":
            print("Number of Doors: 2")
        elif self.number_doors == "6":
            print("Number of Doors: 6")
        else:
            print("Error: Unsupported Number of Doors: ", number_doors)

    def changeNumberDoors(self, number_doors):
        self.number_doors = number_doors