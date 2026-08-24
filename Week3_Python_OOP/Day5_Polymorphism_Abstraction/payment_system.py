from abc import ABC, abstractmethod

# Abstraction: Abstract base class
class PaymentProcessor(ABC):
    @abstractmethod
    def process_payment(self, amount):
        pass

# Polymorphism: Different implementations of the same method
class CreditCardPayment(PaymentProcessor):
    def process_payment(self, amount):
        print(f"Processing credit card payment of Rs.{amount}")

class PayPalPayment(PaymentProcessor):
    def process_payment(self, amount):
        print(f"Processing PayPal payment of Rs.{amount}")

class UPIPayment(PaymentProcessor):
    def process_payment(self, amount):
        print(f"Processing UPI payment of Rs.{amount}")

def checkout(payment_method: PaymentProcessor, amount: float):
    # This function demonstrates polymorphism
    payment_method.process_payment(amount)

# Example usage
if __name__ == "__main__":
    payment1 = CreditCardPayment()
    payment2 = UPIPayment()

    checkout(payment1, 1500)
    checkout(payment2, 500)
