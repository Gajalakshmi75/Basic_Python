#factorial program using functions
def factorial(num): #function defintion
    fact=1
    for i in range(1,num+1):
        fact=fact*i
        return fact
    
number=int(input("enter a number:"))
result=factorial(number)
print("Factorial is %d=%d"%(number,result))
