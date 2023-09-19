def functionname(a,b):
    return a+b
w=functionname(5,7)
print(w)

def functionname(a):
    return a*3
print(functionname(3))


def functionname(a):
    for i in a:
        print(i)
functionname([1,2,3,4,5,6,7])

#arbitrary arguments
def functioname(**a):
    print(a)
functioname(name="lakshmi",age=19)

#function definition:
def functionname(*a):
    for i in a:
        print(i)
functionname(1,2,3,4,5,6,7,8,9,10) #calling function
