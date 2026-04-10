number = int(input("input your number:"))
digits = len(str(number))
resultNumber = 0
temp = number
while temp > 0:
    digit = temp % 10
    reultNumber = digit ** digits+resultNumber
    temp//= 10

#display the reult
if number == reultNumber:
    print(number,"is an armstrong number")
else:
    print(number,"is not an armstrong number")