from abc import ABC, abstractmethod

class InvoiceGenerator(ABC):
    def __init__(self, client_name, items):
        self.client_name = client_name
        self.items = items  # [{name, price, quantity}]

    def calculate_total(self):
        """Tanlangan mahsulotlarning jami narxini hisoblaydi"""
        return sum(item["price"] * item["quantity"] for item in self.items)

    @abstractmethod
    def generate_invoice(self):
        pass
