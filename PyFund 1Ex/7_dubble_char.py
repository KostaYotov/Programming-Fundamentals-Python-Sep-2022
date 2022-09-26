# You will be given strings until you receive the command "End". For
# each string given,# you should print a string in which each character
# (case-sensitive) is repeated twice.
# Note that if you receive the string "SoftUni", you should NOT print it!

current_string = input()
while current_string != "End":
    if current_string =="SoftUni":
        current_string = input()
        continue
    for char in current_string:
        print(char+char, end ="")
    print()
    current_string = input()



