import products

class Store:
    def __init__(self, products: list):
        self.products = products

    def add_product(self, product):
        self.products.append(product)

    def remove_product(self, product):
        self.products.remove(product)

    def get_total_quantity(self) -> int:
        total = 0
        for product in self.products:
            total += product.get_quantity()
        return total

    def get_all_products(self) -> list:
        return self.products

    def order(self, shopping_list) -> float:
        total_price = 0
        for product, quantity in shopping_list:
            if quantity < 0:
                raise ValueError("Quantity can not be negative.")
            if quantity > product.get_quantity():
                raise ValueError("Requested quantity is not available.")
            total_price += product.buy(quantity)
        return total_price


