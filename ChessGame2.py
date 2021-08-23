import tkinter as tk
from chessBoard import ChessBoard as CB
from chessPiece import ChessPiece as CP
from chessPiece import PieceMoves as CPM


class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        # self.pack()
        self.gamebtnFont = "Courier 36"
        self.image_dirs = {'BB': 'static/Black Bishop.png', 'BK': 'static/Black King.png',
                           'BN': 'static/Black Knight.png',
                           'BP': 'static/Black Pawn.png', 'BQ': 'static/Black Queen.png', 'BR': 'static/Black Rook.png',
                           'WB': 'static/White Bishop.png', 'WK': 'static/White King.png',
                           'WN': 'static/White Knight.png',
                           'WP': 'static/White Pawn.png', 'WQ': 'static/White Queen.png', 'WR': 'static/White Rook.png',
                           '  ': 'static/Blank.png'}
        self.text_image = {}
        self.gameBoardStart = [
            [CP('R', 'static/Black Rook.png', [CPM([1, 0]), CPM([0, -1]), CPM([-1, 0]), CPM([0, -1])], 1),
             CP('N', 'static/Black Knight.png', [CPM([2, 1], enemy_jump=True, ally_jump=True, mod_number=1),
                                                 CPM([2, -1], enemy_jump=True, ally_jump=True, mod_number=1),
                                                 CPM([1, -2], enemy_jump=True, ally_jump=True, mod_number=1),
                                                 CPM([-1, -2], enemy_jump=True, ally_jump=True, mod_number=1),
                                                 CPM([-2, -1], enemy_jump=True, ally_jump=True, mod_number=1),
                                                 CPM([-2, 1], enemy_jump=True, ally_jump=True, mod_number=1),
                                                 CPM([-1, 2], enemy_jump=True, ally_jump=True, mod_number=1),
                                                 CPM([1, 2], enemy_jump=True, ally_jump=True, mod_number=1)], 1),
             CP('B', 'static/Black Bishop.png', [CPM([1, 1]), CPM([1, -1]), CPM([-1, 1]), CPM([-1, -1])], 1),
             CP('Q', 'static/Black Queen.png', [CPM([1, 0]), CPM([0, -1]), CPM([-1, 0]), CPM([0, -1]),
                                                CPM([1, 0]), CPM([0, -1]), CPM([-1, 0]), CPM([0, -1])], 1),
             CP('K', 'static/Black King.png', [CPM([1, 0], mod_number=1),
                                               CPM([0, -1], mod_number=1),
                                               CPM([-1, 0], mod_number=1),
                                               CPM([0, -1], mod_number=1),
                                               CPM([1, 0], mod_number=1),
                                               CPM([0, -1], mod_number=1),
                                               CPM([-1, 0], mod_number=1),
                                               CPM([0, -1], mod_number=1)], 1),
             CP('B', 'static/Black Bishop.png', [CPM([1, 1]), CPM([1, -1]), CPM([-1, 1]), CPM([-1, -1])], 1),
             CP('N', 'static/Black Knight.png', [CPM([2, 1], enemy_jump=True, ally_jump=True, mod_number=1),
                                                 CPM([2, -1], enemy_jump=True, ally_jump=True, mod_number=1),
                                                 CPM([1, -2], enemy_jump=True, ally_jump=True, mod_number=1),
                                                 CPM([-1, -2], enemy_jump=True, ally_jump=True, mod_number=1),
                                                 CPM([-2, -1], enemy_jump=True, ally_jump=True, mod_number=1),
                                                 CPM([-2, 1], enemy_jump=True, ally_jump=True, mod_number=1),
                                                 CPM([-1, 2], enemy_jump=True, ally_jump=True, mod_number=1),
                                                 CPM([1, 2], enemy_jump=True, ally_jump=True, mod_number=1)], 1),
             CP('R', 'static/Black Rook.png', [CPM([1, 0]), CPM([0, -1]), CPM([-1, 0]), CPM([0, -1])], 1)],
            [CP('P', 'static/Black Pawn.png', [CPM([0, -1], enemy_capture=False, mod_number=1),
                                               CPM([-1, -1], no_capture=False, mod_number=1),
                                               CPM([1, -1], no_capture=False, mod_number=1)], 1)] * 8,
            [[None] * 8] * 4,
            [CP('P', 'static/White Pawn.png', [CPM([0, 1], enemy_capture=False, mod_number=1),
                                               CPM([-1, 1], no_capture=False, mod_number=1),
                                               CPM([1, 1], no_capture=False, mod_number=1)], 0)] * 8,
            [CP('R', 'static/White Rook.png', [CPM([1, 0]), CPM([0, -1]), CPM([-1, 0]), CPM([0, -1])], 0),
             CP('N', 'static/White Knight.png', [CPM([2, 1], enemy_jump=True, ally_jump=True, mod_number=1),
                                                 CPM([2, -1], enemy_jump=True, ally_jump=True, mod_number=1),
                                                 CPM([1, -2], enemy_jump=True, ally_jump=True, mod_number=1),
                                                 CPM([-1, -2], enemy_jump=True, ally_jump=True, mod_number=1),
                                                 CPM([-2, -1], enemy_jump=True, ally_jump=True, mod_number=1),
                                                 CPM([-2, 1], enemy_jump=True, ally_jump=True, mod_number=1),
                                                 CPM([-1, 2], enemy_jump=True, ally_jump=True, mod_number=1),
                                                 CPM([1, 2], enemy_jump=True, ally_jump=True, mod_number=1)], 0),
             CP('B', 'static/White Bishop.png', [CPM([1, 1]), CPM([1, -1]), CPM([-1, 1]), CPM([-1, -1])], 0),
             CP('Q', 'static/White Queen.png', [CPM([1, 0]), CPM([0, -1]), CPM([-1, 0]), CPM([0, -1]),
                                                CPM([1, 0]), CPM([0, -1]), CPM([-1, 0]), CPM([0, -1])], 0),
             CP('K', 'static/White King.png', [CPM([1, 0], mod_number=1),
                                               CPM([0, -1], mod_number=1),
                                               CPM([-1, 0], mod_number=1),
                                               CPM([0, -1], mod_number=1),
                                               CPM([1, 0], mod_number=1),
                                               CPM([0, -1], mod_number=1),
                                               CPM([-1, 0], mod_number=1),
                                               CPM([0, -1], mod_number=1)], 0),
             CP('B', 'static/White Bishop.png', [CPM([1, 1]), CPM([1, -1]), CPM([-1, 1]), CPM([-1, -1])], 0),
             CP('N', 'static/White Knight.png', [CPM([2, 1], enemy_jump=True, ally_jump=True, mod_number=1),
                                                 CPM([2, -1], enemy_jump=True, ally_jump=True, mod_number=1),
                                                 CPM([1, -2], enemy_jump=True, ally_jump=True, mod_number=1),
                                                 CPM([-1, -2], enemy_jump=True, ally_jump=True, mod_number=1),
                                                 CPM([-2, -1], enemy_jump=True, ally_jump=True, mod_number=1),
                                                 CPM([-2, 1], enemy_jump=True, ally_jump=True, mod_number=1),
                                                 CPM([-1, 2], enemy_jump=True, ally_jump=True, mod_number=1),
                                                 CPM([1, 2], enemy_jump=True, ally_jump=True, mod_number=1)], 0),
             CP('R', 'static/White Rook.png', [CPM([1, 0]), CPM([0, -1]), CPM([-1, 0]), CPM([0, -1])], 0)]]
        self.gameBoard = CB(self.gameBoardStart)
        self.gameBoardWidgets = []
        self.clicked = None

        self.playerColours = ['W', 'B']
        self.colours = {'B': '#000000', 'W': '#FFFFFF', ' ': '#888888'}
        self.bg_colours = ['#FFFFFF', '#444444']
        self.bg_colours_selected = ['#DDDDDD', '#777777']
        self.text_image = {}
        self.fr_left = tk.Frame(main, width=550, height=550, borderwidth=5)
        self.fr_right = tk.Frame(main, width=170, height=550, borderwidth=0)
        self.create_widgets()

    def create_widgets(self):
        self.fr_left.grid(column=0, row=0)
        self.fr_left.grid_propagate(0)
        self.fr_right.grid(column=1, row=0)
        self.fr_right.grid_propagate(0)
        for img_dir in self.image_dirs:
            self.text_image[img_dir] = tk.PhotoImage(file=self.image_dirs[img_dir])
        for x in range(64):
            if x // 8 == 0:
                self.gameBoardWidgets.append([])
            self.gameBoardWidgets[-1].append(
                tk.Button(self.fr_left, image=self.gameBoard.gameBoard[x // 8][x % 8],
                          bg=self.bg_colours[(x + x // 8) % 2], font=self.gamebtnFont,
                          command=lambda i=(x % 8, x // 8): self.clickGameBoard(i)))
            self.gameBoardWidgets[-1][x].grid(column=x % 8, row=x // 8, sticky=tk.W + tk.E + tk.N + tk.S, padx=0, pady=0)

    def clickGameBoard(self, tile):
        if self.clicked == tile:
            self.clicked = None
        elif self.clicked:
            self.gameBoard.updateBoard(self.clicked, tile)
        else:
            self.clicked = tile
            for valid_tile in self.gameBoard.gameBoard.validMoves(tile):
                self.gameBoardWidgets[valid_tile[1]][valid_tile[0]].bg = self.bg_colours[0]


main = tk.Tk()
main.geometry("730x550")
main.title("Chess")
app = Application(master=main)
app.mainloop()
