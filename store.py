
from models.product import Product


class Store:
    """Manage the store's product inventory."""

    def __init__(self) -> None:
        """Initialize an empty product inventory."""
        self.products: list[Product] = []

    def add_product(
        self,
        name: str,
        price: float,
        stock: int
    ) -> None:
        """Add a new product to the store inventory."""
        self.products.append(Product(name, price, stock))

    def list_products(self) -> None:
        """Display all products currently available in the store."""
        if not self.products:
            print("⚠️ No products available in the store yet.")
        else:
            # Display each product with its position in the inventory.
            for i in range(len(self.products)):
                print(f"[{i + 1}] {self.products[i]}")

    def find_product(self, name: str) -> Product | None:
        """Find a product by its name and return it if found."""
        for product in self.products:
            if product.name == name:
                return product

        return None

