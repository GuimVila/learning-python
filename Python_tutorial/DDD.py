# Domain-Driven Design (DDD) - Summary

"""
Domini-Driven Design (DDD) és una metodologia de desenvolupament de software centrada en connectar el disseny i implementació del software amb el seu domini o àrea de negoci. Es tracta d'entendre les necessitats del domini i traduir-les a codi mitjançant un llenguatge comú entre desenvolupadors i experts.
"""

# 1. Domain
# El domini representa l'àrea de coneixement o activitat principal per a la qual es desenvolupa el software.

# Exemples de dominis:
# - Sistema bancari: Gestió de comptes bancaris.
# - Comerç electrònic: Catàleg de productes i comandes.
# - Sistema mèdic: Gestions de pacients i programació de cites.

class BankAccount:
    """A bank account with basic operations."""
    def __init__(self, id, balance):
        self.id = id
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            raise ValueError("Insufficient balance")
        self.balance -= amount

class Order:
    """An order with a list of products."""
    def __init__(self, id):
        self.id = id
        self.products = []

    def add_product(self, product):
        self.products.append(product)

# 2. Domain Model
# És una abstracció del domini que encapsula conceptes clau, regles i comportaments a través d'entitats, objectes de valor, agregats i serveis.

class Product:
    """A product with code, name, and price."""
    def __init__(self, code, name, price):
        self.code = code
        self.name = name
        self.price = price

class Inventory:
    """An inventory of products."""
    def __init__(self):
        self.products = []

    def check_availability(self, code, quantity):
        # Dummy implementation for availability check
        return True

# 3. Ubiquitous Language
# Un llenguatge comú compartit entre desenvolupadors i experts en el domini que assegura coherència.
# Exemple: en un sistema bancari, termes com "Account", "Balance" i "Transaction" són clars per a tothom.

# 4. Bounded Context
# Cada model de domini és vàlid dins d'un context delimitat. Això permet utilitzar models diferents per a conceptes semblants en diferents parts del sistema.

# 5. Benefits of DDD
# - Connecta el desenvolupament amb les necessitats reals del negoci.
# - Simplifica la gestió de la complexitat mitjançant la divisió en contextos delimitats.
# - Promou la col·laboració i un codi clar i organitzat.

# Complete Example
class Product:
    """A product with immutable properties."""
    def __init__(self, code, name, price):
        self.code = code
        self.name = name
        self.price = price

class Order:
    """An order that tracks products and state."""
    def __init__(self, id, status="pending"):
        self.id = id
        self.products = []
        self.status = status

    def add_product(self, product):
        self.products.append(product)

    def calculate_total(self):
        return sum(product.price for product in self.products)

class OrderRepository:
    """Repository for managing orders."""
    def __init__(self):
        self._orders = {}

    def save(self, order):
        self._orders[order.id] = order

    def get(self, order_id):
        return self._orders.get(order_id)

class PaymentService:
    """Service to process payments."""
    def process_payment(self, order):
        if order.status != "paid":
            print(f"Processing payment for order {order.id}")
            order.status = "paid"
        else:
            print(f"Order {order.id} is already paid.")

# Usage Example
if __name__ == "__main__":
    repository = OrderRepository()
    order = Order(id=1, status="pending")
    product = Product(code="P001", name="Laptop", price=1500.00)

    order.add_product(product)
    repository.save(order)

    payment_service = PaymentService()
    payment_service.process_payment(order)
