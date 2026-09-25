from models.product import Product

class CartItem:
    """Represent a product and its selected quantity in the shopping cart."""

    def __init__(self, product: Product, quantity: int) -> None:
        """Initialize a cart item with a product and its quantity."""
        self.product: Product = product
        self.quantity: int = quantity

    def __str__(self) -> str:
        """Return the formatted cart item information."""
        return f"- {self.product.name} x{self.quantity} - ${self.quantity * self.product.price:.2f}"

