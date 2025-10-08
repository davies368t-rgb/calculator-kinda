def add(a,b):
    return(a+b)
def sub(a,b):
    return(a-b)
def mul(a,b):
    return(a*b)
def div(a,b):
    return(a/b)

a=int(input("enter 1st number: "))
b=int(input("enter 2nd number: "))
c=input("enter a for +, s for -, m for * and d for /. ")

if c == "a":
    result=add(a,b)
elif c == "s":
    result=sub(a,b)
elif c == "m":
    result=mul(a,b)
elif c == "d":
    result=div(a,b)
print(result)