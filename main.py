BOARD = [' '] * 9


def draw_board(board):
    print(board[0] + "|" + board[1] + "|" + board[2])
    print("------")
    print(board[3] + "|" + board[4] + "|" + board[5])
    print("------")
    print(board[6] + "|" + board[7] + "|" + board[8])


def choose_symbol():
    letter = input("Wybierz symbol (X lub O): ").upper()
    if (letter != 'X' or letter != 'O'):
        while not (letter == 'X' or letter == 'O'):
            letter = input("Niepoprawny symbol, wybierz X lub O: ").upper()

    return letter


PLAYER_SYMBOL = choose_symbol()
if PLAYER_SYMBOL == 'X':
    COMPUTER_SYMBOL = 'O'
else:
    COMPUTER_SYMBOL = 'X'


def board_full(board):
    for i in range(9):
        if board[i] == ' ':
            return False

    return True


def player_move(board):
    while True:
        move = input("Podaj numer miejsca, w którym chcesz wykonać ruch (0-8)")

        if int(int(move)) not in range(0, 9):
            print("Wprowadz liczbę z przedziału 0-8")
        elif board[int(move)] != ' ':
            print("Pole zajęte")
        else:
            board[int(move)] = PLAYER_SYMBOL
            return board[int(move)]


def get_possible_moves(board):
    moves = []
    for i in range(len(board)):
        if board[i] == ' ':
            moves.append(i)
    return moves


def check_win(board):
    for i in range(0, 9, 3):
        if board[i] == board[i + 1] == board[i + 2] and board[i] != ' ':
            if board[i] == COMPUTER_SYMBOL:
                return -1
            else:
                return 1
    # Sprawdzanie kolumn
    for i in range(3):
        if board[i] == board[i + 3] == board[i + 6] and board[i] != ' ':
            if board[i] == COMPUTER_SYMBOL:
                return -1
            else:
                return 1
    # Sprawdzanie przekątnych
    if board[0] == board[4] == board[8] and board[0] != ' ':
        if board[0] == COMPUTER_SYMBOL:
            return -1
        else:
            return 1
    if board[2] == board[4] == board[6] and board[2] != ' ':
        if board[2] == COMPUTER_SYMBOL:
            return -1
        else:
            return 1

    #remis
    if board_full(board):
        return 0


def undo_move(board, move):

    board[move] = ' '

def is_game_over(board):
    # Sprawdzanie wierszy
    for i in range(0, 9, 3):
        if board[i] == board[i + 1] == board[i + 2] and board[i] != ' ':
             return True
    # Sprawdzanie kolumn
    for i in range(3):
        if board[i] == board[i + 3] == board[i + 6] and board[i] != ' ':
            return True
    # Sprawdzanie przekątnych
    if board[0] == board[4] == board[8] and board[0] != ' ':
        return True
    if board[2] == board[4] == board[6] and board[2] != ' ':
        return True
    # Sprawdzanie remisu
    if board_full(board):
        return True

    return False


def computer_move(board, computer_symbol):
    best_score = float('-inf')
    best_move = None

    if board == BOARD:  # czyli gdy pusta (komputer zaczyna)
        for move in get_possible_moves(board):
            board[move] = computer_symbol
            score = minimax(True, board)
            board[move] = ' '

            if score > best_score:
                best_score = score
                best_move = move

        board[best_move] = computer_symbol
    else:
        for move in get_possible_moves(board):
            board[move] = computer_symbol
            score = minimax(False, board)
            board[move] = ' '

            if score > best_score:
                best_score = score
                best_move = move

        board[best_move] = computer_symbol

def minimax(maximizing, board):
    if is_game_over(board):
        return check_win(board)

    result = []

    for move in get_possible_moves(board):
        if not maximizing:
            board[move] = COMPUTER_SYMBOL
        else:
            board[move] = PLAYER_SYMBOL
        result.append(minimax(not maximizing, board))
        undo_move(board, move)

    if maximizing:
        return max(result)
    else:
        return min(result)


def who_starts():
    player_turn = None

    while player_turn is not True and player_turn is not False:
        player_turn = input("Kto ma zacząć grę? Wybierz '1' dla gracza, '2' dla komputera: ")
        if player_turn == '1':
            player_turn = True
        elif player_turn == '2':
            player_turn = False
        else:
            print("Wybierz '1' lub '2'.")

    return player_turn


def main():
        player_turn = who_starts()

        board = BOARD

        while True:
            draw_board(board)

            if player_turn:
                print(f"Twój ruch! ({PLAYER_SYMBOL})") # Ruch gracza
                player_move(board)
            else:
                print(f"Ruch komputera! ({COMPUTER_SYMBOL})")  # Ruch Komputera
                computer_move(board, COMPUTER_SYMBOL)


            winner = check_win(board)

            if winner is not None:
                draw_board(board)
                if winner == 1:
                    winner = 'Komputer'
                elif winner == -1:
                    winner = 'Gracz'
                else:
                    winner is None
                    draw_board(board)
                    print("\nRemis!")
                    break
                print(f"\nZwycięzca: {winner}")
                break

            # elif board_full(board):
            #     draw_board(board)
            #     print("Remis")

            player_turn = not player_turn


if __name__ == '__main__':
    main()

















