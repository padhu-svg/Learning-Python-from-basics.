#Write a program that:
#•	Accepts the user's age as input.
#•	Prints "Eligible to vote" if the age is 18 or older; otherwise, prints "Not eligible to vote."


print('Enter the age:')
a = int(input())

if a >= 18:
    print('Eligible to vote.')
else:
    print("Not eligible to vote")


#Output:
#Enter the age:
#18
#Eligible to vote.


#Enter the age:
#15
#Not eligible to vote