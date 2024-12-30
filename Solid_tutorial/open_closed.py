# Open closed principel
# We want classes to be open for extension but closed for modification.
# Meaning that we should be able to add new functionality to a class without modifying it.
# We can achieve this by using inheritance and composition.

# We can refactor the PaymentProcessor class to use inheritance.

from abc import ABC, abstractmethod
class Order:
    items = []
    quantities = []
    prices = []
    status = 'open'
    
    def add_item(self, item, quantity, price):
        self.items.append(item)
        self.quantities.append(quantity)
        self.prices.append(price)
        
    def total_price(self): 
        total = 0
        for i in range(len(self.prices)):
            total += self.quantities[i] * self.prices[i]
        return total

class PaymentProcessor(ABC):
    @abstractmethod
    def pay(self, order, security_code):
        pass
    
class DebitPaymentProcessor(PaymentProcessor):
    def pay(self, order, security_code):
        print("Processing debit payment type")
        print(f"Verifying security code: {security_code}")
        order.status = "paid"    
        
class CreditPaymentProcessor(PaymentProcessor):
    def pay(self, order, security_code):
        print("Processing credit payment type")
        print(f"Verifying security code: {security_code}")
        order.status = "paid"
# Now we can create a new payment processor without modifying the existing code.
class PayPalPaymentProcessor(PaymentProcessor):
    def pay(self, order, security_code):
        print("Processing paypal payment type")
        print(f"Verifying security code: {security_code}")
        order.status = "paid"
            
order = Order()
order.add_item('Keyboard', 1, 50)
order.add_item('SSD', 1, 150)
order.add_item('USB cable', 2, 5)

print(order.total_price())
processor = DebitPaymentProcessor()
processor.pay(order, "0372846")