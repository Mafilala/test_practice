class Product:
    def __init__(self, name ,price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
        
    
    def calculateTotal(self):
        if self.quantity < 0:
            raise ValueError
        return self.price * self.quantity