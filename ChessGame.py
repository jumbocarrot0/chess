from tkinter import *
import random

# TO DO LIST:

playerTypes = [0, 0]
# 0 - Human, 1 - Random
playerColours = ['W', 'B']
bg_colours = ['#FFFFFF', '#444444']
bg_colours_selected = ['#DDDDDD', '#777777']
player = 0
validMoves = set()
clickMode = 'none'
clickedPiece = None
gameBoardStart = ['BR', 'BN', 'BB', 'BQ', 'BK', 'BB', 'BN', 'BR',
                  'BP', 'BP', 'BP', 'BP', 'BP', 'BP', 'BP', 'BP',
                  '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ',
                  '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ',
                  '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ',
                  '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ',
                  'WP', 'WP', 'WP', 'WP', 'WP', 'WP', 'WP', 'WP',
                  'WR', 'WN', 'WB', 'WQ', 'WK', 'WB', 'WN', 'WR']
gameBoardStart = ['  ', '  ', '  ', '  ', 'BK', '  ', '  ', '  ',
                  '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ',
                  '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ',
                  '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ',
                  '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ',
                  '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ',
                  '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ',
                  '  ', '  ', '  ', '  ', 'WK', 'WN', '  ', '  ']
colours = {'B': '#000000', 'W': '#FFFFFF', ' ': '#888888'}
image_dirs = {'BB': 'static/Black Bishop.png', 'BK': 'static/Black King.png', 'BN': 'static/Black Knight.png',
              'BP': 'static/Black Pawn.png', 'BQ': 'static/Black Queen.png', 'BR': 'static/Black Rook.png',
              'WB': 'static/White Bishop.png', 'WK': 'static/White King.png', 'WN': 'static/White Knight.png',
              'WP': 'static/White Pawn.png', 'WQ': 'static/White Queen.png', 'WR': 'static/White Rook.png',
              '  ': 'static/Blank.png'}
text_image = {}
coloursInverse = {colours[i]: i for i in colours}
moveHistory = []
importantMoves = {'WhiteKingFirstMove': {'piece': 'K', 'player': 0, 'tileFrom': 60},
                  'BlackKingFirstMove': {'piece': 'K', 'player': 1, 'tileFrom': 4},
                  'T0BlackRookFirstMove': {'piece': 'R', 'player': 1, 'tileFrom': 0},
                  'T7BlackRookFirstMove': {'piece': 'R', 'player': 1, 'tileFrom': 7},
                  'T56WhiteRookFirstMove': {'piece': 'R', 'player': 0, 'tileFrom': 57},
                  'T63WhiteRookFirstMove': {'piece': 'R', 'player': 0, 'tileFrom': 63},
                  }

