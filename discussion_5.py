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
		most_stock = ''
		for i in range(len(self.items)):
			current_item = self.items[i]
			current_stock = current_item.stock
			if current_stock > most_stock:
				most_stock = current_item
		return most_stock.name
	
	# Returns the item in the warehouse with the highest price
	def get_max_price(self):
		highest_price = 0	
		for i in range(len(self.items)):
			current_item = self.items[i]
			current_price = current_item.price
			if current_price > highest_price:
				highest_price = current_item
		return highest_price

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


	## Check to see whether you can add an item to the warehouse
	def test_add_item(self):
		# Warehouse.add_item(self.item1, self.item2)
		# actual= Warehouse.print_items()
		# expect = {["Beer", "Cider"]}
		# self.assertEqual(actual, expect)
		pass

	## Check to see whether warehouse correctly returns the item with the most stock
	def test_warehouse_max_stocks(self):
		self.stock_list = [self.item1, self.item2, self.item3, self.item4]
		max_stock = Warehouse.get_max_stock(self.stock_list)
		expect = "Water"
		self.assertEqual(max_stock, expect)

	# Check to see whether the warehouse correctly return the item with the highest price
	def test_warehouse_max_price(self):
		pass
		

def main():
	unittest.main()

if __name__ == "__main__":
	main()