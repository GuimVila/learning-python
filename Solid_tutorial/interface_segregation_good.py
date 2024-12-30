# Interface segregation principle

# Overall it's better if you have several specific interfaces as opposed to one general purpose interface.

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
# Not all subclasses accept two-factor authentication, so we need to split the PaymentProcessor class into two interfaces    
class PaymentProcessor(ABC):
    @abstractmethod
    def pay(self, order):
        pass
    
class PaymentProcessor_SMS(PaymentProcessor):
    @abstractmethod
    def auth_sms(self, code):
        pass
    
class DebitPaymentProcessor(PaymentProcessor_SMS):
    
    def __init__(self, security_code):
        self.security_code = security_code
        self.verified = False
    
    def auth_sms(self, code):
        print(f"Verifying SMS code: {code}")
        self.verified = True    
        
    def pay(self, order):
        if not self.verified:
            raise Exception("Unverified payment")
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
class PayPalPaymentProcessor(PaymentProcessor_SMS):
    
    def __init__(self, email_adress):
        self.email_adress = email_adress
        self.verified = False
        
    def auth_sms(self, code):
        print(f"Verifying SMS code: {code}")
        self.verified = True 
        
    def pay(self, order):
        if not self.verified:
            raise Exception("Unverified payment")
        print("Processing paypal payment type")
        print(f"Verifying email adress: {self.email_adress}")
        order.status = "paid"
            
order = Order()
order.add_item('Keyboard', 1, 50)
order.add_item('SSD', 1, 150)
order.add_item('USB cable', 2, 5)

print(order.total_price())
processor = PayPalPaymentProcessor("hi@joe.com")
processor.auth_sms("465873")
processor.pay(order)