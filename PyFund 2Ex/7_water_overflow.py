# You have a water tank with a capacity of 255 liters. On the first line,
# you will receive n – the number of lines, which will follow. On the following
# n lines, you will receive liters of water (integers), which you should pour
# into your tank. If the capacity is not enough, print "Insufficient capacity!"
# and continue reading the next line. On the last line, print the liters in the tank.

tank_capacity = 255
litters_in_tank = 0
number_lines = int(input())

for number_of_pouring in range(number_lines):
    current_pouring = int(input())
    if tank_capacity - current_pouring < 0:
        print("Insufficient capacity!")
        continue
    tank_capacity -=current_pouring
    litters_in_tank += current_pouring
print(litters_in_tank)



