#Write a program that:
#•	Takes three numbers as input.
#•	Prints the largest number using if statements.


print('Enter three numbers:')
a = int(input())
b = int(input())
c = int(input())

if a > b >c:
    print('The is the largest number:', a)
elif b > a > c:
    print('The is the largest number:', b)
elif c > b > a:
    print('The is the largest number:', c)   
else:
    print('All number is equal')     

    

