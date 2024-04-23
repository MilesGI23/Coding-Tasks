Menu = ["burger", "sausage roll", "bacon bap", "steak bake" ]

stock = {}
stock["burger"] = 10
stock["sausage roll"] =25
stock["bacon bap"] = 20
stock["steak bake"] = 54

price = {}
price["burger"] = 3.95
price["sausage roll"] = 1.68
price["bacon bap"] = 1.59
price["steak bake"] = 1.99

total_stock = 0

for items in Menu:
    item_value = (stock[items] *price[items])
    total_stock += item_value

print(total_stock)