#Write a program that:
#•	Accepts a number as input.
#•	Prints its multiplication table from 1 to 10.

print('Enter the number to get the multiplication table:')

n = int(input())

for i in range(1,11):
    print(f'{n} * {i} = ({n} * {i})')


#Output:
# Enter the number to get the multiplication table:
#5
#5 * 1 = (5 * 1)
#5 * 2 = (5 * 2)
#5 * 3 = (5 * 3)
#5 * 4 = (5 * 4)
#5 * 5 = (5 * 5)
#5 * 6 = (5 * 6)
#5 * 7 = (5 * 7)
#5 * 8 = (5 * 8)
#5 * 9 = (5 * 9)
#5 * 10 = (5 * 10)    