#program to check if the nth bit is set or not

def setOrNot(number,n):
    
    #make a mask variable by left shifting 1 (k-1) times and check if (n AND mask) equals to 1 or 0
    if number & (1 << (n - 1)):
        print("\nSET")
    else:
        print("\nNOT SET")

number = int(input("enter a number:"))
n = int(input("enter bit number:"))
setOrNot(number, n)