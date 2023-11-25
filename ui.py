from inventory import Inventory
from storage import save_inventory, load_inventory

def get_item_input():
    item_id = int(input("Enter item ID: "))
    name = input("Enter item name: ")
    quantity = int(input("Enter item quantity: "))
    price = float(input("Enter item price: "))

    return {'id': item_id, 'name': name, 'quantity': quantity, 'price': price}


def main():
    inventory = load_inventory()
    if inventory is None:
        inventory = Inventory()

    while True:
        print("\n1. Add Item")
        print("2. Remove Item")
        print("3. Update Quantity")
        print("4. Search Item")
        print("5. Display Inventory")
        print("6. Save and Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            new_item = get_item_input()
            inventory.add_item(new_item)
            print("Itam added successfully.")
        elif choice == '2':
            item_id = int(input("Enter itam ID to remove: "))
            inventory.remove_item(new_item)
            print("Itam removed.")
        elif choice == '3':
            item_id = int(input("Enter item ID to update namber :"))
            inventory.remove_item(item_id)
            print("Namber of items are update.")
        elif choice == '4':
            kay = input("Enter the (name, id, e.g) :")
            value = input(f"Enter {kay} to search :")
            result = inventory.search_item(kay, value)
            print("Search result:")
            for itam in result:
                print(itam)
            pass
        elif choice == '5':
            inventory.display_inventory()
        elif choice == '6':
            save_inventory(inventory)
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
