# You will receive a group size. After that, you receive the days of
# the adventure.
# Every day, you earn 50 coins, but you also spend 2 coins per companion for food.
# Every 3rd (third) day, you organize a motivational party, spending 3 coins
# per companion for drinking water.
# Every 5th (fifth) day, you slay a boss monster and gain 20 coins per companion. But
# if you have a motivational party the same day, you spend additional 2 coins per companion.
# Every 10th (tenth) day at the start of the day, 2 (two) of your companions leave,
# but every 15th (fifteenth) day 5 (five) new companions are joined at the beginning
# of the day.
# You should calculate how many coins gets each companion at the end of the adventure
companions = int(input())
days_of_adventures = int(input())
total_coins = 0
for current_day in range(1, days_of_adventures+1):
    if current_day % 10 == 0:
        companions -= 2
    if current_day % 15 == 0:
        companions += 5
    if current_day % 3 == 0:
        total_coins -= 3 * companions
    if current_day % 5 == 0:
        total_coins += 20 * companions
        if current_day % 3 == 0:
            total_coins -= 2 * companions
    total_coins += 50
    total_coins -= 2 * companions
coins_per_companion = int(total_coins / companions)
print(f"{companions} companions received {coins_per_companion} coins each.")
