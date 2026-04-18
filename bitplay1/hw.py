import math

def get_rightmost_set_bit_position(n):
    # If the number is 0, there are no set bits
    if n == 0:
        return 0
    
    # Isolate the rightmost set bit using 2's complement property (n & -n)
    # Then use log2 to find its index and add 1 for 1-based positioning
    return int(math.log2(n & -n)) + 1

# Testing the code
test_cases = [8, 7]
for num in test_cases:
    pos = get_rightmost_set_bit_position(num)
    print(f"Enter number: {num} ({bin(num)[2:]})")
    print(f"Position of the first set bit: {pos}\n")
