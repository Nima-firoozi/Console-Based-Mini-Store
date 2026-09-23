class Product:
    def __init__(self,name:str,price:float,stock:int)->None:
        self.name = name
        self.price = price
        self.stock = stock

    def __str__(self):
        return f"{self.name} - ${self.price:.2f} (Stock: {self.stock})"
