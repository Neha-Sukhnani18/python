import math

def print_complexity(n):
    # O(n * log(n)) + O(1)
    # The dominant part is n * log(n)
    if n > 0:
        complexity_value = n * math.log2(n + 1)
        print(f"For n = {n}, total operations are approximately: {complexity_value:.2f}")
    print("Time Complexity: O(n log n)")

# Example usage
print_complexity(10)
