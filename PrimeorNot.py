# Write a python program to print all the prime number in a given interval and
# also check is the given input number is prime or not.


while True:
    n=int(input('enter any number : '))
    for i in range(1,n):
        if i>1:
            for j in range(2, i//2 + 2):
                if(i%j) == 0:
                    break
                else:
                    if j==i//2 + 1:
                        print(i)
    if n>1:
        for k in range (2,n):
            if(n%k==0):
                print('{} is not a prime number'.format(n))
                break
        else:
            print('{} is a prime number'.format(n))

else:
    print('{} is not a prime number'.format(n))

