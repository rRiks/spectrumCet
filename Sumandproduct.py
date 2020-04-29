# Accept two numbers from the user and return their product
# and if the product is greater than 1000,return their sum.


a=int(input('enter first no: '))
b=int(input('enter 2nd no: '))
c = a*b
d= a+b
print('product is {}'.format(c))
if c>1000:
    print('sum is {}'.format(d))