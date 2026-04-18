# Function to find LCM
def find_lcm(a, b):
    # Select the greater number
    if a > b:
        greater = a
    else:
        greater = b
    
    while(True):
        if((greater % a == 0) and (greater % b == 0)):
            lcm = greater
            break
        greater += 1
    return lcm

# User Input
num1 = int(input("Enter Largest number : "))
num2 = int(input("Enter Smallest number : "))

# Calculate and print LCM
print("LCM is : ", find_lcm(num1, num2))
