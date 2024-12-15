#Write a program that:
#•	Accepts a year as input.
#•	Checks and prints if it is a leap year. (A year is a leap year if it is divisible by 4 but not by 100, except if it is divisible by 400.)


print('Enter the year:')
y = int(input())

if (y % 4 == 0 and y % 100 != 0) or (y % 400 == 0):
    print(f"{y} is a leap year.")
else:
    print(f"{y} is not a leap year.")


#Output:
#Enter the year:
#2001
#2001 is not a leap year.