def myfunction1(n):
    # Base Case: Stop if n is not greater than 0
    if n <= 0:
        return 
        
    # The (n + 1) work: Printing "Codingal" n+1 times
    for i in range(0, int(n) + 1):
        print("Codingal")
    
    # Recursive calls: T(n/2) and T(n/3)
    myfunction1(n / 2)
    myfunction1(n / 3)

# Example usage
# myfunction1(10)
def myfunction2(n):
    # Base Case: if n is 1 or less, stop recursion
    if (n <= 1):
        return
    
    # Constant work: printing the string
    print("Codingal")
    
    # Recursive Call: call the function with n-1
    myfunction2(n - 1)
