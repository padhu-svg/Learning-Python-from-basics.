#Write a program to remove duplicate elements from a list.

print('Enter the list elements:')
a = list(map(int, input().split()))

dup = list(set(a))

print('After removing the duplicate items:',dup)


#Enter the list elements:
#5 5 5 8 90
#[8, 90, 5]