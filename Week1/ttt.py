import random

def print_board(board):
    print("\n")
    print(board[0], "|", board[1], "|", board[2])
    print("--+---+--")
    print(board[3], "|", board[4], "|", board[5])
    print("--+---+--")
    print(board[6], "|", board[7], "|", board[8])

def check_winner(board, player):
    wins = [ [3,4,5], [6,7,8], 
            [0,4,8],[2,4,6]
    ]
    for combo in wins:
        if board[combo[0]] == board[combo[1]] == board[combo[2]] == player:
            return True
    return False

def computer_move(board):
    empty = [i for i in range(9) if board[i] == " "]
    return random.choice(empty) if empty else None

def tic_tac_toe():
    board = ["O", " ", "X", 
             "X", " ", " ", 
             "X", "O", "O"]
    
    while " " in board:
        print_board(board)
        print("Shashwat,1BF24CS278")
        
        try:
            pos = int(input("Your move (1-9): ")) - 1
            if pos < 0 or pos > 8:
                print("Invalid input! Choose 1-9.")
                continue
        except ValueError:
            print("Invalid input! Enter a number.")
            continue

        if board[pos] != " ":
            print("Position already taken! Try again.")
            continue
            
        board[pos] = "X"
        
        if check_winner(board, "X"):
            print_board(board)
            print("You win!")
            return
            
        comp = computer_move(board)
        if comp is not None:
            board[comp] = "O"
            print(f"Computer chose position {comp+1}")
            
            if check_winner(board, "O"):
                print_board(board)
                print("Computer wins!")
                return

    print_board(board)
    print("It's a draw!")

tic_tac_toe()