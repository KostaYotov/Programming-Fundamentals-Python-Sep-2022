# N – an integer, the number of snowballs being made by Tony and Andi.
# On the following lines, you will receive 3 inputs for each snowball:
# •	The weight of the snowball (integer).
# •	The time needed for the snowball to get to its target (integer).
# •	The quality of the snowball (integer).
# For each snowball, you must calculate its value by the following formula:
# (snowball_weight / snowball_time) ** snowball_quality
# In the end, you must print the highest calculated value of a snowball.
number_of_balls = int(input())
max_weight = 0
max_time = 0
max_quality = 0
max_value = 0
for current_snowball in range (number_of_balls):
    current_weight = int(input())
    current_time = int(input())
    current_quality = int(input())
    current_value = (current_weight/current_time)**current_quality
    if current_value > max_value:
        max_weight = current_weight
        max_time = current_time
        max_quality = current_quality
        max_value = current_value
print(f"{max_weight} : {max_time} = {int(max_value)} ({max_quality})")