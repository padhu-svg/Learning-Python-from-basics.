#Write a program that:
#•	Takes a number between 0 and 100 as input.
#•	Prints the grade based on the following:
#	90-100: A
#	80-89: B
#	70-79: C
#	60-69: D
#	Below 60: Fail

print('Enter the Marks:')
m = int(input())

if m >= 90:
    print('Your grade is A')
elif m >= 80:
    print('Your grade is B')   
elif m >= 70:
    print('Your grade is C')  
elif m >= 60:
    print('Your grade is D')          
else:
    print('Fail')

#Output:
#Enter the Marks:
#71
#Your grade is C

#Output:
#Enter the Marks:
#60
#Fail