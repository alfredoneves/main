class Item:
	def __init__(self, name, quant, desc):
		self.name = name
		self.quant = quant
		self.desc = desc
	
	def change_quant(self, x):
		try:
			self.quant = x
		except:
			print("error to get the new quantity")
	def full_item(self):
		return self.name, self.quant, self.desc
		
def add_item(list1):
	try:
		name = input("type the name of the item: ")
		quant = int(input("type the quantity of the item: "))
		desc = input("type the description of the item: ")
		item = Item(name, quant, desc)
		list1.append(item)
		print("item added to the inventory")
	except:
		print("error to add item")

def remove_item(list1):
	try:
		name = input("type the name of the item to remove: ")
		for pos, item in enumerate(list1):
			if item.name == name:
				inventory.pop(pos)
	except:
		print("error to remove item")
		
def display(list1):
	try:
		for item in list1:
			print(item.full_item())
	except:
		print("error to display item")
		
def change_quantity(list1):
	try:
		name = input("type the name of the item to change the quantity: ")
		quantity = int(input("type the new quantity of the item: "))
		for pos, item in enumerate(list1):
			if item.name == name:
				item.change_quant(quantity)
	except:
		print("error to change the quantity")

item1 = Item("milk", 20, "soil milk")
inventory = [item1]

print("--- Here is the inventory. ---")
display(inventory)

while True:
	print("Options to make changes:")
	print("[1] add item")
	print("[2] display inventory")
	print("[3] change quantity")
	print("[4] remove item")
	print("[5] exit")
	option = input("type the number of the option: ")
	if option == "1":
		add_item(inventory)
	elif option == "2":
		display(inventory)
	elif option == "3":
		change_quantity(inventory)
	elif option == "4":
		remove_item(inventory)
	elif option == "5":
		break
	else:
		print("invalid option")
print("inventory closed!")

