print("Welcome To Tic Tac Toc Game") 
player1=input("Enter your Name Player1:").capitalize()
player2=input("Enter your Name Player2:").capitalize()
print("Choose your Sign X or O") 
sign_player1=input("Enter Sign here:").upper()
if sign_player1=='X':
        sign_player2='O'
elif sign_player1=='O':
        sign_player2='X'
else:
    print('Please select the sign o or x') 
print(f"{player1} sign is {sign_player1} and {player2} sign is {sign_player2} \nLet's Begin the Game....")   

#!dict
game_Board={'1': ' ' , '2': ' ' , '3': ' ',
            '4': ' ' , '5': ' ' , '6': ' ' ,
            '7': ' ' , '8': ' ' , '9': ' '} 

#! storing the dict in list
keys=[]
for key in game_Board:
    keys.append(key)

#! print the game board
def printBoard(board):
    print('-'*10)
    print('|' + board['1'] + ' |' + board['2'] + ' |' + board['3'] + ' |')
    print('-'*10)
    print('|' + board['4'] + ' |' + board['5'] + ' |' + board['6'] + ' |')
    print('-'*10)
    print('|' + board['7'] + ' |' + board['8'] + ' |' + board['9'] + ' |')
    print('-'*10)

#! find the winner
def winner(board):
    win=[['1','2','3'],['4','5','6'],['7','8','9'],
           ['1','4','7'],['2','5','8'],['3','6','9'],
           ['1','5','9'],['3','5','7']]
    
    for check in win:
         if board[check[0]]==board[check[1]]==board[check[2]] and board[check[0]]!=' ':
              return board[check[0]]
    return None

#! main func
def game():
    
    turn=sign_player1
    count = 0

    for i in range(9):
        printBoard(game_Board)
        print(turn,"Enter your position:")
        move = input()        

        if game_Board[move] == ' ':
            game_Board[move] = turn
            count += 1
        else:
            print("Already position occupied......")
            continue

        game_Winner=winner(game_Board)
        if game_Winner:
            printBoard(game_Board)               
            print(turn, "has won the game....")
            break  

        if count==9:
            print("Game Over....\nGame Tie....")                 

        if turn==sign_player1:
            turn=sign_player2
        else:
            turn=sign_player1  
       
game()

