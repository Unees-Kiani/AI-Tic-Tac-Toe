# AI Tic-Tac-Toe Game
# Player uses X and computer uses O

def show_board(board):
    print()
    print(board[0], "|", board[1], "|", board[2])
    print("--+---+--")
    print(board[3], "|", board[4], "|", board[5])
    print("--+---+--")
    print(board[6], "|", board[7], "|", board[8])
    print()


# Check who has won the game
def check_winner(board):
    winning_positions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],
        [0, 3, 6], [1, 4, 7], [2, 5, 8],
        [0, 4, 8], [2, 4, 6]
    ]

    for positions in winning_positions:
        a = positions[0]
        b = positions[1]
        c = positions[2]

        if board[a] == board[b] == board[c] != " ":
            return board[a]

    return None


# Minimax helps the computer choose a good move
def minimax(board, computer_turn):
    winner = check_winner(board)

    if winner == "O":
        return 1

    if winner == "X":
        return -1

    if " " not in board:
        return 0

    if computer_turn:
        best_score = -100

        for i in range(9):
            if board[i] == " ":
                board[i] = "O"
                score = minimax(board, False)
                board[i] = " "

                if score > best_score:
                    best_score = score

        return best_score

    else:
        best_score = 100

        for i in range(9):
            if board[i] == " ":
                board[i] = "X"
                score = minimax(board, True)
                board[i] = " "

                if score < best_score:
                    best_score = score

        return best_score


# Computer selects its next move
def computer_move(board):
    best_score = -100
    best_position = 0

    for i in range(9):
        if board[i] == " ":
            board[i] = "O"
            score = minimax(board, False)
            board[i] = " "

            if score > best_score:
                best_score = score
                best_position = i

    board[best_position] = "O"


# Main game
def play_game():
    board = [" "] * 9

    print("Welcome to AI Tic-Tac-Toe!")
    print("You are X and the computer is O.")
    print("Choose a position from 1 to 9.")

    while True:
       
        # Show numbers in empty positions
        display_board = []

        for i in range(9):
            if board[i] == " ":
                display_board.append(str(i + 1))
            else:
                display_board.append(board[i])

        show_board(display_board)
        # Ask the player for a move
        try:
            position = int(input("Enter your position (1-9): "))
        except ValueError:
            print("Please enter a number.")
            continue

        if position < 1 or position > 9:
            print("Choose a number from 1 to 9.")
            continue

        if board[position - 1] != " ":
            print("That position is already taken.")
            continue

        # Place the player's X
        board[position - 1] = "X"

        if check_winner(board) == "X":
            show_board(board)
            print("Congratulations! You win!")
            break

        if " " not in board:
            show_board(board)
            print("The game is a draw!")
            break

        # Computer plays
        computer_move(board)
        print("Computer has made its move.")

        if check_winner(board) == "O":
            show_board(board)
            print("Computer wins!")
            break

        if " " not in board:
            show_board(board)
            print("The game is a draw!")
            break


play_game()