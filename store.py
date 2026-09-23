from models.product import Product


class Store:
    """Manages the store's product inventory."""

    def __init__(self)->None:
        self.products : list[Product] = []

    def add_product(self,name:str, price:float, stock:int)->None:
        self.products.append(Product(name,price,stock))

    def list_products(self)->None:
        for product in self.products:
            print(product)

    def find_product(self,name:str)->Product | None:
        for product in self.products:
            if product.name == name:
                return product
        return None



