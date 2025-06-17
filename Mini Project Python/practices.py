
#^ Normal if else
# print("Welcome To Tic Tac Toc Game")
# player1=input("Enter your Name Player1:")
# # print(player1)
# player2=input("Enter your Name Player2:")
# # print(player2)
# Sign_player1=input("Select your Sign:")
# if Sign_player1=='x':
#     Sign_player2='o'
# elif Sign_player1=='o':
#     Sign_player2='x'
# else:
#     print('Please select the sign o or x')
# print(f'{player1} sign is {Sign_player1} and {player2} sign is',Sign_player2)
# print("Let's Start the Game....")

#***************************************************************************************
#~ using Function
# print("Welcome To Tic Tac Toc Game")
# def user_data(player1,player2):
#     print("Choose your Sign X or O")
#     Sign_player1=input("Enter Sign here:")
#     if Sign_player1=='x':
#         Sign_player2='o'
#     elif Sign_player1=='o':
#         Sign_player2='x'
#     else:
#         print('Please select the sign o or x')
#     print(f'{player1} sign is {Sign_player1} and {player2} sign is',Sign_player2)
#     print("So Let's Begin the Game....")
# player1=input("Enter your Name Player1:")
# player2=input("Enter your Name Player2:")
# user_data(player1,player2)

#***************************************************************************************
# x=1
# while x<3:
#     for i in range(4):
#         print("|"," ",end="")
#     print()
#     for j in range(10):
#         print("-",end="")
#     print()   
#     x=x+1
# for k in range(4):
#     print("|"," ",end="")

#***************************************************************************************
# x=1
# while x<=4:
#     for i in range(3):
#         print("|",end="")
#         for j in range(2):
#             print("-",end="")
#     print("|")
#     for k in range(4):
#         print("|" "  ",end="")
# x=x+1
#     # break
#***************************************************************************************
# def game_board():
#     for i in range(2):
#         print("|   |   |   |")
#         print("-"*13)
#     for j in range(4):
#         print("|""   ",end="")
# game_board()
#***************************************************************************************
#   for i in range(4):
#         print("|"," ",end="")
#     print()
#     for j in range(10):
#         print("-",end="")
#***************************************************************************************

# board=[
#     [1,2,3],
#     [4,5,6],
#     [7,8,9]
# ]
# print(board)


# def game_board():
#     x=1
#     while x<=3:
#         for j in range(10):
#             print("-",end="")
#         print() 
#         for i in range(4):
#             print("|")
#             y=1
#             while y<=9:
#                 print(y)
#             y=y+1
#             # print()
#         break
#     #     x=x+1
#     # for k in range(10):
#     #    print("-",end="")
# game_board()



# def game_board():
#     x=1
#     while x<=3:
#         for j in range(13):
#             print("-",end="")
#         print() 
#         for i in range(4):
#             print("|","  ",end="")
#         print()
#         x=x+1
#     for k in range(13):
#        print("-",end="")
# game_board()

for i in range(10):
    print(i)