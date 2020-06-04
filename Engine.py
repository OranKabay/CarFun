class Engine:
     def __init__(self, engine_type = "Electric"):
         self.engine_type = engine_type
         if self.engine_type == "Electric":
           print("Engine Type: Electric")
         elif self.engine_type == "Diesel":
           print("Engine Type: Diesel")
         elif self.engine_type == "Petrol":
           print("Engine Type: Petrol")
         else:
           print("Error: Unsupported Engine type: ", engine_type)

     def changeEngine(self, engine_type):
         self.engine_type = engine_type