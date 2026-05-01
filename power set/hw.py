def get_all_substrings(s):
    # Length of the string
    n = len(s)
    
    # Nested list comprehension to slice from every i to every j
    return [s[i:j] for i in range(n) for j in range(i + 1, n + 1)]

# Example usage:
my_string = "abc"
print(get_all_substrings(my_string))
# Output: ['a', 'ab', 'abc', 'b', 'bc', 'c']
