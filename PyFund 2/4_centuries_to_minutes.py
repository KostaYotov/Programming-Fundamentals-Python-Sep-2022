# Write a program that reads an integer number of centuries and
# converts it to years, days, hours, and minutes.

centuries = int(input())

years = centuries * 100
days = int(years * 365.2422)
hours = days * 24
minutes = hours * 60

print(f"{centuries} centuries = {years} years = {days} days = {hours} "
      f"hours = {minutes} minutes")
