#Swap Two Numbers:
#Write a program to swap the values of two variables without using a third variable.

print(' Enter 2 numbers:')
a , b = int(input()), int(input())
temp = int

temp = a
a = b
b = temp
print("After swapping:")
print("a =", a, "b =", b)


#Output:
# Enter 2 numbers:
#10 
#15
#After swapping:
#a = 15 b = 10