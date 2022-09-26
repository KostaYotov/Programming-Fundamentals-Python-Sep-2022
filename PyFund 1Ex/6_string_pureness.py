# You will be given number n. After that, you'll receive different strings n times. '
# 'Your task is to check if the given strings are pure, meaning that they do NOT consist of '
# 'any of the characters: comma ",", period ".", or underscore "_":
# •	If a string is pure, print "{string} is pure."
# •	Otherwise, print "{string} is not pure!"
number_of_strings = int(input())
for _ in range (number_of_strings):
    current_string = input()
    if "," in current_string or "." in current_string or "_" in current_string:
        print(f"{current_string} is not pure!")
    else:
        print(f"{current_string} is pure.")

