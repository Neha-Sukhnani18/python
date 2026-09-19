from scipy.stats import binom
n=10
p=0.5
k_values = [2,3,4]

probability = sum(binom.pmf(k,n,p) for k in k_values)

print(f"the probability is: {probability:.4f}")