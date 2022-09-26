# Write a program to read an integer N and print all triples of the
# first N small Latin letters, ordered alphabetically:

number_of_letters = int(input())

for first_symbol in range (number_of_letters):
    for second_symbol in range (number_of_letters):
        for third_symbol in range (number_of_letters):
            print(f"{chr(97+first_symbol)}{chr(97+second_symbol)}"
                  f"{chr(97+third_symbol)}")

