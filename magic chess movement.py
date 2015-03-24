__author__ = 'Dark-Knight'

import tkinter as tk
import copy


class Board():


    def __init__(self,root ):
        self.chessboard = [['r', 'n', 'b', 'q', 'k', 'b', 'n', 'r'],
             ['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p'],
             [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
             [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
             [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
             [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
             ['P', 'P', 'P ','P','P', 'P', 'P', 'P'],
             ['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R']]
        self.pieces = {'K': ['white king', 1, [[1, 0], [1, 1], [-1, 1], [-1, -1], [1, -1], [-1, 0], [0, -1], [0, 1]], [[1, 0], [1, 1], [-1, 1], [-1, -1], [1, -1], [-1, 0], [0, -1], [0, 1]] ],
              'Q': ["white queen", 8, [[1, 0], [1, 1], [0, 1], [-1, 1], [-1, 0], [-1, -1], [0, -1], [1, -1]], [[1, 0], [1, 1], [0,  1], [-1, 1], [-1,0], [-1,-1], [0,-1], [1,-1]]],
              'B': ['white bishop', 8, [[1, -1], [1, 1], [-1, -1], [-1, 1]], [[1, -1], [1, 1], [-1, -1], [-1, 1]]],
              'R': ['white rook', 8, [[0, -1], [0, 1], [-1, 0], [1, 0]], [[0, -1], [0, 1], [-1, 0]]],
              'P': ['white pawn', 1, [[0, 1]], [[-1, -1], [1, -1]], [[-1, -1], [1, -1]]],
              'N': ['white knight', 8, [[1, -2], [2, -1], [2, 1], [1, 2], [-1, -2], [-2, -1], [-2, 1], [-1, 2]],[[1,-2],[2,-1],[2,1],[1,2],[-1,-2],[-2,-1],[-2,1],[-1,2]]],
              'k': ['black king', 1, [[1, 0], [1, 1], [-1, 1], [-1, -1], [1, -1], [-1, 0], [0, -1], [0, 1]],[[1, 0], [1, 1], [-1, 1], [-1, -1], [1, -1], [-1, 0], [0, -1], [0, 1]]],
              'q': ['black queen', 8, [[1,0], [1,1], [0,1], [-1,1], [-1,0], [-1,-1], [0,-1], [1,-1]],[[1,0], [1,1], [0,1], [-1,1], [-1,0], [-1,-1], [0,-1], [1,-1]]],
              'b': ['black bishop', 8, [[1, -1], [1, 1],[-1, -1], [-1, 1]], [[1, -1], [1, 1], [-1, -1], [-1, 1]]],
              'r': ['black rook', 8, [[0, -1], [0, 1],[-1, 0], [1, 0]], [[0, -1], [0, 1],[-1, 0], [1, 0]]],
              'p': ['black pawn', 1, [[0, 1], [-1, -1], [1, -1]], [[-1, -1],[1, -1]]],
              'n': ['black knight', 8, [[1,-2],[2,-1],[2,1],[1,2],[-1,-2],[-2,-1],[-2,1],[-1,2]] ,[[1,-2],[2,-1],[2,1],[1,2],[-1,-2],[-2,-1],[-2,1],[-1,2]]]}
        self.board = tk.Canvas(root, width=900, height=900, bg='gray')
        self.board.grid(row=0, column=0)
        for row in range(8):
            for column in range(8):
                if ((row + column) % 2) == 0 :
                    self.board.create_rectangle((100*row+50), (100*column+50), (100*row+150), (100*column+150), fill='dark goldenrod',outline="black")
                else:
                    self.board.create_rectangle((100*row+50), (100*column+50), (100*row+150), (100*column+150), fill='grey',outline="black")

    def playpiece(self):
        for row in range(8):
            for column in range(8):
                i, j = 100*row+100, 100*column+100
                #self.chessboard[row][column]
                self.board.create_text(i,j, text=self.board[row][column])
        print(self.playpiece)

    def print_board(self):
        horizontal = '-----------------'
        for row in self.board:
            s = '|'
            for piece in row:
                s += piece + '|'
            print(horizontal)
            print(s)
        print(horizontal)

    def piece_color(self, piece):
        if piece == " ":
            return " "
        elif piece == piece.upper():
            return 'white'
        else:
            return 'black'

    def check_move_piece(self, board, current_pos, new_pos):
        (x1, y1) = (current_pos[0], current_pos[1])
        (x2, y2) = (new_pos[0], new_pos[1])
        number, normalized = (x2-x1, y2-y1)
        piece = board[y1][x1]
        piece2 = board[y2][x2]
        if min(current_pos) < 0 or max(current_pos) > 7 or min(new_pos) < 0 or max(new_pos) > 7:
            return False
        if piece == ' ':
            return False
        if number == 0:
            return False
        if piece.upper() == 'P':  # pawns move differently than everyone else
            if number > 2:
                return False
            if number == 2:
                if ((self.piece_color(piece) == 'black' and y1 == 1) or (self.piece_color(piece) == 'white' and y1 == 6)) and normalized in self.pieces[piece][2]:
                    try:
                        xmid = int((x1+x2)/2)
                        ymid = int((y1+y2)/2)
                    except ValueError:
                        return False
                    if board[ymid][xmid] != ' ' or piece2 != ' ':
                        return False
                    else:
                        return True
                else:
                    return False
                    # is the normalized in the possible moves?
                    # is there a piece in between current position and the moved position?
                    # is there a piece at the moved position?

            else:  # number = 1
                if normalized in self.pieces[piece][2] and normalized == ' ':
                    return True
                elif normalized in self.pieces[piece][3] and self.piece_color(piece) != self.piece_color(piece2):
                    return True
                else:
                    return False

    def check_move_king(self, board, current_pos, new_pos):
    # create a new board where we moved the piece
        new_board = copy.copy(board)
        piece = new_board[current_pos[1]][current_pos[0]]
        new_board[new_pos[1]][new_pos[0]][0][0] = piece
        new_board[new_pos[1]][new_pos[0]] = ' '
        # find our king
        king_pos = [-1, -1]
        for row in range(8):
            for column in range(8):
                if new_board[row][column].upper() == 'K' and self.piece_color(new_board[row][column]) == self.piece_color(piece):
                    king_pos = [row][column]
                # can anyone take our king
                if king_pos != [-1, -1]:
                    for row in new_board:
                        for column in row:
                            if self.check_move_piece(new_board,[row, column], king_pos) and self.piece_color(new_board[row][column]) != self.piece_color(piece):
                                return False
                else:
                    return False


    def move(self, current_pos, new_pos):
        self.piece = self.chessboard[current_pos[1]][current_pos[0]]
        if self.check_move_piece(self.chessboard, current_pos, new_pos):
            #if check_move_king(board, current_pos, new_pos):
               self.chessboard[current_pos[1]][current_pos[0]] = " "
               self.chessboard[new_pos[1]][new_pos[0]] = self.piece
               self.print_board()



root = tk.Tk()
play = Board(root)
root.mainloop()


