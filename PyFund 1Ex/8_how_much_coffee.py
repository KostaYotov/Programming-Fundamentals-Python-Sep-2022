# Until you receive the command "END", you need to read commands on
# different lines. According to the commands, calculate the number of coffees
# you need to drink to stay awake during the daytime.
# •	You have homework to do ("coding").
# •	You have a dog or a cat that decided to wake you up too early ("dog" or "cat").
# •	You watch a movie ("movie").
# •	If other events  Just ignore them!
# •	If it is lowercase, you need 1 coffee by an event.
# •	If it is uppercase, you need 2 coffees by an event.
# In the end, print the number of coffees you will need.
# If the count has exceeded 5, just print "You need extra sleep".
command = input()
coffee_counter = 0
while command != "END":
    if command.lower() == "coding" or command.lower() == "dog" or\
        command.lower() == "cat" or command.lower() == "movie":
        if command.islower():
            coffee_counter += 1
        else:
            coffee_counter += 2
    command = input()
if coffee_counter > 5:
    print("You need extra sleep")
else:
    print(coffee_counter)
