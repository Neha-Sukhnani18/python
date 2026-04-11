#taking a input from the user
number = int(input("enter a number"))

#store the number given by the user for comparison
original_number=number
reversed_number=0
#reverse(turn the number the other way round) the number
while number > 0:
    digit = number % 10
    reversed_number = reversed_number * 10 + digit
    number //=10

#now you check if the original number(the number given by the user) and the number that you have reversed are the same or not
if original_number == reversed_number:
    print(f"{original_number} is a palidrome number")

else:
    print(f"{original_number} is not a palidrome number")