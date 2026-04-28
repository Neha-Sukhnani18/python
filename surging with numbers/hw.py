def is_power_of_eight(n):
    if n <= 0:
        return False
    while n % 8 == 0:
        n //= 8
    return n == 1

# Examples
print(is_power_of_eight(64))  # True (8^2)
print(is_power_of_eight(20))  # False
