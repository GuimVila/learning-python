# Liskov Substitution

# If you have objects in a program, you should be able to replace those objects
# with instances of their subtypes without affecting the correctness of the program.

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
    
# We remove security_code from the pay method in the PaymentProcessor class
class PaymentProcessor(ABC):
    @abstractmethod
    def pay(self, order):
        pass
    
# Now security code it's an attribute of the class instead of a method parameter 
class DebitPaymentProcessor(PaymentProcessor):
    
    def __init__(self, security_code):
        self.security_code = security_code
        
    def pay(self, order):
        print("Processing debit payment type")
        print(f"Verifying security code: {self.security_code}")
        order.status = "paid"    
        
class CreditPaymentProcessor(PaymentProcessor):
    
    def __init__(self, security_code):
        self.security_code = security_code
    def pay(self, order):
        print("Processing credit payment type")
        print(f"Verifying security code: {self.security_code}")
        order.status = "paid"
        
# Paypal uses email adress instead of security code       
class PayPalPaymentProcessor(PaymentProcessor):
    
    def __init__(self, email_adress):
        self.email_adress = email_adress
    def pay(self, order):
        print("Processing paypal payment type")
        print(f"Verifying email adress: {self.email_adress}")
        order.status = "paid"
            
order = Order()
order.add_item('Keyboard', 1, 50)
order.add_item('SSD', 1, 150)
order.add_item('USB cable', 2, 5)

print(order.total_price())
processor = PayPalPaymentProcessor("hi@joe.com")
processor.pay(order)