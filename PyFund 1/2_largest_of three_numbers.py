# Write a program that receives three whole numbers and prints the largest one.

# first_number, second_number, third_number = int (input()), int(input()),\
#                                             int(input())
# print(max (first_number, second_number, third_number))
# # print(min (first_number, second_number, third_number))

first_number = int (input())
second_number = int (input())
third_number =  int(input())

if first_number > second_number and first_number > third_number:
    print(first_number)
elif second_number > first_number and second_number > third_number:
    print(second_number)
else:
    print(third_number)

