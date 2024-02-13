import math
import Chess

# piece-square tables für alle figuren die angeben wie gut sie auf den jeweiligen feldern positioniert sind
pawnTable = {
    1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0,
    9: 5, 10: 10, 11: 10, 12: -20, 13: -20, 14: 10, 15: 10, 16: 5,
    17: 5, 18: -5, 19: -10, 20: 0, 21: 0, 22: -10, 23: -5, 24: 5,
    25: 0, 26: 0, 27: 0, 28: 20, 29: 20, 30: 0, 31: 0, 32: 0,
    33: 5, 34: 5, 35: 10, 36: 25, 37: 25, 38: 10, 39: 5, 40: 5,
    41: 10, 42: 10, 43: 20, 44: 30, 45: 30, 46: 20, 47: 10, 48: 10,
    49: 50, 50: 50, 51: 50, 52: 50, 53: 50, 54: 50, 55: 50, 56: 50,
    57: 0, 58: 0, 59: 0, 60: 0, 61: 0, 62: 0, 63: 0, 64: 0
}
knightTable = {
    1: -50, 2: -40, 3: -30, 4: -30, 5: -30, 6: -30, 7: -40, 8: -50,
    9: -40, 10: -20, 11: 0, 12: 5, 13: 5, 14: 0, 15: -20, 16: -40,
    17: -30, 18: 5, 19: 10, 20: 15, 21: 15, 22: 10, 23: 5, 24: -30,
    25: -30, 26: 0, 27: 15, 28: 20, 29: 20, 30: 15, 31: 0, 32: -30,
    33: -30, 34: 5, 35: 15, 36: 20, 37: 20, 38: 15, 39: 5, 40: -30,
    41: -30, 42: 0, 43: 10, 44: 15, 45: 15, 46: 10, 47: 0, 48: -30,
    49: -40, 50: -20, 51: 0, 52: 0, 53: 0, 54: 0, 55: -20, 56: -40,
    57: -50, 58: -40, 59: -30, 60: -30, 61: -30, 62: -30, 63: -40, 64: -50
}
bishopTable = {
    1: -20, 2: -10, 3: -10, 4: -10, 5: -10, 6: -10, 7: -10, 8: -20,
    9: -10, 10: 5, 11: 0, 12: 0, 13: 0, 14: 0, 15: 5, 16: -10,
    17: -10, 18: 10, 19: 10, 20: 10, 21: 10, 22: 10, 23: 10, 24: -10,
    25: -10, 26: 0, 27: 10, 28: 10, 29: 10, 30: 10, 31: 0, 32: -10,
    33: -10, 34: 5, 35: 5, 36: 10, 37: 10, 38: 5, 39: 5, 40: -10,
    41: -10, 42: 10, 43: 10, 44: 10, 45: 10, 46: 10, 47: 10, 48: -10,
    49: -10, 50: 5, 51: 0, 52: 0, 53: 0, 54: 0, 55: 5, 56: -10,
    57: -20, 58: -10, 59: -10, 60: -10, 61: -10, 62: -10, 63: -10, 64: -20,
}
rookTable = {
    64: 0, 63: 0, 62: 0, 61: 0, 60: 0, 59: 0, 58: 0, 57: 0,
    56: 5, 55: 10, 54: 10, 53: 10, 52: 10, 51: 10, 50: 10, 49: 5,
    48: -5, 47: 0, 46: 0, 45: 0, 44: 0, 43: 0, 42: 0, 41: -5,
    40: -5, 39: 0, 38: 0, 37: 0, 36: 0, 35: 0, 34: 0, 33: -5,
    32: -5, 31: 0, 30: 0, 29: 0, 28: 0, 27: 0, 26: 0, 25: -5,
    24: -5, 23: 0, 22: 0, 21: 0, 20: 0, 19: 0, 18: 0, 17: -5,
    16: -5, 15: 0, 14: 0, 13: 0, 12: 0, 11: 0, 10: 0, 9: -5,
    8: 0, 7: 0, 6: 0, 5: 5, 4: 5, 3: 0, 2: 0, 1: 0
}
queenTable = {
    1: -20, 2: -10, 3: -10, 4: -5, 5: -5, 6: -10, 7: -10, 8: -20,
    9: -10, 10: 0, 11: 0, 12: 0, 13: 0, 14: 0, 15: 0, 16: -10,
    17: -10, 18: 0, 19: 5, 20: 5, 21: 5, 22: 5, 23: 0, 24: -10,
    25: -5, 26: 0, 27: 5, 28: 5, 29: 5, 30: 5, 31: 0, 32: -5,
    33: 0, 34: 0, 35: 5, 36: 5, 37: 5, 38: 5, 39: 0, 40: -5,
    41: -10, 42: 5, 43: 5, 44: 5, 45: 5, 46: 5, 47: 0, 48: -10,
    49: -10, 50: 0, 51: 5, 52: 0, 53: 0, 54: 0, 55: 0, 56: -10,
    57: -20, 58: -10, 59: -10, 60: -5, 61: -5, 62: -10, 63: -10, 64: -20
}
kingTable = {
    64: -30, 63: -40, 62: -40, 61: -50, 60: -50, 59: -40, 58: -40, 57: -30,
    56: -30, 55: -40, 54: -40, 53: -50, 52: -50, 51: -40, 50: -40, 49: -30,
    48: -30, 47: -40, 46: -40, 45: -50, 44: -50, 43: -40, 42: -40, 41: -30,
    40: -30, 39: -40, 38: -40, 37: -50, 36: -50, 35: -40, 34: -40, 33: -30,
    32: -20, 31: -30, 30: -30, 29: -40, 28: -40, 27: -30, 26: -30, 25: -20,
    24: -10, 23: -20, 22: -20, 21: -20, 20: -20, 19: -20, 18: -20, 17: -10,
    16: 20, 15: 20, 14: 0, 13: 0, 12: 0, 11: 0, 10: 20, 9: 20,
    8: 20, 7: 30, 6: 10, 5: 0, 4: 0, 3: 10, 2: 30, 1: 20
}

