def reverse_bits(n, bit_size=32):
    """
    Reverses all bits in a number for a given bit size (default 32).
    """
    result = 0
    for i in range(bit_size):
        # Shift result left to make space for the next bit
        result <<= 1
        # Extract the rightmost bit of n and add it to result
        result |= (n & 1)
        # Shift n right to process its next bit
        n >>= 1
    return result

# Example Usage
num = 5  # Binary: 00...0101
reversed_num = reverse_bits(num)
print(f"Original: {num} | Reversed: {reversed_num}")
