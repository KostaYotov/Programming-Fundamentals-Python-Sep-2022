# Thus, you want to know the price of each order. On the first line, you will receive
# integer N - the number of orders the shop will receive. For each order, you will receive
# the following information:
# •	Price per capsule - a floating-point number in the range [0.01…100.00]
# •	Days - integer in the range [1…31]
# •	Capsules, needed per day - integer in the range [1…2000]
# For each order, you should print a single line in the following format:
# •	"The price for the coffee is: ${price}"
number_of_orders = int(input())
total_price = 0
for order in range(number_of_orders):
    price_per_capsule = float(input())
    days = int(input())
    capsules_per_day = int (input())
    if price_per_capsule < 0.01 or price_per_capsule > 100:
        continue
    elif days < 1 or days > 31:
        continue
    elif capsules_per_day < 1 or capsules_per_day > 2000:
        continue
    order_price = price_per_capsule*capsules_per_day*days
    total_price += order_price
    print(f"The price for the coffee is: ${order_price:.2f}")
print(f"Total: ${total_price:.2f}")