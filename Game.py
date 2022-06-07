from Game_Functions import *

#Show the 'GAME START'
print()
print('-' * 30)
print('\033[1m' + ' GAME START '.center(30,'#')+ '\033[0m')
print('-' * 30)
print()

matrix = Tic_Tac_Toe.Matrix_create()
Tic_Tac_Toe.Show_positions(matrix)
players = Tic_Tac_Toe.Mensage_player()
Win = False #Bool value to indicate the Win player
Moves = 0 #Count the game moves

#Use de dict "players" to view the option(X or O) of the players.
Player_1 = players['Player_1'][0]
Player_2 = players['Player_2'][0]

name = 'Player 1' #Save the player identification
player = Player_1 #Save the X or O element

while Win != True and Moves < 9:

    print('\n' + '\033[1m' + ' %s (%s) '.center(30,'*') %(name,player) + '\033[0m')
    print('\033[1m' + '>>> Select the position(x,y): '+ '\033[0m')

    
    while True:
        move = input().split(',')
        move = Tic_Tac_Toe.Str_to_Int(move)
        try:
            if matrix[move[0]][move[1]] == ' ': #Check if the position is empty
                if move[0] <= 2 and move[1] <= 2: #Check if the position is in the range.
                    matrix = Tic_Tac_Toe.Moves(matrix, player, move)
                    break
                else:
                    IndexError
                    
            else:
                print('\033[1m' + '-> Position is ocuppied by "%s": '%(matrix[move[0]][move[1]])+ '\033[0m')
                Tic_Tac_Toe.Show_game(matrix)
                print('\033[1m' + '>>> Select the empty position(x,y): '+ '\033[0m')
                
        except IndexError as e:
            print('\033[1m' + '{%s}: %d and %d is out of range. \n Type a move in range(0, 1 or 2). Try again...' %(e,move[0],move[1]) + '\033[0m')
   
    
    
    Tic_Tac_Toe.Show_game(matrix)
    
    if Tic_Tac_Toe.Win_verification(matrix, player) == True:
        print('\n' + '\033[1m' + (30*'>') + '\033[0m')
        print('\033[1m' +"%s WIN!".center(20)%name + '\033[0m')
        print('\033[1m' + (30*'<') + '\033[0m')
        Win = True
        break
    
    #Change the player
    if player == Player_1:
        player = Player_2
        name = 'Player 2'
    else:
        player = Player_1
        name = 'Player 1'

    Moves += 1
    
else:
    #Show the game is Tie
    print('\n' + '\033[1m' + (30*'>') + '\033[0m')
    print('\033[1m' +"TIE".center(30)+ '\033[0m')
    print('\033[1m' + (30*'<') + '\033[0m')


