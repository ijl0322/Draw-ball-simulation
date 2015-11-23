import random
def drawing_without_replacement_sim(numTrials):
    '''
    Runs numTrials trials of a Monte Carlo simulation
    of drawing 3 balls out of a bucket containing
    4 red and 4 green balls. Balls are not replaced once
    drawn. Returns a float - the fraction of times 3 
    balls of the same color were drawn in the first 3 draws.
    '''
    result = 0.0
    for i in range(numTrials):
        ball = ["G","G","G","G","R","R","R","R"]
        choice = []
        for i in range(3):
            select_ball = random.choice(ball)
            ball.remove(select_ball)
            choice.append(select_ball)
        
        if choice[0] == choice[1] and choice[1] == choice[2]:
            result += 1
    return result/numTrials    

print drawing_without_replacement_sim(5000)