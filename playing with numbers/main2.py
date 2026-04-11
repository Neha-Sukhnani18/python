#program to find HCF/GCD

#enter 2 numbers

numberLargest= int(input("enter largest number:"))
numberSmallest=int(input("enter smallest number:"))

#using eucliden algorithms
while(numberSmallest):
    numberStore = numberSmallest
    numberSmallest = numberLargest % numberSmallest
    numberLargest= numberStore
     
print("HCF is: ",numberLargest)