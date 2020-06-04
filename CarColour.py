class CarColour:
    def __init__(self, car_colour ="Black"):
        self.car_colour = car_colour
        if self.car_colour == "Black":
            print("Car Colour: Black")
        elif self.car_colour == "Grey":
            print("Car Colour: Grey")
        elif self.car_colour == "White":
            print ("Car Colour: White")
        elif self.car_colour == "Blue":
            print("Car Colour: Blue")
        elif self.car_colour == "Red":
            print("Car Colour: Red")
        elif self.car_colour == "Green":
            print("Car Colour: Green")
        elif self.car_colour == "Yellow":
            print("Car Colour: Yellow")
        elif self.car_colour == "Silver":
            print("Car Colour: Silver")
        elif self.car_colour == "Purple":
            print("Car Colour: Purple")
        elif self.car_colour == "Pink":
            print("Car Colour: Pink")
        elif self.car_colour == "Chrome":
            print("Car Colour: Chrome")
        elif self.car_colour == "Bronze":
            print("Car Colour: Bronze")
        elif self.car_colour == "Gold":
            print("Car Colour: Gold")
        else:
            print("Error: Unsupported Car Colour: ", car_colour)

    def changeCarColour(self, car_colour):
        self.car_colour = car_colour