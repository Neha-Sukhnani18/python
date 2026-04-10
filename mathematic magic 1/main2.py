#to find the factors of user input

#goes from 1 to number and checks if i divide the number. if yes, it is a factor
def print_factors(number):
    print("the factors of",number,"are:")
    for i in range(1, number+1):
        if number % i == 0:
            print(i)

#taking input from the user
number = int(input("Enter your number to find its factors:"))

#calling our function 
print_factors(number)