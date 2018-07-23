a=int(input("enter value"))
b=int(input("enter value"))

val=int(input("enter the method"))
def add(x,y):
    return x+y

def sub(x,y):
    return x-y

def div(x,y):
    return x/y

def mul(x,y):
    return x*y

switch={1:add, 2:sub, 3:mul, 4:div}
switch[val](a,b)