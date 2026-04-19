#program to check if user input numbers are equal without using any comparision operator.
def checkIfSame(number1, number2):

# user XOR operator as a^a is always 0
 if ((number1^number2)!=0):
  print("numbers are not equal")
 else:
  print("both numbers are equal")

#taking input
number1 = int(input("enter the first number to compare:" ))
number2= int(input("enter the second number to compare:"))

checkIfSame(number1, number2)