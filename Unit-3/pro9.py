from abc import ABC, abstractmethod

class PaymentGateway(ABC):
    @abstractmethod
    def process_payment(self, amount):
        pass

class PayPal(PaymentGateway):
    def process_payment(self, amount):
        print(f"Processing ${amount} via PayPal...")

class CreditCard(PaymentGateway):
    def process_payment(self, amount):
        print(f"Processing ${amount} via Credit Card...")

# Usage
pay = PayPal()
pay.process_payment(100)