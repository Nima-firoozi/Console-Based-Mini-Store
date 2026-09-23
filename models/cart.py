from cartitem import CartItem
from product import Product

class Cart:
    def __init__(self) -> None:
        self.items : list[CartItem] = []

    def add_to_cart(self,product:Product, quantity:int)->bool:

        if(product.stock >= quantity):
            cart_item = CartItem(product,quantity)
            is_in_list:bool = False
            for cartitem in self.items:
                if cartitem.product==cart_item.product:
                    cartitem.quantity += quantity
                    is_in_list = True
                    break
            if(not is_in_list):
                self.items.append(cart_item)
            product.stock -= quantity
            return True
        else:
            return False
        
    def remove_form_cart(self,product_name:str)->bool:
        for cartitem in self.items:
            if cartitem.product.name == product_name:
                self.items.remove(cartitem)
                cartitem.product.stock += cartitem.quantity
                return True
        return False


    def view_cart(self)->None:
        for item in self.items:
            print(item)


    def total_price(self) -> float:
        total_price = 0
        for cartitem in self.items:
            total_price += cartitem.product.price*cartitem.quantity
        return total_price

            