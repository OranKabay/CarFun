from Transmission import Transmission
class AutoTransmission(Transmission):
    def __init__(self):
        self.cruise_control = 'OFF'
        super().__init__()
    def upShift(self):
        self.current_gear += 1
        print("Paddle up gear to: ", self.current_gear)
    def downShift(self):
        self.current_gear -= 1
        print("Paddle down gear to: ", self.current_gear)
    def cruise(self):
        if self.cruise_control == 'OFF':
            self.cruise_control = 'ON'
        else:
            self.cruise_control = 'OFF'
        print("Cruise Control is ", self.cruise_control)