import math
from IPython.display import clear_output

################### Part 1: define game state, ###################
gamestate= [[' ',  'X'  ,' ','X',' '],['X',' ',' ',' ','X'],[' ',' ','X',' ',' '],['X',' ',' ',' ','X'],[' ','X',' ','X',' ']]

################### Part 2: Player turn, max depth, pieces ###################
PlayerTurn = 'B' #b for computer
maxDepth = 8
black_pieces= ['b1','b2','b3','b4','b5','b6']
white_pieces = ['w1','w2','w3','w4','w5','w6']
pieces_removed_white= []
pieces_removed_black=[]
white_remaining_pieces=[item for item in white_pieces if item not in pieces_removed_white]
black_remaining_pieces=[item for item in black_pieces if item not in pieces_removed_black]

################### Part 3: check who won
def who_won(cur):
    if len(black_pieces)==2:
        print("Human - Player W has won the game!")
        return True
    if len(white_pieces)==2:
        print("Computer - Player B has won the game!")
        return True 
    return False #keep playing

    
################### Part 4: check three in row for black (computer) , white (human)
def three_in_row_black(cur):
      if current_black_positions:
        for i in range(4):
                if (cur[i][0] == cur[i][2] and cur[0][2] == cur[i][4]): 
                    return white_pieces.remove(int(input("Three in row achieved. Please select what piece you'd like to remove from the opponent:"))) #outerrowwin
                if (cur[i][1] == cur[i][2] and cur[i][2] == cur[i][3]):
                    return white_pieces.remove(int(input("Three in row achieved. Please select what piece you'd like to remove from the opponent:"))) #innerrowwin
                if (cur[0][i] == cur[2][i] and cur[2][i] == cur[4][i]):
                    return white_pieces.remove(int(input("Three in row achieved. Please select what piece you'd like to remove from the opponent:"))) #outtercolumnwin
                if (cur[1][i] == cur[2][i] and cur[2][i] == cur[3][i]): 
                    return white_pieces.remove(int(input("Three in row achieved. Please select what piece you'd like to remove from the opponent:"))) #innerrowwin
    
def three_in_row_white(cur):
      if current_white_positions:
        for i in range(4):
                if (cur[i][0] == cur[i][2] and cur[0][2] == cur[i][4]): 
                    return white_pieces.remove(int(input("Three in row achieved. Please select what piece you'd like to remove from the opponent:"))) #outerrowwin
                if (cur[i][1] == cur[i][2] and cur[i][2] == cur[i][3]):
                    return white_pieces.remove(int(input("Three in row achieved. Please select what piece you'd like to remove from the opponent:"))) #innerrowwin
                if (cur[0][i] == cur[2][i] and cur[2][i] == cur[4][i]):
                    return white_pieces.remove(int(input("Three in row achieved. Please select what piece you'd like to remove from the opponent:"))) #outtercolumnwin
                if (cur[1][i] == cur[2][i] and cur[2][i] == cur[3][i]): 
                    return white_pieces.remove(int(input("Three in row achieved. Please select what piece you'd like to remove from the opponent:"))) #innerrowwin

###################Part 5: Player changes
def changePlayerTurn():
  global PlayerTurn
  if PlayerTurn == 'B':
    PlayerTurn = 'W'
  else:
    PlayerTurn = 'B'       



################### Part 6: Print board
def printGameBoard(cur):
  # clear screen
  clear_output()
  # print the board again
  for i in cur:
    print(i)
    
    
    
################### Part 7: Evaluation Function
#def eval_state(cur): evaluate for win


    
#terminal state: no given state on the board necessarily defines a win other than 2 pieces left of the opposing player


################### Part 8: Min Max Function
#def minimax:
#essentially same as tic-tac-toe, we want 3 out of 5 in a column


#def max value


#def min value

################### Part 9: Print board game winner - need to change it so it can be place all pieces
printGameBoard(gamestate)
while(True):
  if (PlayerTurn == 'B'):
    # Player B move - AI
    rMove = int(input("Player B - Computer, Please enter the row of your move for b1: "))
    cMove = int(input("Player B - Computer, Please enter the column of your move for b1: "))
    while (rMove < 0 or rMove > 4 or cMove < 0 or cMove > 4 or gamestate[rMove][cMove] != ' '):
        rMove = int(input("Please enter a valid row of your move first v: "))
        cMove = int(input("Please enter a valid column of your move: "))
    gamestate[rMove][cMove] = 'B'
    printGameBoard(gamestate)
    if (who_won(gamestate)):
      break
    changePlayerTurn()
  else:
    # Player W move - Human
    rMove = int(input("Player W- Human, Please enter the row for your move w1: "))
    cMove = int(input("Player W- Human, Please enter the column for your move for w1: "))
    while (rMove < 0 or rMove > 4 or cMove < 0 or cMove > 4 or gamestate[rMove][cMove] != ' '):
        rMove = int(input("Player W- Human, Please enter a valid row of your move first: "))
        cMove = int(input("Player W- Human, Please enter a valid column of your move: "))
    #now we have a valid X move
    gamestate[rMove][cMove] = 'W'
    # Print gameBoard()
    printGameBoard(gamestate)
    print("Player B - Computer has remaining pieces of", black_remaining_pieces)
    print("Player W - Human has remaining pieces of", white_remaining_pieces)
    if (who_won(gamestate)):
      break
    changePlayerTurn()
    
    
