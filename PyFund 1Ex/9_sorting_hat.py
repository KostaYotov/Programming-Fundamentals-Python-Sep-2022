# Help out the sorting hat to sort the new students in the houses
# of Hogwarts. You will be receiving names until the command "Welcome!".
# The length of each name determines in which house the student is going:
# •	If the name is less than 5 chars, the student is going into Gryffindor
# o	Print "{name} goes to Gryffindor."
# •	If the name is exactly 5 chars, the student is going into Slytherin
# o	Print "{name} goes to Slytherin."
# •	If the name is exactly 6 chars, the student is going into Ravenclaw
# o	Print "{name} goes to Ravenclaw."
# •	If the name is more than 6 chars, the student is going into Hufflepuff
# o	Print "{name} goes to Hufflepuff."
name = input()
whole_list = False
while name != "Welcome!":
    if name == "Voldemort":
        print("You must not speak of that name!")
        break
    if len(name) < 5:
        print(f"{name} goes to Gryffindor.")
    if len(name) == 5:
        print(f"{name} goes to Slytherin.")
    if len(name) == 6:
        print(f"{name} goes to Ravenclaw.")
    if len(name) > 6:
        print(f"{name} goes to Hufflepuff.")
    name = input()
if name == "Welcome!":
    print("Welcome to Hogwarts.")