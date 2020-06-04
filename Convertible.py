class Convertible:
    def __init__(self, convertible = "ON"):
        self.convertible = convertible
        if self.convertible == "ON":
            print("Convertible Equipped")
        elif self.convertible == "OFF":
            print("Convertible not Equipped")
        else:
            print("Error: Unsupported Convertible Type: ", convertible)

    def changeConvertibleType(self, convertible):
        self.convertible = convertible