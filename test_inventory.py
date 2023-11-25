import unittest
from inventory import Inventory

class TestInventory(unittest.TestCase):
    def setUp(self):
        self.inventory = Inventory()
        self.item1 = {'id': 1, 'name': 'Product1', 'quantity': 10, 'price': 20.0}
        self.item2 = {'id': 2, 'name': 'Product2', 'quantity': 5, 'price': 15.0}
        self.inventory.add_item(self.item1)
        self.inventory.add_item(self.item2)

    def test_add_item(self):
        new_item = {'id': 3, 'name': 'Product3', 'quantity': 8, 'price': 25.0}
        self.inventory.add_item(new_item)
        self.assertIn(new_item, self.inventory.items)

    def test_remove_item(self):
        item_id = 1
        self.inventory.remove_item(item_id)
        self.assertNotIn(self.item1, self.inventory.items)

    def test_update_quantity(self):
        item_id = 2
        new_quantity = 7
        self.inventory.update_quantity(item_id, new_quantity)
        updated_item = next(item for item in self.inventory.items if item['id'] == item_id)
        self.assertEqual(updated_item['quantity'], new_quantity)

    def test_search_item(self):
        key = 'name'
        value = 'Product1'
        result = self.inventory.search_item(key, value)
        self.assertIn(self.item1, result)
        self.assertNotIn(self.item2, result)

if __name__ == '__main__':
    unittest.main()
