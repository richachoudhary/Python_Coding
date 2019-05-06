board = [  "-","-","-",
           "-","-","-",
           "-","-","-", ]
player= 'X'
game_on= True
winner= None
def print_board():
    print(board[0]+ '|'+ board[1]+ '|' + board[2])
    print(board[3]+ '|'+ board[4]+ '|' + board[5])
    print(board[6]+ '|'+ board[7]+ '|' + board[8])

def play_game():
  global game_on
  global winner
  while game_on==True:
     print_board()
     take_input()
     check_if_game_got_over ()
     #print(game_on)
  if winner=='X' or winner=='O':
        print(winner+ ' Won the game.')
  elif winner==None:
        print('Tie')

def take_input():
    # only take input between 0 to 9
    input_pos = int ( input ( "at position: " ) )-1

    while(input_pos not in range(0, 9)):
         print("please enter a value between 1 to 9")
         input_pos = int ( input ( "at position: " ) ) - 1

    #avoid over-writing
    if board[input_pos]=="-":
         board[input_pos]= player

    change_players()
    #print_board()




def change_players():
        global player
        if player=='X':
            player= 'O'
        elif player=='O':
            player='X'

def check_if_game_got_over():

   global winner

   def check_win():

    def check_row():
        global game_on
        global winner
        if board[0]==board[1]==board[2]!='-':
                game_on=False
                winner= board[0]
        if board[3] == board[4] == board[5] != '-':
            game_on = False
            winner = board[3]
        if board[6] == board[7] == board[8] != '-':
            game_on = False
            winner = board[6]


    def check_column():
        global game_on
        global winner
        if board[0] == board[3] == board[6] != '-':
            game_on = False
           # print('cifgjhrg')
            winner = board[0]
            #print('b1')
        if board[1] == board[4] == board[7] != '-':
            game_on =False
            winner = board[1]
        if board[2] == board[5] == board[8] != '-':
            game_on = False
            winner = board[2]
    def check_diagonal():
        global game_on
        global winner
        if board[0] == board[4] == board[8] != '-':
            game_on = False
            winner = board[0]
        if board[2] == board[4] == board[6] != '-':
            game_on = False
            winner = board[2]

    check_row ()
    check_column ()
    check_diagonal ()

   # Check if there is a tie
   def check_for_tie():
        # Set global variables
        global game_on
        # If board is full
        if "-" not in board :
            game_on = False


   check_win()
   check_for_tie()






play_game()

