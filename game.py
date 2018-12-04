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
        for x in range(9):
            self.board.append(Tile())

    def make_move(self, coords, move):
        self.board[coords[0]].make_move(coords[1:], move)
        if self.winner == None:
            self.winner = self.check_win()

    def check_win(self):
        # Rows
        if all(self.board[0].value != " " and self.board[0].value == rest.value for rest in self.board[0:3]):
            return self.board[0].value
        elif all(self.board[3].value != " " and self.board[3].value == rest.value for rest in self.board[3:6]):
            return self.board[3].value
        elif all(self.board[6].value != " " and self.board[6].value == rest.value for rest in self.board[6:9]):
            return self.board[6]
        # Columns
        elif all(self.board[0].value != " " and self.board[0].value == rest.value for rest in self.board[0:9:3]):
            return self.board[0].value
        elif all(self.board[1].value != " " and self.board[1].value == rest.value for rest in self.board[1:9:3]):
            return self.board[1].value
        elif all(self.board[2].value != " " and self.board[2].value == rest.value for rest in self.board[2:9:3]):
            return self.board[2].value
        # Diagonals
        elif all(self.board[0].value != " " and self.board[0].value == rest.value for rest in self.board[0:9:4]):
            return self.board[0].value
        elif all(self.board[2].value != " " and self.board[2].value == rest.value for rest in self.board[2:9:2][:-1]):
            return self.board[2].value
        return None


class Board(object):
    def __init__(self, nesting):
        self.board = []
        for x in range(9):
            self.board.append(SubBoard())
        self.winner = None

    def make_move(self, coords, move):
        self.board[coords[0]].make_move(coords[1:], move)
        winner = self.check_win()
        return winner

    def check_win(self):
        # Rows
        if all(self.board[0].winner != None and self.board[0].winner == rest.winner for rest in self.board[0:3]):
            return self.board[0]
        elif all(self.board[3].winner != None and self.board[3].winner == rest.winner for rest in self.board[3:6]):
            return self.board[3]
        elif all(self.board[6].winner != None and self.board[6].winner == rest.winner for rest in self.board[6:9]):
            return self.board[6]
        # Columns
        elif all(self.board[0].winner != None and self.board[0].winner == rest.winner for rest in self.board[0:9:3]):
            return self.board[0]
        elif all(self.board[1].winner != None and self.board[1].winner == rest.winner for rest in self.board[1:9:3]):
            return self.board[1]
        elif all(self.board[2].winner != None and self.board[2].winner == rest.winner for rest in self.board[2:9:3]):
            return self.board[2]
        # Diagonals
        elif all(self.board[0].winner != None and self.board[0].winner == rest.winner for rest in self.board[0:9:4]):
            return self.board[0]
        elif all(self.board[2].winner != None and self.board[2].winner == rest.winner for rest in self.board[2:9:2][:-1]):
            return self.board[2]
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

        move_count += 1
        prev_internal = int(coords[1])
    except InvalidMoveException:
        pass
    print("Subboard winners:")
    print(external_board.subBoardWins())
    external_board.display()
