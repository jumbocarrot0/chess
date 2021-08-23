class ChessPiece:
    def __init__(self, id, img, moves, player):
        self.id = id
        self.img = img
        self.moves = moves
        self.colour = player


class PieceMoves:
    def __init__(self, tile_mod,
                 mod_number=8,
                 enemy_capture=True,
                 ally_capture=False,
                 no_capture=True,
                 enemy_jump=False,
                 ally_jump=False):
        self.tileModifier = tile_mod
        self.modNumber = mod_number
        self.enemyCapture = enemy_capture
        self.allyCapture = ally_capture
        self.noCapture = no_capture
        self.enemyJump = enemy_jump
        self.allyJump = ally_jump
