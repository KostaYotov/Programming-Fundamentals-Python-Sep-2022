# create a program that greets the user when he/she gives his/her name
# in the format "Hello, {name}!". However, Jenny is in love with Johnny and
# would like to greet him differently: "Hello, my love!"

name = input()

if name == "Johnny":
    print("Hello, my love!")
else:
    print(f"Hello, {name}!")