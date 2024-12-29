# Arquitectura Hexagonal - Resum

"""
L'Arquitectura Hexagonal, també coneguda com a "Patró de Ports i Adaptadors", és un enfocament de disseny que busca desacoblar la lògica de negoci central (domini) de les dependències externes com bases de dades, interfícies d'usuari o serveis de tercers. Això permet una aplicació més mantenible, testeable i flexible.

Conceptes clau:
1. **Domini (Core)**: Conté la lògica de negoci i els models centrals. És el cor de l'aplicació i no hauria de dependre de sistemes externs.
2. **Ports**: Defineixen les interfícies per interactuar amb el domini. Són els punts d'entrada i sortida de la lògica de negoci.
3. **Adaptadors**: Implementacions dels ports que connecten el domini amb tecnologies concretes com bases de dades o frameworks web.

"""

# Domini (Core)
# Conté la lògica de negoci i els models

class Order:
    """Representa una comanda en el sistema."""
    def __init__(self, id, products=None):
        self.id = id
        self.products = products if products else []
        self.status = "pending"

    def add_product(self, product):
        self.products.append(product)

    def calculate_total(self):
        return sum(product.price for product in self.products)

class Product:
    """Representa un producte en el sistema."""
    def __init__(self, code, name, price):
        self.code = code
        self.name = name
        self.price = price

# Ports
# Defineixen les interfícies per interactuar amb sistemes externs

class OrderRepositoryPort:
    """Interfície per a persistir comandes."""
    def save(self, order):
        raise NotImplementedError

    def get(self, order_id):
        raise NotImplementedError

class PaymentProcessorPort:
    """Interfície per a processar pagaments."""
    def process_payment(self, order):
        raise NotImplementedError

# Adaptadors
# Implementen els ports per connectar amb sistemes externs

class InMemoryOrderRepository(OrderRepositoryPort):
    """Implementació en memòria de OrderRepositoryPort per testeig."""
    def __init__(self):
        self.orders = {}

    def save(self, order):
        self.orders[order.id] = order

    def get(self, order_id):
        return self.orders.get(order_id)

class StripePaymentProcessor(PaymentProcessorPort):
    """Una implementació simulada d'un processador de pagaments com Stripe."""
    def process_payment(self, order):
        print(f"Processing payment for order {order.id} with total: {order.calculate_total()}")
        order.status = "paid"

# Capa d'Aplicació
# Coordina entre el domini, els ports i els adaptadors

class OrderService:
    """Servei per gestionar comandes."""
    def __init__(self, order_repository: OrderRepositoryPort, payment_processor: PaymentProcessorPort):
        self.order_repository = order_repository
        self.payment_processor = payment_processor

    def create_order(self, order_id):
        order = Order(order_id)
        self.order_repository.save(order)
        return order

    def add_product_to_order(self, order_id, product):
        order = self.order_repository.get(order_id)
        if not order:
            raise ValueError("Order not found")
        order.add_product(product)
        self.order_repository.save(order)

    def process_order_payment(self, order_id):
        order = self.order_repository.get(order_id)
        if not order:
            raise ValueError("Order not found")
        self.payment_processor.process_payment(order)
        self.order_repository.save(order)

# Exemple d'ús
if __name__ == "__main__":
    # Creació d'adaptadors (infraestructura)
    order_repository = InMemoryOrderRepository()
    payment_processor = StripePaymentProcessor()

    # Creació del servei (capa d'aplicació)
    order_service = OrderService(order_repository, payment_processor)

    # Crear una nova comanda
    order = order_service.create_order(order_id=1)

    # Afegir productes a la comanda
    product1 = Product(code="P001", name="Laptop", price=1500.00)
    product2 = Product(code="P002", name="Mouse", price=50.00)
    order_service.add_product_to_order(order_id=1, product=product1)
    order_service.add_product_to_order(order_id=1, product=product2)

    # Processar el pagament de la comanda
    order_service.process_order_payment(order_id=1)

    # Verificar l'estat de la comanda
    processed_order = order_repository.get(1)
    print(f"Order {processed_order.id} status: {processed_order.status}")

"""
Organització en carpetes:

project/
├── domain/  # Núcli de l'aplicació
│   ├── models.py  # Conté Order, Product
│   └── ports.py  # Conté OrderRepositoryPort, PaymentProcessorPort
├── adapters/  # Implementacions específiques dels ports
│   ├── in_memory_order_repository.py  # Implementa InMemoryOrderRepository
│   └── stripe_payment_processor.py  # Implementa StripePaymentProcessor
├── application/  # Coordina el flux entre domini i adaptadors
│   └── services.py  # Conté OrderService
└── main.py  # Punt d'entrada de l'aplicació

Com interactuen:
- **domain/models.py**: Defineix la lògica de negoci i models centrals.
- **domain/ports.py**: Defineix les interfícies per interactuar amb sistemes externs.
- **adapters/**: Conté les implementacions concretes de les interfícies definides a "ports.py".
- **application/services.py**: Utilitza models del domini i interactua amb adaptadors a través dels ports.
- **main.py**: Inicia els adaptadors i serveis, i executa el flux de l'aplicació.
"""
