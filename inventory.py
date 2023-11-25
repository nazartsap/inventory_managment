class Inventory:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, item_id):
        self.items = [i for i in self.items if i['id'] != item_id]

    def update_quantity(self, item_id, new_quantity):
        for item in self.items:
            if item['id'] == item_id:
                item['quantity'] = new_quantity
                break

    def search_item(self, key, value):
        return [item for item in self.items if item.get(key) == value]

    def display_inventory(self):
        for item in self.items:
            print(item)

# Пример использования
if __name__ == "__main__":
    inventory = Inventory()
    item1 = {'id': 1, 'name': 'Product1', 'quantity': 10, 'price': 20.0}
    item2 = {'id': 2, 'name': 'Product2', 'quantity': 5, 'price': 15.0}

    inventory.add_item(item1)
    inventory.add_item(item2)

    inventory.display_inventory()
