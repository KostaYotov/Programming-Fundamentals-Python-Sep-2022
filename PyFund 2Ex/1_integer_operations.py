# Write a program that reads four integer numbers. It should add the
# first to the second number, integer divide the sum by the third number,
# and multiply the result by the fourth number. Print the final result.

first_integer = int(input())
second_integer = int(input())
third_integer = int(input())
fourth_integer = int(input())
final_results = (first_integer+second_integer)//third_integer*fourth_integer

print(final_results)
