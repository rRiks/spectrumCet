# Given a number, count the total number of digits in it.



x= int(input('The given number is : '))
X=str(x)
length=len(X)
print('length of the given number {0} is {1}.'.format(x,length))



# or
def countDigit(n): 

    if n == 0: 

        return 0

    return 1 + countDigit(n // 10) 

n = int(input('enter any number :'))

print ("Number of digits : % d"%(countDigit(n))) 