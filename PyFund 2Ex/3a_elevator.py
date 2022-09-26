from math import ceil

number_of_people = int(input())
capacity_of_elevator = int(input())

number_of_cources = ceil(number_of_people/capacity_of_elevator)
print(number_of_cources)