holes = [1, 2, 3, 4, 5, 6]
MAX_DEPTH = 5

def calculateMove(player1Marbles, player2Marbles):
    #set alpha to negative infinity
    alpha = float('-inf')
    #set beta to positive infinity
    beta = float('inf')
    #set bestMove to none, which will be updated later
    bestMove = None
    
    #for each hole in the holes array
    for hole in holes:
        #check if the move is valid 
        if checkValidMove(player1Marbles, hole):
            #make a move 
            newPlayer1Marbles = makeMove(player1Marbles, hole)
            #return the score for this move by running the move through the alpha beta algorithm
            score = alphaBeta(newPlayer1Marbles, player2Marbles, MAX_DEPTH-1, alpha, beta, False)
            #if the score is greater than alpha
            #update alpha and the best move
            if score > alpha:
                alpha = score
                bestMove = hole
    
    #print out the best move
    print(bestMove)

def alphaBeta(player1Marbles, player2Marbles, depth, alpha, beta, maximizingPlayer):
    if depth == 0:
        #calculate the score for leaf node
        return calculateScore(player1Marbles)
    
    #if current node is maximizing player
    if maximizingPlayer:
        
        #set value to negative infinity
        value = float('-inf')
        
        #for each hole inside the holes array
        for hole in holes:
            
            #if the move is valid
            if checkValidMove(player1Marbles, hole):
                
                #make a move for player 1
                newPlayer1Marbles = makeMove(player1Marbles, hole)
                
                #update value with the max value between the current value and returned value from the recursive call
                value = max(value, alphaBeta(newPlayer1Marbles, player2Marbles, depth-1, alpha, beta, False))
                
                #update alpha with the max value between alpha and the current value
                alpha = max(alpha, value)
                
                #if the beta value is less than or equal to the alpha value, break from loop
                if beta <= alpha:
                    break
        return value
    
    #if current node is minimizing player
    else:
        #set value to positive infinity
        value = float('inf')
        
        #for each hole inside the holes array
        for hole in holes:
            
            #if the move is valid
            if checkValidMove(player1Marbles, hole):
                
                #make a move for player 2
                newPlayer2Marbles = makeMove(player2Marbles, hole)
                
                #update value with the max value between the current value and returned value from the recursive call
                value = min(value, alphaBeta(player1Marbles, newPlayer2Marbles, depth-1, alpha, beta, True))
                
                #update beta with the max value between beta and the current value
                beta = min(beta, value)
                
                #if the beta value is less than or equal to the alpha value, break from loop
                if beta <= alpha:
                    break
        return value
    
def calculateScore(player1Marbles):
    #add all the values inside the input list and return the sum
    marblesSum = sum([int(x) for x in player1Marbles])
    return marblesSum

def makeMove(player1Marbles, botInput):
    #get value of chosenHole
    chosenHole = int(botInput) - 1
    #remove the marbles from the chosen hole
    marblesTakenFromHole = int(player1Marbles[chosenHole])
    #set the number of marbles at the chosen hole to 0
    player1Marbles[chosenHole] = "0"
    #distribute the marbles to each hole/mancala
    while marblesTakenFromHole > 0:
        chosenHole = (chosenHole + 1) % len(player1Marbles)
        player1Marbles[chosenHole] = str(int(player1Marbles[chosenHole]) + 1)
        marblesTakenFromHole -= 1
    return player1Marbles

def checkValidMove(player1Marbles, botInput):
    #check if current hole is empty
    if player1Marbles[int(botInput) - 1] == 0:
        return False
    else:
        return True

def printNextMove(player, player1Mancala, player1Marbles, player2Mancala, player2Marbles):
    
    #take the string input of marbles of both players and convert it into an integer list
    player1Holes = [int(num) for sublist in player1Marbles for num in sublist.split()] 
    player2Holes = [int(num) for sublist in player2Marbles for num in sublist.split()] 
    
    #calculate next move
    calculateMove(player1Holes, player2Holes)

#call the print function passing in all the inputs 
printNextMove(input(), input(), input(), input(), input())