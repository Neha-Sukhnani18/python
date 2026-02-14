num = int(input("Enter a number: "))

temp = num
digit_sum = 0

n = len(str(num))

while temp > 0:
    digit = temp % 10

    digit_sum += digit ** n

    temp //= 10

if num == digit_sum:
    print(f"{num} is an Armstrong number.")
else:
    print(f"{num} is not an Armstrong number.")
