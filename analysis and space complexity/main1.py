def prints(n):
    if n<=0:
        return
    print("Codingal")
    prints(n//2)
    prints(n//2)

#call the function
prints(8)
#this is n log n complexity because the output gives is high but the output is small and no matter how high the input gets the output value that will be given will always increase by a few digits therefore; showing that this is n log n complexity. 