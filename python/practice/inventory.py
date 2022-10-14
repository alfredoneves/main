# items with name, quantity and description
item0 = {"name": "bread", "quant": 100, "description": "french bread"}
item1 = {"name": "cheese", "quant": 40, "description": "chedar cheese"}
item2 = {"name": "cake", "quant": 20, "description": "chocolate cake"}

# master inventory list
inventory = [item0, item1, item2]

# function to add an item
def add_item():
	name = input("type the name of the item: ")
	quant = int(input("type the quantity of the item: "))
	description = input("type the description of the item: ")
	item = {"name": name, "quant": quant, "description": description}
	inventory.append(item)
	print("item added to the inventory")
	
# function to display the inventory in a readable format
def display():
	for item in inventory:
		print(item)

# function to change the quantity of an item
def change_quantity():
	name = input("type the name of the item: ")
	new_quant = int(input("type the new quantity of the item: "))
	for item in inventory:
		if item["name"] == name:
			item["quant"] = new_quant
			return True

# function to remove an item from the list
def remove_item():
	name = input("type the name of the item to remove: ")
	for pos, item in enumerate(inventory):
		if item["name"] == name:
			inventory.pop(pos)

print("Here is the inventory.")
display()
while True:
	print("Options to make changes:")
	print("[1] add item")
	print("[2] display inventory")
	print("[3] change quantity")
	print("[4] remove item")
	print("[5] exit")
	option = input("type the number of the option: ")
	if option == "1":
		add_item()
	elif option == "2":
		display()
	elif option == "3":
		change_quantity()
	elif option == "4":
		remove_item()
	elif option == "5":
		break
	else:
		print("invalid option")
print("inventory closed!")

