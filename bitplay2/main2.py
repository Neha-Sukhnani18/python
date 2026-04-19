#program to find the element not making a pair
#function to calculate the number that is odd occurring
def OddOccuring(arr):
    #initialize result
    res = 0
    #tanverse the array
    for element in arr:
        #XOR with the reult
        res = res^element
    return res

#initialize our array
arr =[]
#take array size as input
n = int(input("enter array size:"))

#take array element input
while(n):
    num= int(input("enter number:"))
    arr.append(num)
    n-=1

print("\n\nOdd occurring number is:",OddOccuring(arr))