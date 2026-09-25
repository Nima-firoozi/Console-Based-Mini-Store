
from models.cartitem import CartItem
from models.product import Product


class Cart:
    """Manage products and quantities in the shopping cart."""

    def __init__(self) -> None:
        """Initialize an empty shopping cart."""
        self.items: list[CartItem] = []

    def add_to_cart(self, product: Product, quantity: int) -> bool:
        """Add a product with the specified quantity to the cart."""
        if product.stock >= quantity:
            cart_item: CartItem = CartItem(product, quantity)
            is_in_list: bool = False

            # Check if the product is already in the cart.
            for cartitem in self.items:
                if cartitem.product == cart_item.product:
                    cartitem.quantity += quantity
                    is_in_list = True
                    break

            if not is_in_list:
                self.items.append(cart_item)

            # Reduce the product stock by the selected quantity.
            product.stock -= quantity
            return True
        else:
            return False

    def remove_form_cart(self, product_name: str) -> bool:
        """Remove a product from the cart and restore its stock."""
        for cartitem in self.items:
            if cartitem.product.name == product_name:
                self.items.remove(cartitem)
                cartitem.product.stock += cartitem.quantity
                return True

        return False

    def view_cart(self) -> CartItem:
        """Display all products currently in the shopping cart."""
        if not self.items:
            print("⚠️ No products available in the cart yet.")
        else:
            for item in self.items:
                print(item)

    def total_price(self) -> float:
        """Calculate and return the total price of all cart items."""
        total_price = 0

        for cartitem in self.items:
            total_price += cartitem.product.price * cartitem.quantity

        return total_price
