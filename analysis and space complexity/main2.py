def sum_(n):
    return n * (n+1)//2 #integer result

print("sum of first n numbers (n=5):", sum_n(5))

def array_sum(a):
    total = 0
    for i in a:
        total+=i
    return total 
# examples

a=[12,3,4,15]
print("Array sum:", array_sum(a))
def summ(n):
    if n<=0:
        return 0
    return n+summ(n-1)

print("recursive sum (n=5):", summ(5))
#in the first piece of code the complexity is constant this is because the output remains the same and for the second piece of code the complexity is order of n as the number of input and output increase together
