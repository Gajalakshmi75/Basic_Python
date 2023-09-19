# factorial using recusrion
def factorial(n):
    if(n==0 or n==1):    #base case
        return 1
    else:                #recursive case
        return n*factorial(n-1)
n=int(input("enter a number:"))
result=(factorial(n))
print("Factorial of ",n,"is",result)
