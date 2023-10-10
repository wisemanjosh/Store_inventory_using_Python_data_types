# An Inventory for a store
# Define some sample data using different data types

item_name = "Widget"  # String
item_price = 10.99  # Float
in_stock = 100  # Integer
is_on_sale = True # Boolean
features = ["Red", "Green", "Blue"]  # List
item_details = ("Small", "Plastic")  # Tuple
item_info = {"name": "item_name", "price": item_price, "stock": in_stock}  # Dictionary
item_set = {"Widget", "Gadget", "Doodad"}  # Set
item_review = None  # None

# Display the item's details
print("Item Name: ", item_name)
print("Price: ", item_price)
print("In Stock: ", in_stock)
print("On Sale: ", is_on_sale)
print("Available Colors:", features)
print("Details (Size, Material):", item_details)
print("Item Information:", item_info)
print("Available Items:", item_set)
print("Customer Review:", item_review)

# Update the stock
in_stock -= 10

# Add  a new item to the inventory
new_item = "Super Widget"
item_set.add(new_item)
print("Updated Available Items:", item_set)