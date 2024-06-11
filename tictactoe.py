def display_board(board):
    print(f" {board[0]} | {board[1]} | {board[2]}")
    print("---+---+---")
    print(f" {board[3]} | {board[4]} | {board[5]}")
    print("---+---+---")
    print(f" {board[6]} | {board[7]} | {board[8]}")

def player_input():
    while True:
        user_choice = input("CHOOSE X OR O: ").upper()
        if user_choice in ['X', 'O']:
            p2_choice = 'O' if user_choice == 'X' else 'X'
            return user_choice, p2_choice
        elif user_choice in ['Q', 'q']:
            return None
        else:
            print("PLEASE ENTER VALID INPUT!")

def position_input(board):
    while True:
        try:
            position_choice = int(input("Enter the position on the board (1-9): "))
            if position_choice in range(1, 10) and board[position_choice - 1] == ' ':
                return position_choice - 1
            else:
                print("Position already taken or invalid, please choose another.")
        except ValueError:
            print("PLEASE ENTER A VALID NUMBER")

def check_winner(board, player):
    win_conditions = [
        [board[0], board[1], board[2]],  # Top row
        [board[3], board[4], board[5]],  # Middle row
        [board[6], board[7], board[8]],  # Bottom row
        [board[0], board[3], board[6]],  # Left column
        [board[1], board[4], board[7]],  # Middle column
        [board[2], board[5], board[8]],  # Right column
        [board[0], board[4], board[8]],  # Diagonal from top-left
        [board[2], board[4], board[6]]   # Diagonal from top-right
    ]
    return [player, player, player] in win_conditions

def main_menu():
    print("x-o-x-o WELCOME TO THE TIC-TAC-TOE GAME x-o-x-o")
    while True:
        user_input = input("Press Enter to start the game (or 'q' to quit): ").upper()
        if user_input == "":
            break 
        elif user_input == 'Q':
            return False
    return True

if main_menu():
    board = [' '] * 9  # Initialize the board
    player_choices = player_input()
    if player_choices:
        player1, player2 = player_choices
        print(f"Player 1 chose: {player1}, Player 2 will be: {player2}")
        current_player = player1
        while True:
            display_board(board)
            pos = position_input(board)
            board[pos] = current_player
            
            # Check for a winner after each move
            if check_winner(board, current_player):
                display_board(board)
                print(f"Player {current_player} wins!")
                break
            
            # Check for a tie
            if ' ' not in board:
                display_board(board)
                print("It's a tie!")
                break
            
            # Switch player for the next turn
            current_player = player1 if current_player == player2 else player2
    else:
        print("Game exited.")
else:
    print("Game exited.")
