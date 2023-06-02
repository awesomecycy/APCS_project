
def print_board(board):
    print("-------------")
    for i in range(3):
        print("|", board[i][0], "|", board[i][1], "|", board[i][2], "|")
        print("-------------")

def check_winner(board, player):
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] == player:
            return True
        if board[0][i] == board[1][i] == board[2][i] == player:
            return True
    if board[0][0] == board[1][1] == board[2][2] == player:
        return True
    if board[0][2] == board[1][1] == board[2][0] == player:
        return True
    return False

def is_board_full(board):
    for row in board:
        if ' ' in row:
            return False
    return True

def play_game():
    board = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
    current_player = 'X'

    while True:
        print_board(board)

        while True:
            row = int(input("Enter the row (0-2): "))
            col = int(input("Enter the column (0-2): "))

            if 0 <= row <= 2 and 0 <= col <= 2 and board[row][col] == ' ':
                break
            else:
                print("Invalid move. Try again.")

        board[row][col] = current_player

        if check_winner(board, current_player):
            print("Player", current_player, "wins!")
            break

        if is_board_full(board):
            print("It's a tie!")
            break

        current_player = 'O' if current_player == 'X' else 'X'

play_game()