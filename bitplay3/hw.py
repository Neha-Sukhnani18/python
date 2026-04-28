def longest_consecutive_ones(n):
    count = 0
    # Repeatedly reduce every run of 1s by one bit until n becomes 0
    while n != 0:
        n = n & (n << 1)
        count += 1
    return count

# Example usage
num = 14  # Binary: 1110
print(f"Longest consecutive 1s in {num}: {longest_consecutive_ones(num)}") # Output: 3
