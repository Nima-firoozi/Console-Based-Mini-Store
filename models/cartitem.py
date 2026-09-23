from product import Product

class CartItem:
    """Holds a product and the quantity of it selected in the cart."""
    def __init__(self,product:Product,quantity:int) -> None:
        self.product = product
        self.quantity = quantity

    def __str__(self)-> str:
        return f"- {self.product.name} x{self.quantity} - ${self.quantity*self.product.price:.2f}"

