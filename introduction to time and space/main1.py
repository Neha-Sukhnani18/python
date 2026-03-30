def fun1(n):
    return n*(n+1)/2
print(fun1(4))
#since there is only one function taking place for this algorithm the number of iteration is one (4*5)/2

def fun2(n):
    sum=0

    for i in range(1,n+1):
        sum+=i

    return sum

print(fun2(4))
#for the second algorithm there is a loop that is also being run so the number of iterations will be four[1+1+1+1]/(1+2+3+4)
def fun3(n):
    sum=0

    for i in range(1,n+1):

        for j in range(1,n+1):
            sum+=1
    return sum
print(fun3(4))
#for the third algorithm there are 2 loops running(nested loop) therefore; the number of iterations will be ten(1+2+3+4) and the algorithm will look like: 1+(1+1)+(1+1+1)+(1+1+1+1)