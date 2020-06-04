class Transmission:
    def __init__(self, current_gear = 0):
        self.current_gear = current_gear
    def changeGear(self,new_gear):
        self.current_gear = new_gear
        print("Changed gear to: ", self.current_gear)
    def reverseGear(self):
        self.current_gear = -1
        print("Changed gear to Reverse: ", self.current_gear)