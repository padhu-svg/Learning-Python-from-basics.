print('Enter the marks of  subjects')
m1,m2,m3,m4,m5 = int(input()),int(input()),int(input()),int(input()),int(input())
total,avg,grade = int, int, int

total = (m1+m2+m3+m4+m5)
avg = total/5
print('The total marks is:',total)
print('The average is:', avg)
if(avg >= 85):
    print('Your grade is Distinction.')
elif(avg >= 60):
    print('Your grade is first class.')
elif(avg >= 50):
    print('Your grade is second class.')
elif(avg >= 35):
    print('Your grade is pass.')
else:
    print('Your grade is fail')