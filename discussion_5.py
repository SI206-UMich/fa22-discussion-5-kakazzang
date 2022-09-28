import unittest

# Counts the number of a's in a sentence (e.g., a string)
def count_a(sentence):
	total = 0
	for i in range(len(sentence) - 1):
		if sentence[i] == 'a':
			total += 1
	return total


# Item class
# Describes an item to be sold. Each item has a name, a price, and a stock.
class Item:
	# Constructor.
	def __init__(self, name, price, stock):
		self.name = name
		self.price = price
		self.stock = stock

	# Print
	def __str__(self):
		return ("Item = {}, Price = {}, Stock = {}".format(self.name, self.price, self.stock))

# Warehouse class
# A warehouse stores items and manages them accordingly.
class Warehouse:

	# Constructor
	def __init__(self, items = []):
		self.items = items[:]

	# Prints all the items in the warehouse, one on each line.	
	def print_items(self):
		for item in self.items:
			print(item)
			print("\n")	

	# Adds an item to the warehouse	
	def add_item(self, item):
		self.items.append(item)

	# Returns the item in the warehouse with the most stock		
	def get_max_stock(self):
		most_stock = 0
		most_item = None
		for i in range(len(self.items)):
			current_item = self.items[i]
			current_stock = current_item.stock
			if current_stock > most_stock:
				most_stock = current_stock
				most_item = current_item
		return most_item

	# Returns the item in the warehouse with the highest price
	def get_max_price(self):
		highest_price = 0
		highest_item = None	
		for item in self.items:
			if item.price > highest_price:
				highest_price = item.price
				highest_item = item
		return highest_item

# Tests
class TestAllMethods(unittest.TestCase):

	# SetUp -- we create a bunch of items for you to use in your tests.
	def setUp(self):
		self.item1 = Item("Beer", 6, 20)
		self.item2 = Item("Cider", 5, 25)
		self.item3 = Item("Water", 1, 100)
		self.item4 = Item("Fanta", 2, 60)
		self.item5 = Item("CocaCola", 3, 40)

	## Check to see whether count_a works
	def test_count_a(self):
		total_a1 = count_a('apple')
		self.assertEqual(total_a1, 1)
		total_a2 = count_a('ahahah')
		self.assertEqual(total_a2, 3)
		total_a3 = count_a('bbb')
		self.assertEqual(total_a3, 0)

	## Check to see whether you can add an item to the warehouse
	def test_add_item(self):
		w1 = Warehouse()
		w1.add_item(self.item1)
		w1.add_item(self.item2)
		self.assertEqual(w1.items, [self.item1, self.item2])
		w1.add_item(self.item3)
		self.assertEqual(w1.items, [self.item1, self.item2, self.item3])
		w1.add_item(self.item4)
		self.assertEqual(w1.items, [self.item1, self.item2, self.item3, self.item4])
		

	## Check to see whether warehouse correctly returns the item with the most stock
	def test_warehouse_max_stocks(self):
		w1 = Warehouse()
		w1.items = [self.item1, self.item2, self.item3, self.item4]
		self.assertEqual(w1.get_max_stock(), self.item3)
		w1.items = [self.item5, self.item2, self.item4]
		self.assertEqual(w1.get_max_stock(), self.item4)
		w1.items = [self.item1, self.item2]
		self.assertEqual(w1.get_max_stock(), self.item2)
		w1.items = [self.item1, self.item5]
		self.assertEqual(w1.get_max_stock(), self.item5)
		

	# Check to see whether the warehouse correctly return the item with the highest price
	def test_warehouse_max_price(self):
		w1 = Warehouse()
		w1.items = [self.item1, self.item2, self.item3, self.item4]
		self.assertEqual(w1.get_max_price(), self.item1)
		w1.items = [self.item5, self.item2, self.item4]
		self.assertEqual(w1.get_max_price(), self.item2)
		w1.items = [self.item1, self.item2]
		self.assertEqual(w1.get_max_price(), self.item1)
		w1.items = [self.item3, self.item4]
		self.assertEqual(w1.get_max_price(), self.item4)
		

def main():
	unittest.main()

if __name__ == "__main__":
	main()