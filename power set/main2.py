#program to find the number of bits needed to be swapped to make 2 numbers equal

def totalFlips(number1,number2):
    #variable to count the flips required 
    flips=0
    #get the last bit of both numbers and check if both are same if yes no flip required else flip is required
    while(number1> 0 or number2 > 0):
        t1 = (number1 &1 )
        t2 = (number2 & 2)
        if (t1 !=t2):
            flips+=1

        #right shift both numbers
        number1>>=1
        number2>>=1

    return flips

number1 = int(input("enter first number:"))
number2 = int(input("enter second number:"))

print("\nNumber of flips needed:",totalFlips(number1,number2))

