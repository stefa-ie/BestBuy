import products
import store


product_list = [ products.Product("MacBook Air M2", price=1450, quantity=100),
                 products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                 products.Product("Google Pixel 7", price=500, quantity=250)
               ]
best_buy = store.Store(product_list)


def making_order():
    """ Helper function for the menu/start (initialization function) """
    print("------")
    for index, product in enumerate(best_buy.get_all_products(), start=1):
        print(f"{index}. {product.show()}")
    print(("------"))
    print("When you want to finish order, enter empty text.")

    shopping_cart = []

    while True:
        select = input("Which product # do you want? ").strip()
        quantity = input("What amount do you want? ").strip()

        if not select or not quantity:
            if not shopping_cart:
                break

            total_payment = best_buy.order(shopping_cart)
            print("******** ")
            print(f"Order made! Total payment: ${total_payment}\n")

            for product, quantity in shopping_cart:
                if product.get_quantity() == 0:
                    product.deactivate()

            break

        try:
            select = int(select)
            quantity = int(quantity)
        except ValueError:
            continue

        if select < 1 or select > len(best_buy.get_all_products()):
            print("Error adding product!\n")
        else:
            selected_product = best_buy.get_all_products()[select - 1]
            if quantity > selected_product.get_quantity():
                print("Error while making order! Quantity larger than what exists\n")
            else:
                shopping_cart.append((selected_product, quantity))
                print("Product added to list!\n")


def start():
    """
    Within a while loop, user gets a menu to choose options 1-4 to
    interact with the Best Buy Store.
    """
    while True:
        print("   Store Menu")
        print("   ----------")
        print("Welcome to Best Buy Store!")
        print("1. List all products in store")
        print("2. Show total amount in store")
        print("3. Make an order")
        print("4. Quit")

        choice = input("Please choose a number: ")

        if choice == "1":
            print("------")
            for index, product in enumerate(best_buy.get_all_products(), start=1):
                print(f"{index}. {product.show()}")
        if choice == "2":
            print(f"Total of {best_buy.get_total_quantity()} items in store")
        if choice == "3":
            making_order()

        if choice == "4":
            return quit()

if __name__ == '__main__':
    start()
