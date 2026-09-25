"""Entry point for the Mini Store Management System."""

from store import Store
from cli import start

# Create the main store instance.
main_store = Store()

# Start the application.
start(main_store)
