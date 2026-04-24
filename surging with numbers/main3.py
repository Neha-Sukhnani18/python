#program to computer x^y without using math function


def computerPower(x,y):
    #default total is 1
    result = x
    while(y>1):
        result = result * x#8
        y=y-1
    return result

x = int(input("enter x for x^y:"))
y = int(input("enter y for x^y:"))
print("total:",(computerPower(x,y)))