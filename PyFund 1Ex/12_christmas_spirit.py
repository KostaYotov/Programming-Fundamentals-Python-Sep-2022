quantity_of_decorations = int(input())
days_till_christmas = int(input())
budget = 0
spirit = 0
ornaments_set_price = 2
tree_skirt_price = 5
tree_garland_price = 3
tree_lights = 15
for current_day in range (1, days_till_christmas+1):
    if current_day % 11 == 0:
        quantity_of_decorations += 2
    if current_day % 2 == 0:
        budget += ornaments_set_price*quantity_of_decorations
        spirit += 5
    if current_day % 3 == 0:
        budget += (tree_skirt_price+ tree_garland_price)*quantity_of_decorations
        spirit += 3 + 10
    if current_day % 5 == 0:
        budget += tree_lights*quantity_of_decorations
        spirit += 17
        if current_day % 3 == 0:
            spirit += 30
    if current_day % 10 == 0:
        spirit -= 20
        budget += tree_lights + tree_garland_price +  tree_skirt_price
if current_day % 10 == 0:
    spirit -= 30
print(f"Total cost: {budget}")
print(f"Total spirit: {spirit}")



