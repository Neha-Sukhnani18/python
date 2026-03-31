def multiply_n_iterations(m, n):
    """
    Multiplies m by n using n iterations of addition.
    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    if n < 0:
        m, n = -m, -n
    
    product = 0
    # The loop runs n times
    for _ in range(n):
        product += m
    return product

result_n = multiply_n_iterations(5, 3)
print(f"Result of 5 * 3 (n iterations): {result_n}")
