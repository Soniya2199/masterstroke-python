print("Welcome To Tic Tac Toc Game")
def player_data(player1,player2,sign_player1,sign_player2):
    
    print()   
player1=input("Enter your Name Player1:")
player2=input("Enter your Name Player2:")
print("Choose your Sign X or O") 
sign_player1=input("Enter Sign here:").upper()
if sign_player1=='X':
        sign_player2='O'
elif sign_player1=='O':
        sign_player2='X'
else:
    print('Please select the sign o or x')    
# player_data(player1,player2)

game_Board={'1': ' ' , '2': ' ' , '3': ' ',
            '4': ' ' , '5': ' ' , '6': ' ' ,
            '7': ' ' , '8': ' ' , '9': ' '} 

keys=[]
for key in game_Board:
    keys.append(key)
# print(keys)

def printBoard(board):
    print(board['1'] + '|' + board['2'] + '|' + board['3'])
    print('-----')
    print(board['4'] + '|' + board['5'] + '|' + board['6'])
    print('-----')
    print(board['7'] + '|' + board['8'] + '|' + board['9'])
# printBoard(game_Board)

def game():

    player_data(player1,player2,sign_player1,sign_player2)
    print(f"{player1} sign is {sign_player1} and {player2} sign is {sign_player2} \nLet's Begin the Game....")
    
    turn=sign_player1
    count = 0

    for i in range(10):
        printBoard(game_Board)
        print(turn,"Enter your position:")

        move = input()        

        if game_Board[move] == ' ':
            game_Board[move] = turn
            count += 1
        else:
            print("Already position occupied......")
            continue

        if count >= 5:
            if game_Board['1'] == game_Board['2'] == game_Board['3'] != ' ':
                printBoard(game_Board)               
                print(turn, "has won the game....")                
                break
            elif game_Board['4'] == game_Board['5'] == game_Board['6'] != ' ': 
                printBoard(game_Board)               
                print(turn, "has won the game....")                
                break
            elif game_Board['7'] == game_Board['8'] == game_Board['9'] != ' ':  
                printBoard(game_Board)               
                print(turn, "has won the game....")                
                break
            elif game_Board['1'] == game_Board['4'] == game_Board['7'] != ' ':
                printBoard(game_Board)               
                print(turn, "has won the game....")                
                break
            elif game_Board['2'] == game_Board['5'] == game_Board['8'] != ' ': 
                printBoard(game_Board)               
                print(turn, "has won the game....")                
                break
            elif game_Board['3'] == game_Board['6'] == game_Board['9'] != ' ':
                printBoard(game_Board)               
                print(turn, "has won the game....")                
                break 
            elif game_Board['3'] == game_Board['5'] == game_Board['7'] != ' ': 
                printBoard(game_Board)               
                print(turn, "has won the game....")                
                break
            elif game_Board['1'] == game_Board['5'] == game_Board['9'] != ' ':
                printBoard(game_Board)               
                print(turn, "has won the game....")                
                break 

        if count == 9:            
            print("Tie....")

        if turn ==sign_player1:
            turn =sign_player2
        else:
            turn =sign_player1        
    
    replay = input("Restart game(y/n):").upper()
    if replay == "y":  
        for key in keys:
            game_Board[key] = " "
    else:
        print("Exits")

game()