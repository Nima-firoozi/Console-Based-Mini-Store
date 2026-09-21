class Product:
    def __init__(self,name:str,price:float,stock:int):
        self.name = name
        self.price = price
        self.stock = stock


    def __str__(self):
        return f"{self.name} - {self.price}$ (Stock: {self.stock})"

