def manage_menu():
    menu = input("Enter menu items separated by commas: ").split(',')
    add_item = input("Enter item to add: ")
    remove_item = input("Enter item to remove: ")
    check_item = input("Enter item to check: ")
    if remove_item in menu:
        menu.remove(remove_item)
    menu.append(add_item)
    print("Updated menu:", menu)
    if check_item in menu:
        print(check_item, "is available")
    else:
        print(check_item, "is not available")

if __name__ == "__main__":
    manage_menu()
