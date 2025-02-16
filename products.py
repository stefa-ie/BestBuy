from multiprocessing.managers import Value


class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.active = True

        if not len(name) or price < 0 or quantity < 0:
            raise ValueError("Name can not be empty, price and quantity can not be negative.")

    def get_quantity(self) -> int:
        return self.quantity

    def set_quantity(self, quantity):
        if quantity < 0:
            raise ValueError("Quantity can not be negative.")
        self.quantity = quantity
        if self.quantity == 0:
            self.deactivate()

    def is_active(self) -> bool:
        return self.active

    def activate(self):
        self.active = True

    def deactivate(self):
        self.active = False

    def show(self) -> str:
        return f"Name, Price={self.price}, Quantity={self.quantity}"

    def buy(self, quantity) -> float:
        if quantity < 0:
            raise ValueError("Quantity can not be negative.")
        if quantity < self.quantity:
            raise ValueError("Requested quantity is not available.")

        total_price = self.price * quantity
        self.quantity -= quantity

        if self.quantity == 0:
            self.deactivate()

        return total_price

