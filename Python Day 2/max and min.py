#Find Maximum and Minimum: Take a list of numbers as input and find the maximum and minimum numbers.

print("Enter the list of numbers:")
a = list(map(int,input().split()))
print("The listed item is: ", a)

maximum = max(a)
minimum = min(a)

print("The maximum number of the list is", maximum)
print("The minimum number of the list is", minimum)

#Output:
#Enter the list of numbers:
#5 6 70
#The listed item is:  [5, 6, 70]
#The maximum number of the list is 70
#The minimum number of the list is 5