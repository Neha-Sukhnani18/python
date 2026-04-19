#program to find two numbers that are odd occurring

def printTwoOdd(arr, size):
    # xorof2 will hold xor of the 2 odd occurring numbers
    xorof2 = 0
    #these will hold 2 odd occurring numbers
    x=0
    y=0
    #this will hold the rightmost set bot from xorof2
    setbit=0

    for i in range(0,size):
        xoof2 = xorof2^arr[i]
    setbit = xorof2 &~(xorof2-1)
    #if number is having set bit at location we need then XOR it with x else y
    for i in range(size):
        if(arr[i]&setbit):
            x=y^arr[i]
        else:
            y=y^arr[i]
    print("the two ODD elemens are", x, "&",y)

#create an empty array
arr=[]
#take array size and elements as input
arr_size=int(input("enter size of the array:"))
for i in range(0,arr_size):
    z = int(input("enter element:"))
    arr.append(z)
printTwoOdd(arr,arr_size)