for x in range(0, 16):
    importantMoves['T' + str((32 + x % 8) - (x // 8) * 8) + 'PawnFirstMove'] = {'piece': 'P', 'player': x // 8,
                                                                                'tileFrom': (48 + x % 8) - (
                                                                                        x // 8) * 40}

print(importantMoves)


def isTileColourSame(customGameBoard, tileFrom, tileTo):
    if customGameBoard[tileFrom]['fg'] == customGameBoard[tileTo]['fg']:
        return True
    elif customGameBoard[tileFrom]['fg'] != customGameBoard[tileTo]['fg']:
        return False


def possibleMoves(customGameBoard, player, pieceSpecific=False, checkKing=False, excludeIllegalMoves=False):
    validMoves = set()
    for tile in range(0, len(customGameBoard)):
        if pieceSpecific:
            newList = []
            if customGameBoard[tile]['fg'] == colours[playerColours[player]]:
                newList += anyPieceMove(customGameBoard, tile, excludeIllegalMoves, checkKing=checkKing)
            validMoves.add(newList)
        else:
            if customGameBoard[tile]['fg'] == colours[playerColours[player]]:
                validMoves.update(anyPieceMove(customGameBoard, tile, excludeIllegalMoves, checkKing=checkKing))
    return validMoves


def rookMoves(customGameBoard, tileOrigin):
    validRookMoves = []
    move_additons = [-8, -1, 1, 8]
    for addition in move_additons:
        tileCheck = tileOrigin + addition
        if tileCheck not in range(0, 64) or (tileCheck // 8 != tileOrigin // 8 and tileCheck % 8 != tileOrigin % 8):
            continue
        if not isTileColourSame(customGameBoard, tileCheck, tileOrigin):
            validRookMoves.append(tileCheck)
        while tileCheck in range(0, 64) and not isTileColourSame(customGameBoard, tileOrigin, tileCheck) and \
                (tileCheck // 8 == tileOrigin // 8 or tileCheck % 8 == tileOrigin % 8):
            validRookMoves.append(tileCheck)
            if customGameBoard[tileCheck]['text'] != ' ':
                break
            tileCheck += addition
    return validRookMoves


def bishopMoves(customGameBoard, tileOrigin):
    validBishopMoves = []
    move_additons = [-9, -7, 7, 9]
    for addition in move_additons:
        tileCheck = tileOrigin + addition
        if tileCheck not in range(0, 64) or (tileCheck // 8 - tileCheck % 8 != tileOrigin // 8 - tileOrigin % 8 and
                                             tileCheck // 8 + tileCheck % 8 != tileOrigin // 8 + tileOrigin % 8):
            continue
        if not isTileColourSame(customGameBoard, tileCheck, tileOrigin):
            validBishopMoves.append(tileCheck)
        while tileCheck in range(0, 64) and not isTileColourSame(customGameBoard, tileOrigin, tileCheck) and \
                (tileCheck // 8 - tileCheck % 8 == tileOrigin // 8 - tileOrigin % 8 or
                 tileCheck // 8 + tileCheck % 8 == tileOrigin // 8 + tileOrigin % 8):
            validBishopMoves.append(tileCheck)
            if customGameBoard[tileCheck]['text'] != ' ':
                break
            tileCheck += addition
    return validBishopMoves


def knightMoves(customGameBoard, tileOrigin):
    validKnightMoves = []
    move_additons = [-17, -15, -10, -6, 6, 10, 15, 17]
    for addition in move_additons:
        tileCheck = tileOrigin + addition
        if tileCheck not in range(0, 64):
            continue
        if abs(tileOrigin % 8 - tileCheck % 8) in [1, 2] and \
                not isTileColourSame(customGameBoard, tileCheck, tileOrigin):
            validKnightMoves.append(tileCheck)
    return validKnightMoves


def kingMoves(customGameBoard, tileOrigin, excludeDangerMoves=True):
    validKingMoves = []
    move_additons = [-9, -8, -7, -1, 1, 7, 8, 9]
    for addition in move_additons:
        tileCheck = tileOrigin + addition
        if tileCheck in range(0, 63):
            if not isTileColourSame(customGameBoard, tileOrigin, tileCheck):
                print('dangerMoves: ' + str(possibleMoves(customGameBoard, (player + 1) % 2)))
                customGameBoard2 = [{'text': tile['text'], 'fg': tile['fg']} for tile in gameBoard]
                customGameBoard2[tileCheck]['text'] = ' '
                customGameBoard2[tileCheck]['fg'] = colours[' ']
                if not excludeDangerMoves or tileCheck not in possibleMoves(customGameBoard2, (player + 1) % 2):
                    validKingMoves.append(tileCheck)
    if player == 0:
        # print('moveHistory: ' + str(moveHistory))
        if importantMoves['WhiteKingFirstMove'] not in moveHistory:
            dangerTiles = possibleMoves(customGameBoard, (player + 1) % 2)
            if importantMoves['T56WhiteRookFirstMove'] not in moveHistory:
                castle = True
                for x in [57, 58, 59]:
                    if customGameBoard[x]['text'] != ' ' or x in dangerTiles:
                        castle = False
                        break
                if castle:
                    validKingMoves.append(58)
            if importantMoves['T63WhiteRookFirstMove'] not in moveHistory:
                castle = True
                for x in [62, 61]:
                    if customGameBoard[x]['text'] != ' ' or x in dangerTiles:
                        castle = False
                        break
                if castle:
                    validKingMoves.append(62)
    if player == 1:
        # print('moveHistory: ' + str(moveHistory))
        if importantMoves['BlackKingFirstMove'] not in moveHistory:
            dangerTiles = possibleMoves(customGameBoard, (player + 1) % 2)
            if importantMoves['T0BlackRookFirstMove'] not in moveHistory:
                castle = True
                for x in [1, 2, 3]:
                    if customGameBoard[x]['text'] != ' ' or x in dangerTiles:
                        castle = False
                        break
                if castle:
                    validKingMoves.append(2)
            if importantMoves['T7BlackRookFirstMove'] not in moveHistory:
                castle = True
                for x in [5, 6]:
                    if customGameBoard[x]['text'] != ' ' or x in dangerTiles:
                        castle = False
                        break
                if castle:
                    validKingMoves.append(6)
    return validKingMoves


def pawnMoves(customGameBoard, tileOrigin):
    validPawnMoves = []
    if customGameBoard[tileOrigin]['fg'] == colours['W']:
        if customGameBoard[tileOrigin - 8]['fg'] == colours[' ']:
            validPawnMoves.append(tileOrigin - 8)
            if tileOrigin // 8 == 6 and customGameBoard[tileOrigin - 16]['fg'] == colours[' ']:
                validPawnMoves.append(tileOrigin - 16)
        if tileOrigin % 8 != 7:
            if customGameBoard[tileOrigin - 7]['fg'] == colours['B']:
                validPawnMoves.append(tileOrigin - 7)
            elif customGameBoard[tileOrigin + 1]['fg'] == colours['B'] and \
                    customGameBoard[tileOrigin + 1]['text'] == 'P' and \
                    moveHistory[-1] == importantMoves['T' + str((tileOrigin + 1) % 8 + 24) + 'PawnFirstMove']:
                validPawnMoves.append(tileOrigin - 7)
        if tileOrigin % 8 != 0:
            if customGameBoard[tileOrigin - 9]['fg'] == colours['B']:
                validPawnMoves.append(tileOrigin - 9)
            elif customGameBoard[tileOrigin - 1]['fg'] == colours['B'] and \
                    customGameBoard[tileOrigin - 1]['text'] == 'P' and \
                    moveHistory[-1] == importantMoves['T' + str((tileOrigin - 1) % 8 + 24) + 'PawnFirstMove']:
                validPawnMoves.append(tileOrigin - 9)
    elif customGameBoard[tileOrigin]['fg'] == colours['B']:
        if customGameBoard[tileOrigin + 8]['fg'] == colours[' ']:
            validPawnMoves.append(tileOrigin + 8)
            if tileOrigin // 8 == 1 and customGameBoard[tileOrigin + 16]['fg'] == colours[' ']:
                validPawnMoves.append(tileOrigin + 16)
        if tileOrigin % 8 != 0:
            if customGameBoard[tileOrigin + 7]['fg'] == colours['W']:
                validPawnMoves.append(tileOrigin + 7)
            elif customGameBoard[tileOrigin - 1]['fg'] == colours['W'] and \
                    customGameBoard[tileOrigin - 1]['text'] == 'P' and \
                    moveHistory[-1] == importantMoves['T' + str((tileOrigin - 1) % 8 + 32) + 'PawnFirstMove']:
                validPawnMoves.append(tileOrigin + 7)
        if tileOrigin % 8 != 7:
            if customGameBoard[tileOrigin + 9]['fg'] == colours['W']:
                validPawnMoves.append(tileOrigin + 9)
            elif customGameBoard[tileOrigin + 1]['fg'] == colours['W'] and \
                    customGameBoard[tileOrigin + 1]['text'] == 'P' and \
                    moveHistory[-1] == importantMoves['T' + str((tileOrigin + 1) % 8 + 32) + 'PawnFirstMove']:
                validPawnMoves.append(tileOrigin + 9)
    return validPawnMoves


def anyPieceMove(customGameBoard, tileOrigin, excludeIllegalMoves, checkKing=True):
    validPieceMoves = []
    if gameBoard[tileOrigin]['text'][0] == 'R':
        validPieceMoves += rookMoves(customGameBoard, tileOrigin)
    elif gameBoard[tileOrigin]['text'][0] == 'N':
        validPieceMoves += knightMoves(customGameBoard, tileOrigin)
    elif gameBoard[tileOrigin]['text'][0] == 'B':
        validPieceMoves += bishopMoves(customGameBoard, tileOrigin)
    elif gameBoard[tileOrigin]['text'][0] == 'Q':
        validPieceMoves += rookMoves(customGameBoard, tileOrigin)
        validPieceMoves += bishopMoves(customGameBoard, tileOrigin)
    elif gameBoard[tileOrigin]['text'][0] == 'K' and checkKing:
        validPieceMoves += kingMoves(customGameBoard, tileOrigin)
    elif gameBoard[tileOrigin]['text'][0] == 'P':
        validPieceMoves += pawnMoves(customGameBoard, tileOrigin)
    if excludeIllegalMoves and 0 == 0:
        # print('anyPieceMove customGameBoard: ' + str(customGameBoard))
        # print('Valid Moves: ' + str(validPieceMoves))
        GameBoardSource = [{'text': tile['text'], 'fg': tile['fg']} for tile in gameBoard]
        for index, move in enumerate(validPieceMoves):
            customGameBoard = list(GameBoardSource)
            customGameBoard[move] = dict(customGameBoard[tileOrigin])
            customGameBoard[tileOrigin]['text'] = ' '
            customGameBoard[tileOrigin]['fg'] = colours[' ']
            # print('anyPieceMove customGameBoard2: ' + str(customGameBoard))
            if findKing(player) in possibleMoves(customGameBoard, (player + 1) % 2):
                # print('dangerTiles: ' + str(possibleMoves(customGameBoard)))
                validPieceMoves[index] = -1
        while -1 in validPieceMoves:
            validPieceMoves.remove(-1)
        # print('Valid Legal Moves: ' + str(validPieceMoves))
    return validPieceMoves


def checkCheck(customGameBoard, tileKing, checkMateCheck):
    global gameBoard
    dangerMoves = possibleMoves(gameBoard, (player + 1) % 2)
    if tileKing in dangerMoves:
        checkMate = True
        for index, tile in enumerate(gameBoard):
            if tile['fg'] == colours[playerColours[player]]:
                if anyPieceMove(customGameBoard, index, True):
                    checkMate = False
                    break
        if checkMate and checkMateCheck:
            endGame((player + 1) % 2)
            return False
        else:
            return True
    else:
        staleMate = True
        for index, tile in enumerate(gameBoard):
            if tile['fg'] == colours[playerColours[player]]:
                if anyPieceMove(customGameBoard, index, True):
                    staleMate = False
                    break
        if staleMate and checkMateCheck:
            endGame(-1)
        return False


def findKing(player):
    for index, gameTile in enumerate(gameBoard):
        if gameTile['text'] == 'K' and gameTile['fg'] == colours[playerColours[player]]:
            return index


def clickGameBoard(tile):
    global player, clickMode, clickedPiece, validMoves
    if clickMode == 'select':
        if coloursInverse[gameBoard[tile]['fg']] == playerColours[player]:
            clickedPiece = tile
            gameBoard[clickedPiece]['bg'] = bg_colours_selected[bg_colours.index(gameBoard[clickedPiece]['bg'])]
            validMoves = anyPieceMove(gameBoard, tile, True)
            for validTile in validMoves:
                try:
                    gameBoard[validTile]['bg'] = bg_colours_selected[bg_colours.index(gameBoard[validTile]['bg'])]
                except ValueError:
                    pass
            clickMode = 'move'
    elif clickMode == 'move':
        if tile in validMoves:
            if gameBoard[tile]['text'] == ' ' and gameBoard[clickedPiece]['text'] == 'P':
                if clickedPiece - tile in [9, -7]:
                    gameBoard[clickedPiece - 1].config(text=' ', fg=colours[' '], image='')
                if clickedPiece - tile in [7, -9]:
                    gameBoard[clickedPiece + 1].config(text=' ', fg=colours[' '], image='')
            gameBoard[tile].config(text=gameBoard[clickedPiece]['text'], fg=gameBoard[clickedPiece]['fg'],
                                   image=gameBoard[clickedPiece]['image'])
            gameBoard[clickedPiece].config(text=' ', fg=colours[' '], image=text_image['  '])
            # Castling Checks
            if importantMoves['WhiteKingFirstMove'] not in moveHistory and player == 0 and clickedPiece == 60:
                if tile == 62:
                    gameBoard[61].config(text=gameBoard[63]['text'], fg=gameBoard[63]['fg'],
                                         image=gameBoard[63]['image'])
                    gameBoard[63].config(text=' ', fg=colours[' '], image='')
                    moveHistory.append({'piece': 'R', 'player': 0, 'tileFrom': 63})
                if tile == 58:
                    gameBoard[59].config(text=gameBoard[56]['text'], fg=gameBoard[56]['fg'],
                                         image=gameBoard[56]['image'])
                    gameBoard[56].config(text=' ', fg=colours[' '], image='')
                    moveHistory.append({'piece': 'R', 'player': 0, 'tileFrom': 56})
            elif importantMoves['BlackKingFirstMove'] not in moveHistory and player == 1 and clickedPiece == 4:
                if tile == 6:
                    gameBoard[5].config(text=gameBoard[7]['text'], fg=gameBoard[7]['fg'], image=gameBoard[7]['image'])
                    gameBoard[7].config(text=' ', fg=colours[' '], image='')
                    moveHistory.append({'piece': 'R', 'player': 1, 'tileFrom': 7})
                if tile == 3:
                    gameBoard[4].config(text=gameBoard[0]['text'], fg=gameBoard[0]['fg'], image=gameBoard[0]['image'])
                    gameBoard[0].config(text=' ', fg=colours[' '], image='')
                    moveHistory.append({'piece': 'R', 'player': 1, 'tileFrom': 0})
            moveHistory.append({'piece': gameBoard[tile]['text'], 'player': player, 'tileFrom': clickedPiece})

            try:
                gameBoard[clickedPiece]['bg'] = bg_colours[bg_colours_selected.index(gameBoard[clickedPiece]['bg'])]
            except ValueError:
                pass
            for validTile in validMoves:
                gameBoard[validTile].config(bg=bg_colours[bg_colours_selected.index(gameBoard[validTile]['bg'])])
            if gameBoard[tile]['text'] == 'P' and tile // 8 in [0, 7]:
                gameBoard[tile]['text'] = 'Q'
                gameBoard[tile]['image'] = text_image[playerColours[player] + 'Q']

            endTurn()
        elif tile == clickedPiece:
            clickMode = 'select'
            gameBoard[clickedPiece]['bg'] = bg_colours[bg_colours_selected.index(gameBoard[clickedPiece]['bg'])]
            for validTile in validMoves:
                try:
                    gameBoard[validTile].config(bg=bg_colours[bg_colours_selected.index(gameBoard[validTile]['bg'])])
                except ValueError:
                    pass
    # print('Tile: ' + str(tile))
    # print(clickMode)


# -------------------- Enemy AI -----------------------------------


class ChessError(Exception):
    pass


def randomAIMove(customGameBoard, player):
    validMoves = possibleMoves(customGameBoard, player, pieceSpecific=True, checkKing=True, excludeIllegalMoves=True)
    print('AI validMoves: ' + str(validMoves))
    moveWeightings = set()
    for x in validMoves:
        moveWeightings.add(len(x))
    print('AI moveWeightings: ' + str(moveWeightings))
    if sum(moveWeightings) == 0:
        endGame((player - 1) % 2)
    randomNumb = random.randint(0, sum(moveWeightings) - 1)
    sumNumb = 0
    for i, x in enumerate(moveWeightings):
        sumNumb += x
        if randomNumb < sumNumb:
            return {'TileOrigin': i, 'TileTarget': random.choice(x)}
    raise ChessError('No move found for randomAIMove')


# ------------------------- Game Management -----------------------------


def gameStart():
    global player, validMoves, clickMode, clickedPiece, moveHistory
    player = 0
    validMoves = []
    clickMode = 'select'
    clickedPiece = None
    moveHistory = []

    lblMsg.config(text="Player 1's \n turn!")
    btnPlay.config(text="Restart")
    btnOption.config(state="disabled")
    for x in range(0, 64):
        gameBoard[x].config(text=gameBoardStart[x][1], fg=colours[gameBoardStart[x][0]],
                            image=text_image[gameBoardStart[x]])


def endTurn():
    global player, gameBoard, clickMode
    player = (player + 1) % 2
    message = "Player " + str(player + 1) + "'s \n turn!"
    if checkCheck(gameBoard, findKing(player), True):
        message += "\nCheck!"
    if clickMode != 'none':
        lblMsg.config(text=message)
        clickMode = 'select'
        if playerTypes[player] == 1:
            randomAIResults = randomAIMove(gameBoard, player)
            print('Result: ' + str(randomAIResults))
            clickGameBoard(randomAIResults['TileOrigin'])
            clickGameBoard(randomAIResults['TileTarget'])


def endGame(winner):
    global clickMode
    print('Winner!')

    btnPlay.config(text="Play")
    if winner == 0:
        lblMsg.config(text="Checkmate\nPlayer 1 \n Wins!")
    if winner == 1:
        lblMsg.config(text="Checkmate\nPlayer 2 \n Wins!")
    if winner == -1:
        lblMsg.config(text="Stalemate!")

    clickMode = 'none'
    btnOption.config(state="active")


def exitGame():
    exit()


main = Tk()
main.geometry("730x550")
main.title("Chess")

fr_left = Frame(main, width=550, height=550, borderwidth=5)
fr_right = Frame(main, width=170, height=550, borderwidth=0)

fr_left.grid(column=0, row=0)
fr_left.grid_propagate(0)
fr_right.grid(column=1, row=0)
fr_right.grid_propagate(0)

# Left Frame Widgets

gamebtnFont = "Courier 36"
gameBoard = []
for img_dir in image_dirs:
    text_image[img_dir] = PhotoImage(file=image_dirs[img_dir])
for x in range(0, 64):
    gameBoard.append(Button(fr_left, text=gameBoardStart[x][1], image=text_image[gameBoardStart[x]],
                            bg=bg_colours[(x + x // 8) % 2], fg=colours[gameBoardStart[x][0]], font=gamebtnFont,
                            command=lambda i=x: clickGameBoard(i)))
    gameBoard[x].grid(column=x % 8, row=x // 8, sticky=W + E + N + S, padx=0, pady=0)

# Right Frame Widgets

btnFont = "Arial 24"

btnPlay = Button(fr_right, text="Play", command=gameStart, font=btnFont, width=8)
btnOption = Button(fr_right, text="Options", font=btnFont, width=8)
btnExit = Button(fr_right, text="Exit", command=exitGame, font=btnFont, width=8)
lblMsg = Label(fr_right, text="Hello", font=btnFont, width=8)

btnPlay.grid(column=0, row=0, sticky=W + E, columnspan=1, pady=1, padx=5)
btnOption.grid(column=0, row=1, sticky=W + E, columnspan=1, pady=1, padx=5)
btnExit.grid(column=0, row=2, sticky=W + E, columnspan=1, pady=1, padx=5)
lblMsg.grid(column=0, row=3, sticky=W + E, columnspan=1, pady=4, padx=5)

main.mainloop()
