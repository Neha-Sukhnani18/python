# Range for all 2-digit numbers
for num in range(10, 100):
    # Check for factors from 2 up to num-1
    for i in range(2, num):
        if (num % i) == 0:
            break
    else:
        # If no factors were found, the number is prime
        print(num, end=" ")
