#program to find the number of bits present in a number
#functions taking our number as input
def numberOfBits(n):
    count=0
    #right shift the numer till its becomes 0
    while (n):
        count +=1
        n >>= 1
    return count
number = int(input("enter your number:"))
print("total bits :", numberOfBits(number))