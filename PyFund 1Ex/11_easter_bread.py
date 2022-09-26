# calculates how many loaves you can make with the budget you have.
# Eggs 1 pack, Flour	1 kg, Milk	0.250 l
# First, you will receive your budget. Then, you will receive the price for 1 kg flour.
# The price for 1 pack of eggs is 75% of the price for 1 kg flour.
# The price for 1L milk is 25% more than the price for 1 kg flour.
# Keep in mind that you use only 250ml milk for a bread.
# Start cooking the loaves and keep making them until you have enough budget.
# Keep in mind that:
# •	For every loaf of bread that you make, you will receive 3 colored eggs.
# •	For every 3rd bread you make, you will lose some of your colored eggs
# after receiving the usual 3 colored eggs for your bread.
# The count of eggs you will lose is calculated when you subtract
# 2 from your current count of loaves - ({current_bread_count} - 2)
budget = float(input())
price_of_flour = float(input())
price_pack_eggs = price_of_flour * 0.75
price_of_milk = price_of_flour * 1.25 / 4
breads_counter = 0
collored_eggs_counter = 0
bread_price = price_of_flour+price_of_milk+price_pack_eggs
while budget >= bread_price:
    if collored_eggs_counter < 0:
        break
    budget -= bread_price
    breads_counter +=1
    collored_eggs_counter += 3
    if breads_counter % 3 == 0:
        collored_eggs_counter -= (breads_counter -2)
print(f"You made {breads_counter} loaves of Easter bread! "\
      f"Now you have {collored_eggs_counter} eggs and {budget:.2f}BGN left.")