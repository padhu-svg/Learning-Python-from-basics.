#Write a program that:
#•	Takes a number as input.
#•	Checks and prints whether the number is positive, negative, or zero.

print('Enter the number:')
a = int(input())
if a > 0:
    print('The integer is positive.')
elif a == 0:
    print('The number is zero')    
else:
    print("The integer is negative")    

#Output:
#Enter the number:
#-4
#The integer is negative

#Enter the number:
#5
#The integer is positive.

#Enter the number:
#0
#The number is zero