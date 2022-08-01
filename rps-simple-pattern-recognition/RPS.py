import random
opp = {} # general pattern dict
ct_ms = {'R':'P', 'P':'S', 'S':'R'} # counter moves

def player(prev_play, opponent_history=[],player_history=[]):
    ms = ['R','S','P'] # possible moves
    guess = 'R'
    if prev_play == "":
        prev_play = 'R'
        
    opponent_history.append(prev_play) # track opponent's move
    
    if len(opponent_history) > 4: # pattern of this length
        
        pb = playbook(opponent_history) # add the pattern
        
        pattern = "".join(opponent_history[-4:]) # get current pattern
        potential = [pattern+ms[0],pattern+ms[1],pattern+ms[2]]
        
        for pattern in potential:
            if not(pattern in opp.keys()): #check if pattern exists
                opp[pattern] = -1 #delay the importance if not exists

        # predict the next move and counter it
        guess = predict(opp,potential,player_history) 
        
    coeff = check_my_moves(opponent_history, player_history)
    
    if coeff >= 0.4: #random threshold value but 0.4 is best working
         guess = ct_ms[ct_ms[player_history[-1]]] # rotate by 2 
                                                
    player_history.append(guess) # keep track of our moves
    return guess

def playbook(opponent_history):
    key = "".join(opponent_history[-5:]) # get last 5 moves
    if not(key in opp.keys()): # check if in dict
        opp[key] = 1 # create if not
    else:
        opp[key] += 1 # increase if
        
    return opp

def predict(opp,pot,player_history):
    predict = max(pot, key=lambda key: opp[key])
    if predict[-1] == "P":
        guess = ct_ms[predict[-1]]
    if predict[-1] == "R":
        guess = ct_ms[predict[-1]]
    if predict[-1] == "S":
        guess = ct_ms[predict[-1]]
    return guess

#Also check if opponent's strategy depends on our previous moves
def check_my_moves(opponent_history,player_history):
    coeff = 0 # create a value to determine if our hypothesis true
    if(len(opponent_history)>5 and len(player_history) > 5):
        for i in range(1,5):
            o_move = opponent_history[-i]
            p_move = player_history[-i-1]
            #check if opponent tries to counter us
            check  = o_move == ct_ms[p_move] 
            if(check):
                coeff += 0.1 # if yes increase the coeff
    return coeff
