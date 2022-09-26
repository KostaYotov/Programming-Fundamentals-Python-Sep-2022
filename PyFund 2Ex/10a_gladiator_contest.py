lost_fights = int(input())
price_of_helmet = float(input())
price_of_sword = float(input())
price_of_shield = float(input())
price_of_armor = float(input())
total_expense = 0

t_helmets_broken = lost_fights//2
t_swords_broken = lost_fights//3
t_shields_broken = lost_fights//6
t_armors_broken = lost_fights//12

total_expense = t_helmets_broken*price_of_helmet+\
    t_swords_broken*price_of_sword + t_shields_broken*price_of_shield +\
    t_armors_broken*price_of_armor
print(f"Gladiator expenses: {total_expense:.2f} aureus")