# Write a program that reads an integer n. Then, for all numbers
# in the range [1, n], prints the number and if it is special or
# not (True / False). A number is special when the sum of its digits is 5, 7,
# or 11.

last_integer = int(input())

for number in range (1, last_integer +1):
    new_number = 0
    figure = str(number)
    length = len(figure)
    for i in range (length):
        new_number += int(figure[i])
        continue
    if new_number % 5 == 0 or new_number % 7 == 0 or new_number % 11 == 0:
        print(f"{number} -> True")
    else:
        print(f"{number} -> False")