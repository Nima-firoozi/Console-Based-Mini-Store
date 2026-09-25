from models.OutOfRangeError import OutOfRangeError
from models.cart import Cart
from store import Store


def start(store: Store) -> None:
    """Start the main menu and handle the user's role selection."""

    while True:
        print("""
=================================
🛍️ MINI STORE MANAGEMENT SYSTEM
=================================
👋 Welcome! Please select your role:
1.Store Manager
2.Customer
3.Exit Program
Enter choice: """, end="")

        # Keep asking until the user enters a valid role.
        while True:
            try:
                role = int(input())

                if not (1 <= role <= 3):
                    raise OutOfRangeError

                break

            except OutOfRangeError:
                print("Please choose a number between 1 and 3: ", end="")

            except ValueError:
                print("Please choose a number between 1 and 3: ", end="")

        if role == 1:
            store_manager(store)
            continue

        elif role == 2:
            customer(store)
            continue

        elif role == 3:
            print("👋 Goodbye! See you next time.")
            break


def store_manager(store: Store) -> None:
    """Handle store manager login and product management."""

    user_name: str = input("Username: ")
    password: str = input("Password: ")

    if user_name == "admin" and password == "1234":
        name: str = ""

        while True:
            print("""
1. Add product.
2. View product.
3. Return to main menu.
Enter choice: """, end="")

            select = int()

            # Keep asking until the user enters a valid menu option.
            while True:
                try:
                    select = int(input())

                    if not (1 <= select <= 3):
                        raise OutOfRangeError

                    break

                except OutOfRangeError:
                    print("Please choose a number between 1 and 3: ", end="")

                except ValueError:
                    print("Please choose a number between 1 and 3: ", end="")

            if select == 1:
                print("""
--------------------------------
📦 Add Products
--------------------------------
""")

                while True:
                    name = input(
                        "Enter product name (or 'done' to finish): "
                    )

                    if name == "done":
                        break

                    print("Enter product price: ", end="")

                    while True:
                        try:
                            price = float(input(""))
                            break

                        except ValueError:
                            print("Please enter a valid price: ", end="")

                    print("Enter product stock quantity: ", end="")

                    while True:
                        try:
                            stock: int = int(input(""))
                            break

                        except ValueError:
                            print("Please enter a valid stock: ", end="")

                    store.add_product(name, price, stock)

            elif select == 2:
                print("Products:")
                store.list_products()
                continue

            else:
                break

    else:
        print("❌ Login failed! Please try again or return to main menu.")


def customer(store: Store) -> None:
    """Handle the customer portal and shopping cart operations."""

    cart = Cart()

    while True:
        print(f"""
--------------------
🛍️ CUSTOMER PORTAL
--------------------
Available products:
""", end="")

        store.list_products()

        print("""
What would you like to do?
1. Add item to cart.
2. Remove item from cart. 
3. View cart.
4. Checkout. 
5. Return to main menu.
Enter choice: """, end="")

        select = int()

        # Keep asking until the user enters a valid menu option.
        while True:
            try:
                select = int(input())

                if not (1 <= select <= 5):
                    raise OutOfRangeError

                break

            except OutOfRangeError:
                print("Please choose a number between 1 and 5: ", end="")

            except ValueError:
                print("Please choose a number between 1 and 5: ", end="")

        if select == 1:
            product_name = input("Enter product name: ")
            product = store.find_product(product_name)

            if product:
                quantity = int()
                print("Enter quantity: ", end="")

                while True:
                    try:
                        quantity = int(input())

                        if not (1 <= quantity <= product.stock):
                            raise OutOfRangeError

                        break

                    except OutOfRangeError:
                        print(
                            f"Please choose a number between 1 and {product.stock}:",
                            end=""
                        )

                    except ValueError:
                        print(
                            f"Please choose a number between 1 and {product.stock}: ",
                            end=""
                        )

                cart.add_to_cart(product, quantity)
                print(f"✅ Added {quantity} x {product.name} to cart.")
                continue

            else:
                print(f"❌ Product '{product_name}' not found.")
                continue

        elif select == 2:
            product_name = input("Enter product name: ")

            if cart.remove_form_cart(product_name):
                print(f"🗑️ Removed {product_name} from cart.")
                continue

            else:
                print(f"❌ Product '{product_name}' not found.")
                continue

        elif select == 3:
            print("🛒 Your cart:")
            cart.view_cart()
            print(f"💰 Total: {cart.total_price()}")
            continue

        elif select == 4:
            print("🧾 Final Checkout:")
            cart.view_cart()
            print(f"💳 Total amount due: ${cart.total_price()}")
            print("🎉 Thank you for shopping with us!")
            continue

        elif select == 5:
            print("Returning to main menu...")
            break