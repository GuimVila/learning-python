# Dependency Inversion Principle

# Means that we want a class to depend on abstractions and not on concrete subclasses. 
# In the last example, the payment processes were depending on specific authorizers. 

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

class Authorizer(ABC):
    @abstractmethod
    def is_authorized(self) -> bool:
        pass
    
class SMSAuth(Authorizer):  
    authorized = False
    
    def verify_code(self, code):
        print(f"Verifying SMS code: {code}")
        self.authorized = True
        
    def is_authorized(self) -> bool:
        return self.authorized
    
class NotARobot(Authorizer):
    authorized = False
    
    def not_a_robot(self):
        print("You are not a robot")
        self.authorized = True
        
    def is_authorized(self) -> bool:
        return self.authorized
    
class PaymentProcessor(ABC):
    @abstractmethod
    def pay(self, order):
        pass
    
class DebitPaymentProcessor(PaymentProcessor):
    
    def __init__(self, security_code, authorizer: Authorizer):
        self.authorizer = authorizer
        self.security_code = security_code
        
    def pay(self, order):
        if not self.authorizer.is_authorized():
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
class PayPalPaymentProcessor(PaymentProcessor):
    
    def __init__(self, email_adress, authorizer: Authorizer):
        self.authorizer = authorizer
        self.email_adress = email_adress
        
    def pay(self, order):
        if not self.authorizer.is_authorized():
            raise Exception("Unverified payment")
        print("Processing paypal payment type")
        print(f"Verifying email adress: {self.email_adress}")
        order.status = "paid"
            
order = Order()
order.add_item('Keyboard', 1, 50)
order.add_item('SSD', 1, 150)
order.add_item('USB cable', 2, 5)

print(order.total_price())
# We can call the not_a_robot method from the NotARobot class
# authorizer = NotARobot()
authorizer = SMSAuth()
processor = DebitPaymentProcessor("2349875", authorizer)
# authorizer.not_a_robot()
authorizer.verify_code("465839")
processor.pay(order)