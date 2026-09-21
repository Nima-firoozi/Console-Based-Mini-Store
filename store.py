from models.product import Product


class Store:
    def __init__(self):
        self.products = list()

    def add_product(self,name:str, price:float, stock:int):
        self.products.append(Product(name,price,stock))

    def list_products(self):
        for product in self.products:
            print(product)

    def find_product(self,name:str):
        for product in self.products:
            if product.name == name:
                return f"find , {product}"
        return f"not find!"




