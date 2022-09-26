# Calculate how many courses will be needed to elevate N persons by using
# an elevator with a capacity of P persons. The input holds two lines:
# the number of people N and the capacity P of the elevator.
# if capacity_of_elevator % number_of_people == 0:
#     print(number_of_courses)
# else:
#     number_of_courses += 1
# print(number_of_courses)
number_of_people = int(input())
capacity_of_elevator = int(input())

number_of_courses = number_of_people//capacity_of_elevator
if number_of_people % capacity_of_elevator  == 0:
    print(number_of_courses)
else:
    number_of_courses += 1
    print(number_of_courses)



# if capacity_of_elevator % number_of_people != 0:
#     number_of_courses += 1
# print(number_of_courses)

