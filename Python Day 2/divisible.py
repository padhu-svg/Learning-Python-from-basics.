#Divisibility Check:
#Check if a number entered by the user is divisible by 5 and 11.

print('Enter the number:')
a = int(input())

if (a % 5 == 0 and a % 11 == 0):
    print('the number is divisible by 5 and 11.')
else:
    print('The number is not divisible b 5 and 11.')


#Output:
#Enter the number:
#55
#the number is divisible by 5 and 11.