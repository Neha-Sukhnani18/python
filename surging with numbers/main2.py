#program to check if a number is a power of 4 or not
def powerof4(number):

    count=0

    #if only 1 set bit exists
    if(number&(~(number&(number-1)))):
        
        #count 0 bits before set bit
        while(number>1):
            number>>=1
            count+=1

        #if count is even return true else false
        if(count % 2 == 0):
            return True
        else:
            return False
        
number=int(input("enter a number:"))
if(powerof4(number)):
    print(number,'is a power of 4.')
else:
    print(number,'is not a power of 4.')
