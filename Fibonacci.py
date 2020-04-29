# Write a python program to print the Fibonacci series and also check is a given
# input is a Fibonacci number or not.


n1=0
n2=1
count=0
length=int(input('enter the length of Fibonacci series :'))
if length<=0:
    print('enter a positive integer')
elif length==1:
    print('Fibonacci series will be : {}'.format(n1))
else:
    print('Fibonacci series will be : ')
    while count < length:
        print(n1)
        n3=n1 + n2
        n1 = n2
        n2 = n3
        count += 1

import math
def perfectsquare(x):
   s = int(math.sqrt(x))
   return s*s == x
def isFibonacci(n):
   return perfectsquare(5*n*n + 4) or perfectsquare(5*n*n - 4)
y = int(input('Enter the number you want to check: '))
if (isFibonacci(y) == True):
    print (y,"is a Fibonacci Number")
else:
    print (y,"is a not Fibonacci Number")