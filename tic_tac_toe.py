def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(board, player):
    win_conditions = [
        [board[0][0], board[0][1], board[0][2]],
        [board[1][0], board[1][1], board[1][2]],
        [board[2][0], board[2][1], board[2][2]],
        [board[0][0], board[1][0], board[2][0]],
        [board[0][1], board[1][1], board[2][1]],
        [board[0][2], board[1][2], board[2][2]],
        [board[0][0], board[1][1], board[2][2]],
        [board[0][2], board[1][1], board[2][0]],
    ]
    return [player, player, player] in win_conditions

def get_move(board, player):
    while True:
        move = input(f"Player {player}, enter your move (row col): ")
        row, col = map(int, move.split())
        if 0 <= row <= 2 and 0 <= col <= 2 and board[row][col] == " ":
            return row, col
        else:
            print("Invalid move. Try again.")

def tic_tac_toe():
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"
    for _ in range(9):
        print_board(board)
        row, col = get_move(board, current_player)
        board[row][col] = current_player
        if check_winner(board, current_player):
            print_board(board)
            print(f"Player {current_player} wins!")
            return
        current_player = "O" if current_player == "X" else "X"
    print_board(board)
    print("It's a tie!")

if __name__ == "__main__":
    tic_tac_toe()
