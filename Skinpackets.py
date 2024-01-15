import Values

chosenPacket = Values.chosenSkinPacket
dirLocation = Values.dirLocation

dirName = chosenPacket + "Skins/"
fileName = dirLocation + dirName

icon = fileName + "Icon.ico"

whiteKing = fileName + "WhiteKing.png"
whiteQueen = fileName + "WhiteQueen.png"
whiteBishop = fileName + "WhiteBishop.png"
whiteKnight = fileName + "WhiteKnight.png"
whiteRook = fileName + "WhiteRook.png"
whitePawn = fileName + "WhitePawn.png"

blackKing = fileName + "BlackKing.png"
blackQueen = fileName + "BlackQueen.png"
blackBishop = fileName + "BlackBishop.png"
blackKnight = fileName + "BlackKnight.png"
blackRook = fileName + "BlackRook.png"
blackPawn = fileName + "BlackPawn.png"

lobbySound = fileName + "LobbySound.mp3"
hitSound = fileName + "HitSound.mp3"
hitEnPassanteSound = fileName + "HitEnPassanteSound.mp3"
checkSound = fileName + "CheckSound.mp3"
winSound = fileName + "WinSound.mp3"
loseSound = fileName + "LoseSound.mp3"
pattSound = fileName + "PattSound.mp3"


def updateAll():
    global chosenPacket
    global dirLocation
    global dirName
    global fileName

    chosenPacket = Values.chosenSkinPacket
    dirLocation = Values.dirLocation

    dirName = chosenPacket + "Skins/"
    fileName = dirLocation + dirName

    global icon

    global whiteKing
    global whiteQueen
    global whiteBishop
    global whiteKnight
    global whiteRook
    global whitePawn

    global blackKing
    global blackQueen
    global blackBishop
    global blackKnight
    global blackRook
    global blackPawn

    global lobbySound
    global hitSound
    global hitEnPassanteSound
    global checkSound
    global winSound
    global loseSound
    global pattSound

    icon = fileName + "Icon.ico"

    whiteKing = fileName + "WhiteKing.png"
    whiteQueen = fileName + "WhiteQueen.png"
    whiteBishop = fileName + "WhiteBishop.png"
    whiteKnight = fileName + "WhiteKnight.png"
    whiteRook = fileName + "WhiteRook.png"
    whitePawn = fileName + "WhitePawn.png"

    blackKing = fileName + "BlackKing.png"
    blackQueen = fileName + "BlackQueen.png"
    blackBishop = fileName + "BlackBishop.png"
    blackKnight = fileName + "BlackKnight.png"
    blackRook = fileName + "BlackRook.png"
    blackPawn = fileName + "BlackPawn.png"

    lobbySound = fileName + "LobbySound.mp3"
    hitSound = fileName + "HitSound.mp3"
    hitEnPassanteSound = fileName + "HitEnPassanteSound.mp3"
    checkSound = fileName + "CheckSound.mp3"
    winSound = fileName + "WinSound.mp3"
    loseSound = fileName + "LoseSound.mp3"
    pattSound = fileName + "PattSound.mp3"


def updateWhite(pack):
    global whiteKing
    global whiteQueen
    global whiteBishop
    global whiteKnight
    global whiteRook
    global whitePawn

    whiteDirName = pack + "Skins/"
    whiteFileName = dirLocation + whiteDirName

    whiteKing = whiteFileName + "WhiteKing.png"
    whiteQueen = whiteFileName + "WhiteQueen.png"
    whiteBishop = whiteFileName + "WhiteBishop.png"
    whiteKnight = whiteFileName + "WhiteKnight.png"
    whiteRook = whiteFileName + "WhiteRook.png"
    whitePawn = whiteFileName + "WhitePawn.png"


def updateBlack(pack):
    global blackKing
    global blackQueen
    global blackBishop
    global blackKnight
    global blackRook
    global blackPawn

    blackDirName = pack + "Skins/"
    blackFileName = dirLocation + blackDirName

    blackKing = blackFileName + "BlackKing.png"
    blackQueen = blackFileName + "BlackQueen.png"
    blackBishop = blackFileName + "BlackBishop.png"
    blackKnight = blackFileName + "BlackKnight.png"
    blackRook = blackFileName + "BlackRook.png"
    blackPawn = blackFileName + "BlackPawn.png"
