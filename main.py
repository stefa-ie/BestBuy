import products
import store

product_list = [ products.Product("MacBook Air M2", price=1450, quantity=100),
                 products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                 products.Product("Google Pixel 7", price=500, quantity=250)
               ]
best_buy = store.Store(product_list)

def start():
    while True:
        print("   Store Menu")
        print("   ----------")
        print("Welcome to Best Buy Store!")
        print("1. List all products in store")
        print("2. Show total amount in store")
        print("3. Make an order")
        print("4. Quit")

        choice = input("Please choose a number: ")
        print("------")

        if choice == "1":
            for index, product in enumerate(best_buy.get_all_products(), start=1):
                print(f"{index}. {product.show}")

start()
