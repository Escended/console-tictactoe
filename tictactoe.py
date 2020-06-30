state = " " * 9
winner = None
draw = False


# "1 1", "1 2", "1 3",
# "2 1", "2 2", "2 3",
# "3 1", "3 2", "3 3"

def main():
    game_state(state)
    read_board(state)
    while winner is None:
        player_move()
        if winner is not None:
            break


def game_state(cells):
    print("-" * 9)
    print(f"| {cells[0]} {cells[1]} {cells[2]} |")
    print(f"| {cells[3]} {cells[4]} {cells[5]} |")
    print(f"| {cells[6]} {cells[7]} {cells[8]} |")
    print("-" * 9)


def read_board(cells):
    board = zip(*[iter(cells)] * 3)
    # board = list(board)
    board = [list(i) for i in board]
    return board


def player_move():
    # Input a coordinate
    global state
    board = read_board(state)
    updated_board = ""
    global co
    move = True
    while move and winner is None and not draw:
        check_if_possible(updated_board)
        find_winner(read_board(state))
        co = input("Enter the coordinates: ")
        try:
            co = [int(c) for c in co.split()]
            if len(co) < 2:
                raise ValueError
            elif co[0] > 3 or co[1] > 3:
                print("Coordinates should be from 1 to 3!")
            # Check if coordinate is available according to board status
            elif board[3 - co[1]][co[0] - 1] in ["_", " "]:
                if check_if_possible(board):
                    board[3 - co[1]][co[0] - 1] = "X"
                else:
                    board[3 - co[1]][co[0] - 1] = "O"
                for lst in board:
                    updated_board += "".join(lst)
                game_state(updated_board)
                state = updated_board
                move = False
            else:
                print("This cell is occupied! Choose another one!")
        except ValueError:
            print("You should enter numbers!")


def check_if_possible(board):
    X_count = []
    O_count = []

    for i, lst in enumerate(board):
        for j, item in enumerate(lst):
            if item == 'X':
                X_count.append(item)
            elif item == 'O':
                O_count.append(item)
    if abs(len(X_count) - len(O_count)) >= 1:
        # print("Impossible")
        return False
    else:
        return True


def find_winner(board):
    global winner
    global draw
    if True:
        count = 0
        winners = []
        for i, lst in enumerate(board, 1):
            for j, item in enumerate(lst, 1):
                if item in ["X", "O"]:
                    # If every item in a list is the same then winner in row
                    # Horizontal check
                    if all(x == item for x in lst):
                        count += 1
                        if count > 3:
                            print("Impossible")
                        else:
                            winner = item
                            print(winner, "wins")
                            exit()
                    # Vertical check
                    if i == 2:
                        if item == board[0][j - 1] and item == board[2][j - 1]:
                            count += 1
                            winners.append(item)
                            if count > 1:
                                print("Impossible")
                                return True
                    # Diagonal win condition
                    if i == 2 and j == 2:
                        if (item == board[0][0] and item == board[2][2]) or (
                                item == board[0][2] and item == board[2][0]):
                            winner = item
                            print(winner, "wins")
                            exit()

        if len(winners) == 1:
            winner = winners[0]
            print(winner, "wins")
            return
        empty = 9
        if winner is None:
            for lst in board:
                for item in lst:
                    # print(item)
                    if item == " ":
                        continue
                    else:
                        empty -= 1
        if empty == 0:
            print("Draw")
            draw = True
            exit()
            return True


main()
