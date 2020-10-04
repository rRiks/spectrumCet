# Write a python program to print all the prime number in a given interval and
# also check is the given input number is prime or not
n=int(input())
def prime(n):
    x=True
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            x=False
            break
    return x    
            
for i in range(2,n):
    if prime(i):
        print(i)
