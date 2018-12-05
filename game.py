#!/usr/bin/env python3


class InvalidMoveException(Exception):
    def __init__(self, message):
        super().__init__(message)


class Tile(object):
    def __init__(self):
        self.value = " "

    def make_move(self, coords, move):
        if self.value != " ":
            raise InvalidMoveException("Invalid move")
        self.value = move

    def display(self, row):
        return self.value


class SubBoard(object):
    def __init__(self):
        self.board = []
        self.winner = None
        self.winning_combos = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]

        for x in range(9):
            self.board.append(Tile())

    def make_move(self, coords, move):
        self.board[coords[0]].make_move(coords[1:], move)
        if self.winner == None:
            self.winner = self.check_win()

    def check_win(self):
        for wc in self.winning_combos:
            if self.board[wc[0]].value != " " and self.board[wc[0]].value == self.board[wc[1]].value == self.board[wc[2]].value:
                return self.board[wc[0]].value
        return None


class Board(object):
    def __init__(self, nesting):
        self.board = []
        self.winning_combos = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
        for x in range(9):
            self.board.append(SubBoard())
        self.winner = None

    def make_move(self, coords, move):
        self.board[coords[0]].make_move(coords[1:], move)
        winner = self.check_win()
        return winner

    def check_win(self):
        for wc in self.winning_combos:
            if self.board[wc[0]] != None and self.board[wc[0]].winner == self.board[wc[1]].winner == self.board[wc[2]].winner:
                return self.board[wc[0]].winner
        return None



    def subBoardWins(self):
        s = ""
        for index, board in enumerate(self.board):
            s += str(index) + " " + str(board.winner) + "\n"
        return s

    def display(self):
        s = ""
        for k in range(0, 9, 3):
            for i in range(k, k + 3):
                for j in range(3):
                    s += self.board[i].board[j].value
                    if i == k+2 and j == 2:
                        pass
                    elif j == 2:
                        s += " \u2503 " # thick line
                    else:
                        s += "\u2502"
            print(s)
            s = ""
            print(
                "\u2500\u253C\u2500\u253C\u2500 \u2503 \u2500\u253C\u2500\u253C\u2500 \u2503 \u2500\u253C\u2500\u253C\u2500")
            for i in range(k, k + 3):
                for j in range(3, 6):
                    s += self.board[i].board[j].value
                    if i == k+2 and j == 5:
                        pass
                    elif j == 5:
                        s += " \u2503 "
                    else:
                        s += "\u2502"
            print(s)
            s = ""
            print(
                "\u2500\u253C\u2500\u253C\u2500 \u2503 \u2500\u253C\u2500\u253C\u2500 \u2503 \u2500\u253C\u2500\u253C\u2500")
            for i in range(k, k + 3):
                for j in range(6, 9):
                    s += self.board[i].board[j].value
                    if i == k+2 and j == 8:
                        pass
                    elif j == 8:
                        s += " \u2503 "
                    else:
                        s += "\u2502"
            print(s)
            s = ""
            if not k == 6:
                print((("\u2501"*6)+"\u254b\u2501")*2+("\u2501"*6))
            else:
                print()



winning_moves = ["0 0", "1", '0', '2', '0', '4', '4', '0', '3', '0', '6', '1', '2', '1', '1', '8', '8', '2', '4', '2', '8']
external_board = Board(1)
move_count = 0

command = input(
    "First move. Enter space seperated coordinates place the first move. 0 0 for top left 8 8 for bottom right.\n")
coords = command.split()
for i in range(len(coords)):
    coords[i] = int(coords[i])
external_board.make_move(coords, 'x')
external_board.display()
move_count += 1
prev_internal = coords[1]
winner = None
while not winner:
    command = input("Where do you want to make your move?\n")
    coords = [prev_internal, int(command)]
    try:
        if move_count % 2 == 0:
            winner = external_board.make_move(coords, 'x')
        else:
            winner = external_board.make_move(coords, 'o')
        if winner:
            print(f'{winner} wins!')
        move_count += 1
        prev_internal = int(coords[1])
    except InvalidMoveException:
        pass
    print("Subboard winners:")
    print(external_board.subBoardWins())
    external_board.display()