#Funktion, die das aktuelle Board bewertet und einen Score anhand folgender Kriterien zurueckgibt:
# 1. Pure Materialkosten,
# 2. Position des Materials,
# (work in progress)


def evaluate():
    score = 0
    for field in Chess.chessField:
        # 0             1         2           3         4       5       6        7         8          9     10
        fieldKey, fieldNumber, figure, figureTexture, leftX, yAbove, centerX, centerY, figureColor, column, row = field
        if figureColor == "black":
            if figure.endswith("pawn"):
                score += pawnTable[field[1]] + 100
            elif figure.endswith("knight"):
                score += knightTable[field[1]] + 320
            elif figure.endswith("bishop"):
                score += bishopTable[field[1]] + 330
            elif figure.endswith("rook"):
                score += rookTable[field[1]] + 500
            elif figure.endswith("queen"):
                score += queenTable[field[1]] + 900
            elif figure.endswith("king"):
                score += kingTable[field[1]] + 20000

        if figureColor == "white":
            if figure.endswith("pawn"):
                score -= 100
            elif figure.endswith("knight"):
                score -= 320
            elif figure.endswith("bishop"):
                score -= 330
            elif figure.endswith("rook"):
                score -= 500
            elif figure.endswith("queen"):
                score -= 900
            elif figure.endswith("king"):
                score -= 20000
    return score


def makemove(move):
    return move


def unmakemove(move):
    return move


def getMoves():
    print("DEBUG")


def getMove():
    moves = []
    index = 0
    for field in Chess.chessField:
        Chess.selectedField = []
        fieldKey, fieldNumber, figure, figureTexture, leftX, yAbove, centerX, centerY, figureColor, column, row = field
        if figure.startswith("black"):
            Chess.selectedField.append((centerX, centerY, figure, fieldNumber, column, row))
            Chess.selectedField.append(index)
            #print(figure)
            if figure.endswith("pawn"):
                print("p", Chess.possiblePawnMoves())
                moves.append(Chess.possiblePawnMoves())
                moves.append(("P", "p"))
            elif figure.endswith("knight"):
                print("k", Chess.possibleKnightMoves())
                moves.append(Chess.possibleKnightMoves())
            elif figure.endswith("bishop"):
                moves.append(Chess.possibleBishopMoves())
            elif figure.endswith("rook"):
                moves.append(Chess.possibleRookMoves())
            elif figure.endswith("queen"):
                moves.append(Chess.possibleQueenMoves())
            elif figure.endswith("king"):
                moves.append(Chess.possibleKingMoves())

        index += 1
    #print(moves)
    #Chess.selectedField.append((centerX, centerY, figure, fieldNumber, column, row))
    #Chess.selectedField.append(0)
    #move = Chess.possiblePawnMoves()
    #print(move)
    #return move
        
#minimax algorithm with alpha beta pruning


def maxi(depth):
    if(depth == 0):
        return evaluate()
    max = -10000000
    allmoves = getMoves()
    for move in allmoves:
        score = mini(depth - 1)
        if (score > max):
            max = score
    return max


def mini(depth):
    if(depth == 0):
        return -evaluate()
    min = 10000000
    allmoves = getMoves()
    for move in allmoves:
        score = maxi(depth - 1)
        if (score > min):
            min = score
    return min


