import random

def pick_ball_experiments():
    #defining our balls as lists
    balls = ['Blue','Red','Green']

    #"flipping" coins randomly
    result = random.choice(balls)

    #finding out the probability
    pro = balls.count('Red')/len(balls)
    print("Probability of picking the red ball is:", pro)

    #checkinh if the red ball was picked
    if result == 'Red':
        return 'Red Ball Was Picked!'
    else:
        return 'Better Luck Next Time'

res = pick_ball_experiments() 
print(res) 