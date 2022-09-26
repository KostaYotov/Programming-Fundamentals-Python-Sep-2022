# You will receive Peter's lost fights count.
# Every second lost game, his helmet is broken.
# Every third lost game, his sword is broken.
# When both his sword and helmet are broken in the same lost fight, his shield
# also breaks.
# Every second time his shield brakes, his armor also needs to be repaired.
# You will receive the price of each item in his equipment. Calculate his expenses
# for the year for renewing his equipment.
# •	As output, you must print Peter`s total expenses for new equipment: ""
# "Gladiator expenses: {expenses} aureus"
lost_fights = int(input())
price_of_helmet = float(input())
price_of_sword = float(input())
price_of_shield = float(input())
price_of_armor = float(input())
total_expense = 0
for current_fight in range (1, lost_fights+1):
    if current_fight % 2 == 0:
        total_expense += price_of_helmet
    if current_fight % 3 == 0:
        total_expense += price_of_sword
    if current_fight % 6 == 0:
        total_expense += price_of_shield
    if current_fight % 12 == 0:
        total_expense += price_of_armor
print(f"Gladiator expenses: {total_expense:.2f} aureus")

