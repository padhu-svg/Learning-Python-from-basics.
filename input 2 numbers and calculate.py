#Write a program that:
#•	Accepts two numbers and an operator (+, -, *, /) from the user.
#•	Performs the operation and prints the result.


print('Enter two numbers:')
a=int(input())
b=int(input())
print('Enter the operation:')
o = str(input())

if(o == '+'):
    o = a+b
    print('The sum of two numbers:', o)
elif(o == '-'):
    o = a-b
    print('The subtracton of two numbers:', o)  
elif(o == '*'):
    o = a*b
    print('The multiplicaton of two numbers:', o)   
elif(o == '/'):
    o = a/b
    print('The division of two numbers:', o)         
else:
    print('Error')    
