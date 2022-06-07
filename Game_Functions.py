class Tic_Tac_Toe:
    def Matrix_create():
        '''
        Create the Matrix 3x3 of the Tic-Tac-Toe Game with a empty characters.
        :return: Matrix Tic-Tac-Toe
        ''' 
        Matrix_Game = []
        for i in range(3):
            Matrix_Game.append([])
            for j in range(3):
                Matrix_Game[i].append(' ')
        return Matrix_Game
    
    def Moves(Matrix, player, moves):
        '''
        Receive the Matrix, the X or O and the position to put the element.
        :return: The new Matrix .
        ''' 
        Matrix[moves[0]][moves[1]] = player
        return Matrix
    
    def Mensage_player():
        '''
        Receive the names and the X or O of the players. Before show this information.
        :return: Dictionary with players information.
        ''' 
        Players = {}
        for i in range(2):
            if i == 0:
                print('\033[1m' + ' HI, PLAYER 1! '.center(30,'*') + '\033[0m')
                print('\033[1m' + '-> Select X or O: '+ '\033[0m')
                while True:
                    XO = input().upper()
                    if XO == 'X' or XO == 'O':
                        break
                    else:
                        print('\033[1m' + 'ERROR! Type X or O. Try again...' + '\033[0m')
                print('-' * 30)
                Players['Player_1'] = XO
                
                
            else:
                print('\033[1m' + ' HI, PLAYER 2! '.center(30,'*') + '\033[0m')
                print()
                XO = 'X' if Players['Player_1'][0] == 'O' else 'O'
                print('-' * 30)
                Players['Player_2'] = XO
                
            print('- You are: ' + '\033[1m' + '%s'%(XO) + '\033[0m')
            print('-' * 30)
            print()
            print('\033[1m' + ' GOOD LUCK! '.center(30,'*') + '\033[0m')
            print('\n')
        
        return Players
    
    def Show_game(Matrix):
        '''
        Print the Tic-Tac-Toe Game.
        :return: none
        ''' 
        for i in range(3):
            print(end='|')
            for j in range(3):
                print(Matrix[i][j],end='|')
            print()
    
    def Show_positions(Matrix):
        '''
        Print the positions of Tic-Tac-Toe Game.
        :return: none
        ''' 
        print('-' * 30)
        print('\033[1m' + 'POSITIONS - TIC-TAC-TOE '.center(30) + '\033[0m')
        print('-' * 30)
        for i in range(3):
            print(end='|')
            for j in range(3):
                print('\033[1m' + '(%d,%d)'%(i,j) + '\033[0m',end='|')
            print()    
        print('-' * 30,'\n')
              
    def Win_verification(Matrix, element):
        '''
        Receive the matrix of Tic_Tac_Toe and a element of the player.
        Check if the player win and the game end.
        :return: bool value, True(Win) and False(Game not finished). 
        ''' 
        Win = False
        
        #Verification of right diagonal line  
        for i in range(3):
            if Matrix[i][i] == element:
                Win = True
            else:
                Win = False
                break
        
        if Win != True:
            #Verification of left diagonal line
            for i in range(3):
                if Matrix[i][2-i] == element:
                    Win = True
                else:
                    Win = False
                    break
                
        if Win != True:
            #Verification of horizontal line      
            for i in range(3):
                for j in range(3):
                    if Matrix[j][i] == element:
                        Win = True
                    else:
                        Win = False
                        break
                if Win == True:
                    break
            
        if Win!=True:
            #Verification of columns      
            for i in range(3):
                for j in range(3):
                    if Matrix[i][j] == element:
                        Win = True
                    else:
                        Win = False
                        break  
                if Win == True:
                    break
        return Win                 
     
    def Str_to_Int(list):
        '''
        Receive a list containing numbers in string format and transform in int format.
        :return: list with int elements
        ''' 
        for i in range(2):
            list[i] = int(list[i])
        return list