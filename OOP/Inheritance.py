class vehicle:
    def __init__(self, brand):
        self.brand = brand
    
    def displayBrand(self):
        print("Brand :", self.brand)
    
class bike(vehicle):
    def __init__(self, brand, model):
        super().__init__(brand)
        self.model = model
    
    def displayModel(self):
        print("Model : ", self.model)

class bikeSpec(bike):
    def __init__(self, model, color):
        super().__init__(model)
        self.color = color

    def displayColor(self):
        print("Color :", self.color)



bike1 = bikeSpec('BMW','G310R','Blue')
bike1.displayBrand()
bike1.displayModel()
bike1.displayColor()
        