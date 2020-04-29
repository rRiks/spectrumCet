#Accept n numbers from the user and calculate sum of all numbers
# between 1 and n including n.



n= int(input('enter an integer: '))
sum=0
for i in range(1,n+1):
    sum= sum + i
    i=i+1
print('sum of {0} integer is {1}'.format(n,sum))
