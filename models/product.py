class Product:
    """Represent a product available in the store."""

    def __init__(self, name: str, price: float, stock: int) -> None:
        """Initialize a product with its name, price, and stock."""
        self.name: str = name
        self.price: float = price
        self.stock: int = stock

    def __str__(self) -> str:
        """Return the formatted product information."""
        return f"{self.name} - ${self.price:.2f} (Stock: {self.stock})"