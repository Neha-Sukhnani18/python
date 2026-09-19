def prob_a_and_b(a,b, total):
    #probability of event a 
    prob_a = orange/total

    #pobability of event b
    prob_bga = blue/(total-1)

    #probability
    prob_AandB = prob_a * prob_bga

    #add return statement
    return round(prob_AandB, 3)


#taking input
orange = int(input("enter the number of orange balls"))
blue = int(input("enter the number of blue balls"))
total = orange + blue


#call
print('Probability of getting 1st orange and 2nd blue ball:')
print(prob_a_and_b(orange, blue, total))