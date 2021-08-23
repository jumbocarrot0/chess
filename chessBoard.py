from chessPiece import ChessPiece


class ChessBoard:
    def __init__(self, setup):
        self.gameBoard = setup

    def updateBoard(self, target, destination):
        self.gameBoard[destination[0]][destination[1]] = self.gameBoard[target[0]][target[1]]
        self.gameBoard[target[0]][target[1]] = '  '

    def checkThreatSquare(self, target):
        pass

    def validMoves(self, target):
        valid_tiles = []
        target_piece = self.gameBoard[target[0]][target[1]]
        if target_piece:
            for mod in target_piece.moves:
                for i in range(mod.mod_number):
                    dest_piece = self.gameBoard[target[0] + i * mod.tileMod[1]][target[1] + i * mod.tileMod[0]]
                    destination = [target[0] + i * mod.tileMod[0], target[1] + i * mod.tileMod[1]]
                    if not dest_piece:
                        if not mod.noCapture:
                            valid_tiles.append(destination)
                    elif dest_piece.player == target_piece.player:
                        if mod.allyCapture:
                            valid_tiles.append(destination)
                        if not mod.allyJump:
                            break
                    elif dest_piece.player != target_piece.player:
                        if mod.enemyCapture:
                            valid_tiles.append(destination)
                        if not mod.enemyJump:
                            break
        return valid_tiles
