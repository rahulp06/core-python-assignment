def calculate_total():
    cart_items = {}
    count = int(input("Enter number of items: "))
    for i in range(count):
        item = input("Enter item name: ")
        price = int(input("Enter price: "))
        cart_items[item] = price
    if not cart_items:
        print("Cart is empty")
    else:
        total = sum(cart_items.values())
        if len(cart_items) > 5:
            total *= 0.9
        print("Total Price:", int(total))

if __name__ == "__main__":
    calculate_total()
