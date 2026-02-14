n_terms = int(input("Enter the number of terms: "))

a = 0  
b = 1  
count = 0

if n_terms <= 0:
    print("Please enter a positive integer.")
elif n_terms == 1:
    print(f"Fibonacci sequence: {a}")
else:
    print("Fibonacci sequence:")

    while count < n_terms:
        print(a, end=" ")
        
        
        nth = a + b 
        
        a = b     
        b = nth  
        count += 1
