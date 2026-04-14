#program to check if given number is prime or not

from math import sqrt

number = int(input("enter your number:"))
print("\n")

# if given number is greater then 1
if number > 1:

    #check if number is divisible from 2 to number/2
    for i in range(2, int(sqrt(number))+1):

        # if divisible by any nymber it is not a prime number
        if (number % i) == 0:
            print(number,"is not a prime number")
            break
    else: 
        print(number, "is a prime number")

else:
    print(number,"is not a prime number")