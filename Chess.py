import Values
import Skinpackets as Skin
import botChess as BC
import pygame
import sys
import time
import threading
import socket
import pickle
import tkinter
from tkinter import ttk

if __name__ == "__main__":
    sys.exit("Starte Gamemode.py, um das Spiel zu starten")

screenW = Values.screenW
screenH = Values.screenH

mScreenW = screenW / 1000
mScreenH = screenH / 1000  # Teilen durch 1000, da das Schachfeld in einem 1000 x 1000 Feld eingerichtet ist

black = (0, 0, 0)
white = (250, 250, 250)
gray = (198, 198, 198)
red = (250, 0, 0)
darkGray = (128, 128, 128)
green = (0, 250, 0)

chessField = []


def resetChessField():
    global chessField

    # Schachfeld
                    #   0           1          2           3          4       5       6        7          8          9     10
    chessField = [  # fieldKey, fieldNumber, figure, figureTexture, leftX, yAbove, centerX, centerY, figureColor, column, row
        ("a8", 1, "black_1_rook", Skin.blackRook, 100 * mScreenW, 100 * mScreenH, 150 * mScreenW, 150 * mScreenH, "black", 1, 1), ("b8", 2, "black_knight", Skin.blackKnight, 200 * mScreenW, 100 * mScreenH, 250 * mScreenW, 150 * mScreenH, "black", 1, 2), ("c8", 3, "black_bishop", Skin.blackBishop, 300 * mScreenW, 100 * mScreenH, 350 * mScreenW, 150 * mScreenH, "black", 1, 3), ("d8", 4, "black_queen", Skin.blackQueen, 400 * mScreenW, 100 * mScreenH, 450 * mScreenW, 150 * mScreenH, "black", 1, 4), ("e8", 5, "black_king", Skin.blackKing, 500 * mScreenW, 100 * mScreenH, 550 * mScreenW, 150 * mScreenH, "black", 1, 5), ("f8", 6, "black_bishop", Skin.blackBishop, 600 * mScreenW, 100 * mScreenH, 650 * mScreenW, 150 * mScreenH, "black", 1, 6), ("g8", 7, "black_knight", Skin.blackKnight, 700 * mScreenW, 100 * mScreenH, 750 * mScreenW, 150 * mScreenH, "black", 1, 7), ("h8", 8, "black_2_rook", Skin.blackRook, 800 * mScreenW, 100 * mScreenH, 850 * mScreenW, 150 * mScreenH, "black", 1, 8),
        ("a7", 9, "black_pawn", Skin.blackPawn, 100 * mScreenW, 200 * mScreenH, 150 * mScreenW, 250 * mScreenH, "black", 2, 1), ("b7", 10, "black_pawn", Skin.blackPawn, 200 * mScreenW, 200 * mScreenH, 250 * mScreenW, 250 * mScreenH, "black", 2, 2), ("c7", 11, "black_pawn", Skin.blackPawn, 300 * mScreenW, 200 * mScreenH, 350 * mScreenW, 250 * mScreenH, "black", 2, 3), ("d7", 12, "black_pawn", Skin.blackPawn, 400 * mScreenW, 200 * mScreenH, 450 * mScreenW, 250 * mScreenH, "black", 2, 4), ("e7", 13, "black_pawn", Skin.blackPawn, 500 * mScreenW, 200 * mScreenH, 550 * mScreenW, 250 * mScreenH, "black", 2, 5), ("f7", 14, "black_pawn", Skin.blackPawn, 600 * mScreenW, 200 * mScreenH, 650 * mScreenW, 250 * mScreenH, "black", 2, 6), ("g7", 15, "black_pawn", Skin.blackPawn, 700 * mScreenW, 200 * mScreenH, 750 * mScreenW, 250 * mScreenH, "black", 2, 7), ("h7", 16, "black_pawn", Skin.blackPawn, 800 * mScreenW, 200 * mScreenH, 850 * mScreenW, 250 * mScreenH, "black", 2, 8),
        ("a6", 17, "", "", 100 * mScreenW, 300 * mScreenH, 150 * mScreenW, 350 * mScreenH, "", 3, 1), ("b6", 18, "", "", 200 * mScreenW, 300 * mScreenH, 250 * mScreenW, 350 * mScreenH, "", 3, 2), ("c6", 19, "", "", 300 * mScreenW, 300 * mScreenH, 350 * mScreenW, 350 * mScreenH, "", 3, 3), ("d6", 20, "", "", 400 * mScreenW, 300 * mScreenH, 450 * mScreenW, 350 * mScreenH, "", 3, 4), ("e6", 21, "", "", 500 * mScreenW, 300 * mScreenH, 550 * mScreenW, 350 * mScreenH, "", 3, 5), ("f6", 22, "", "", 600 * mScreenW, 300 * mScreenH, 650 * mScreenW, 350 * mScreenH, "", 3, 6), ("g6", 23, "", "", 700 * mScreenW, 300 * mScreenH, 750 * mScreenW, 350 * mScreenH, "", 3, 7), ("h6", 24, "", "", 800 * mScreenW, 300 * mScreenH, 850 * mScreenW, 350 * mScreenH, "", 3, 8),
        ("a5", 25, "", "", 100 * mScreenW, 400 * mScreenH, 150 * mScreenW, 450 * mScreenH, "", 4, 1), ("b5", 26, "", "", 200 * mScreenW, 400 * mScreenH, 250 * mScreenW, 450 * mScreenH, "", 4, 2), ("c5", 27, "", "", 300 * mScreenW, 400 * mScreenH, 350 * mScreenW, 450 * mScreenH, "", 4, 3), ("d5", 28, "", "", 400 * mScreenW, 400 * mScreenH, 450 * mScreenW, 450 * mScreenH, "", 4, 4), ("e5", 29, "", "", 500 * mScreenW, 400 * mScreenH, 550 * mScreenW, 450 * mScreenH, "", 4, 5), ("f5", 30, "", "", 600 * mScreenW, 400 * mScreenH, 650 * mScreenW, 450 * mScreenH, "", 4, 6), ("g5", 31, "", "", 700 * mScreenW, 400 * mScreenH, 750 * mScreenW, 450 * mScreenH, "", 4, 7), ("h5", 32, "", "", 800 * mScreenW, 400 * mScreenH, 850 * mScreenW, 450 * mScreenH, "", 4, 8),
        ("a4", 33, "", "", 100 * mScreenW, 500 * mScreenH, 150 * mScreenW, 550 * mScreenH, "", 5, 1), ("b4", 34, "", "", 200 * mScreenW, 500 * mScreenH, 250 * mScreenW, 550 * mScreenH, "", 5, 2), ("c4", 35, "", "", 300 * mScreenW, 500 * mScreenH, 350 * mScreenW, 550 * mScreenH, "", 5, 3), ("d4", 36, "", "", 400 * mScreenW, 500 * mScreenH, 450 * mScreenW, 550 * mScreenH, "", 5, 4), ("e4", 37, "", "", 500 * mScreenW, 500 * mScreenH, 550 * mScreenW, 550 * mScreenH, "", 5, 5), ("f4", 38, "", "", 600 * mScreenW, 500 * mScreenH, 650 * mScreenW, 550 * mScreenH, "", 5, 6), ("g4", 39, "", "", 700 * mScreenW, 500 * mScreenH, 750 * mScreenW, 550 * mScreenH, "", 5, 7), ("h4", 40, "", "", 800 * mScreenW, 500 * mScreenH, 850 * mScreenW, 550 * mScreenH, "", 5, 8),
        ("a3", 41, "", "", 100 * mScreenW, 600 * mScreenH, 150 * mScreenW, 650 * mScreenH, "", 6, 1), ("b3", 42, "", "", 200 * mScreenW, 600 * mScreenH, 250 * mScreenW, 650 * mScreenH, "", 6, 2), ("c3", 43, "", "", 300 * mScreenW, 600 * mScreenH, 350 * mScreenW, 650 * mScreenH, "", 6, 3), ("d3", 44, "", "", 400 * mScreenW, 600 * mScreenH, 450 * mScreenW, 650 * mScreenH, "", 6, 4), ("e3", 45, "", "", 500 * mScreenW, 600 * mScreenH, 550 * mScreenW, 650 * mScreenH, "", 6, 5), ("f3", 46, "", "", 600 * mScreenW, 600 * mScreenH, 650 * mScreenW, 650 * mScreenH, "", 6, 6), ("g3", 47, "", "", 700 * mScreenW, 600 * mScreenH, 750 * mScreenW, 650 * mScreenH, "", 6, 7), ("h3", 48, "", "", 800 * mScreenW, 600 * mScreenH, 850 * mScreenW, 650 * mScreenH, "", 6, 8),
        ("a2", 49, "white_pawn", Skin.whitePawn, 100 * mScreenW, 700 * mScreenH, 150 * mScreenW, 750 * mScreenH, "white", 7, 1), ("b2", 50, "white_pawn", Skin.whitePawn, 200 * mScreenW, 700 * mScreenH, 250 * mScreenW, 750 * mScreenH, "white", 7, 2), ("c2", 51, "white_pawn", Skin.whitePawn, 300 * mScreenW, 700 * mScreenH, 350 * mScreenW, 750 * mScreenH, "white", 7, 3), ("d2", 52, "white_pawn", Skin.whitePawn, 400 * mScreenW, 700 * mScreenH, 450 * mScreenW, 750 * mScreenH, "white", 7, 4), ("e2", 53, "white_pawn", Skin.whitePawn, 500 * mScreenW, 700 * mScreenH, 550 * mScreenW, 750 * mScreenH, "white", 7, 5), ("f2", 54, "white_pawn", Skin.whitePawn, 600 * mScreenW, 700 * mScreenH, 650 * mScreenW, 750 * mScreenH, "white", 7, 6), ("g2", 55, "white_pawn", Skin.whitePawn, 700 * mScreenW, 700 * mScreenH, 750 * mScreenW, 750 * mScreenH, "white", 7, 7), ("h2", 56, "white_pawn", Skin.whitePawn, 800 * mScreenW, 700 * mScreenH, 850 * mScreenW, 750 * mScreenH, "white", 7, 8),
        ("a1", 57, "white_1_rook", Skin.whiteRook, 100 * mScreenW, 800 * mScreenH, 150 * mScreenW, 850 * mScreenH, "white", 8, 1), ("b1", 58, "white_knight", Skin.whiteKnight, 200 * mScreenW, 800 * mScreenH, 250 * mScreenW, 850 * mScreenH, "white", 8, 2), ("c1", 59, "white_bishop", Skin.whiteBishop, 300 * mScreenW, 800 * mScreenH, 350 * mScreenW, 850 * mScreenH, "white", 8, 3), ("d1", 60, "white_queen", Skin.whiteQueen, 400 * mScreenW, 800 * mScreenH, 450 * mScreenW, 850 * mScreenH, "white", 8, 4), ("e1", 61, "white_king", Skin.whiteKing, 500 * mScreenW, 800 * mScreenH, 550 * mScreenW, 850 * mScreenH, "white", 8, 5), ("f1", 62, "white_bishop", Skin.whiteBishop, 600 * mScreenW, 800 * mScreenH, 650 * mScreenW, 850 * mScreenH, "white", 8, 6), ("g1", 63, "white_knight", Skin.whiteKnight, 700 * mScreenW, 800 * mScreenH, 750 * mScreenW, 850 * mScreenH, "white", 8, 7), ("h1", 64, "white_2_rook", Skin.whiteRook, 800 * mScreenW, 800 * mScreenH, 850 * mScreenW, 850 * mScreenH, "white", 8, 8)
    ]


resetChessField()

kingFields = [(50 * mScreenW, 350 * mScreenH, "black"), (50 * mScreenW, -350 * mScreenH, "white")]  # centerX, centerY, figureColor

selectedField = []
rochadeFigurePlace = []
lastPossibleFields = []
possibleHitFields = []
moveList = {}
schlagenEnPassant = [0, 0, 0]  # [move, sourceField, MoveToField] (move: Zug in dem der Bauer geschlagen werden könnte)
sEPHit = []
rochadeAllowed = True
rochadeMoved = [False, False, False, False, False, False]  # w_king, w_1_rook, w_2_rook, b_king, b_1_rook, b_2_rook | Falls bereits bewegt -> entsprechender Wert == True
activePlayer = "white"
activePlayerText = "Weiss"
enemy = "black"
yourColor = "white"
playerEnemy = "black"
playerEnemyText = "Schwarz"
inputAllowed = True
onlineConnection = False
onlineMode = False
moves = 0
returnValue = None
showPygameWindow = True
gameExit = False
turnChessField = False


def repaint():  # Funktion zum Zeichnen des Spielfeldes
    letters = ["8", "7", "6", "5", "4", "3", "2", "1", "a", "b", "c", "d", "e", "f", "g", "h"]
    if not onlineMode:
        if activePlayer == "black" and turnChessField:
            letters = ["1", "2", "3", "4", "5", "6", "7", "8", "h", "g", "f", "e", "d", "c", "b", "a"]
    else:
        if playerEnemy == "white":
            letters = ["1", "2", "3", "4", "5", "6", "7", "8", "h", "g", "f", "e", "d", "c", "b", "a"]
    letter = ""
    pygameWindow.fill((250, 250, 250))  # Komplettes Fenster weiß färben

    for i in range(0, 901, 100):  # Spaltenstriche
        for j in range(0, 901, 100):  # Zeilenstriche
            if (i + j) % 200 == 0 and not ((i == 0 or i == 900) or (j == 0 or j == 900)):
                color = white
            elif (i == 0 or i == 900) or (j == 0 or j == 900):
                color = darkGray
            else:
                color = gray
            if i == 0 and j == 0 and not onlineMode:
                if turnChessField:
                    color = green
                else:
                    color = red
            pygame.draw.rect(pygameWindow, color, (i * mScreenW, j * mScreenH, 100 * mScreenW, 100 * mScreenH))

            if (i == 0 or i == 900) or (j == 0 or j == 900):
                if i != 900 and j != 900:
                    textBackground = darkGray
                    if i == 0 and j == 0 and not onlineMode:
                        letter = "Drehen"
                        if turnChessField:
                            textBackground = green
                        else:
                            textBackground = red
                    elif i == 0:
                        letter = letters[j // 100 - 1]  # Wenn das Schachfeld gedreht wird, müssen sich auch die Feldbezeichnungen mit drehen
                    elif j == 0:
                        letter = letters[i // 100 - 1 + 8]
                    font = pygame.font.Font("freesansbold.ttf", 25)
                    text = font.render(letter, True, black, textBackground)
                    textRect = text.get_rect()
                    textRect.center = ((i + 50) * mScreenW, (j + 50) * mScreenH)  # Position des Textes
                    pygameWindow.blit(text, textRect)

    textCount = 0
    for move in range(moves - 4, moves + 1):  # Anzeigen der letzten 5 Züge am Rand
        try:
            font = pygame.font.Font(None, 25)
            text = font.render(moveList[move], True, black, darkGray)
            textRect = text.get_rect()
            textRect.center = (950 * mScreenW, 400 + (textCount * 25))  # Position des Textes
            pygameWindow.blit(text, textRect)
            textCount += 1
        except KeyError as ke:
            pass

    figureRepaint()


def figureRepaint():  # Funktion zum Zeichnen der Figuren
    for largeTupel in chessField:
        centerX = largeTupel[6]
        centerY = largeTupel[7]
        figureTexture = largeTupel[3]

        if figureTexture != "":
            image = pygame.image.load(figureTexture)
            image_rect = image.get_rect()

            a = (centerX - image_rect.width // 2)
            b = (centerY - image_rect.height // 2)

            if not onlineMode:
                if activePlayer == "black" and turnChessField:
                    a = -a + screenW - image_rect.width
                    b = -b + screenH - image_rect.height
            else:
                if playerEnemy == "white":
                    a = -a + screenW - image_rect.width
                    b = -b + screenH - image_rect.height

            pygameWindow.blit(image, (a, b))
    pygame.display.update()
       

def toast(message, duration=0, color=red):  # Funktion zum Anzeigen von "Toast-Nachrichten"
    font = pygame.font.Font(None, 50)
    text = font.render(message, True, color)

    toastWidth = text.get_width()
    toastHeight = text.get_height()
    toastRect = pygame.Rect(350 - toastWidth // 4, 350 - toastHeight // 4, toastWidth, toastHeight)  # Toast-Position

    textRect = text.get_rect(center=toastRect.center)
    pygameWindow.blit(text, textRect)

    pygame.display.flip()
    if duration != 0:
        pygame.time.wait(duration * 1000)
        repaint()


def startClient():  # Funktion zum Starten des Clients / Verbinden mit dem Server
    global clientSocket
    global playerEnemy
    global playerEnemyText
    global yourColor
    global onlineConnection

    while time.time() - gameStart <= 10 and not onlineConnection:  # Falls innerhalb von 10 Sekunden keine Verbindung hergestellt werden kann wird das Programm mit einem SystemExit beendet
        try:  # Falls keine Verbindung mit dem Server zustande kommt: Fehler abfangen, Programm durch Sys-exit beenden mit entsprechender Nachricht
            clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            clientSocket.connect(('jythonchess.de', 8888))  # Verbinden mit dem Server, falls möglich
            clientSocket.send("spielen".encode())
            openGames = clientSocket.recv(1024)  # Erhalten der offenen Spiellobby-Codes, damit dem Nutzer bekannt ist, welche Spielräume offen sind
            if openGames is not None:
                onlineConnection = True
                
            if time.time() - gameStart <= 3 and not onlineConnection:
                sys.exit("Es konnte keine Verbindung zum Server hergestellt werden")  # Mitteilung, dass kein Verbindungsaufbau möglich ist
            else:
                gameCode = informationDialog("Gib deinen Spielcode ein", "Willkommen! \nBitte gib einen Game-Code ein oder erstelle einen neuen \n" + openGames.decode(), "Gib einen Game-Code ein: ")
                if gameCode is None:
                    sys.exit("Dialog geschlossen!")
                else:
                    clientSocket.send(gameCode.encode())
                
                gameCreationSuccess = clientSocket.recv(1024)  # Auf Bestätigung des Servers warten

                playerEnemy = clientSocket.recv(1024).decode()  # Gegner-Farbe empfangen
                if playerEnemy == "white":
                    yourColor = "Schwarz"
                    playerEnemyText = "Weiss"
                else:
                    yourColor = "Weiss"
                    playerEnemyText = "Schwarz"
                informationDialog("Spiel Information", gameCreationSuccess.decode() + "\n\n--> Du spielst " + yourColor + " <--", "", False, True)

                receiveThread = threading.Thread(target=receiveMessages, args=(clientSocket,))
                receiveThread.start()  # Nachrichtenempfangs-Thread starten
                    
        except Exception as e:
            informationDialog("ERROR", "Fehler: {}".format(e))


def receiveMessages(cSocket):  # Funktion zum Empfangen von Anweisungen
    global rochadeAllowed
    global inputAllowed
    global showPygameWindow
    global gameExit

    try:
        while True:  # Muss durchgängig laufen, da zu jedem Zeitpunkt Bewegungen empfangen werden müssen
            checkMate = False
            stalemate = False
            data = cSocket.recv(1024)  # Empfangen der Nachricht
            if not data:  # Falls kein Zug gemacht wurde, ist der Inhalt der Nachricht 'None'. Nur nicht 'None'-Nachrichten weiter verarbeiten, sonst Fehlermeldung
                break

            if data == b"christmas":
                if playerEnemy == "white":
                    Skin.updateWhite("christmas")
                else:
                    Skin.updateBlack("christmas")
                continue

            if data == b"default":
                if playerEnemy == "white":
                    Skin.updateWhite("default")
                else:
                    Skin.updateBlack("default")
                continue
            
            if data == b"Mitspieler left game":  # Falls der Mitspieler das Spiel verlässt
                inputAllowed = False
                if gameExit:
                    informationDialog("Spiel verlassen!", "Du hast das Spiel verlassen")
                else:
                    informationDialog("Dein Mitspieler hat das Spiel verlassen", "Dein Mitspieler hat das Spiel verlassen! \n Ein Reconnect ist nicht möglich, zum spielen Programm neustarten!")
                showPygameWindow = False
                cSocket.close()
                break

            if data == b"You Won":  # Nachricht, die Erhalten wird, wenn der Gegner verliert
                pygame.mixer.music.load(Skin.winSound)
                pygame.mixer.music.play(0, 0.0)
                informationDialog("Schachmatt   |   " + yourColor + " gewinnt das Spiel", yourColor + " hat das Spiel gewonnen!")
                inputAllowed = False
                break
            
            if data == b"Draw":  # Nachricht, die Erhalten wird, wenn es zu einem Unentschieden kommt
                pygame.mixer.music.load(Skin.pattSound)
                pygame.mixer.music.play(0, 0.0)
                informationDialog("Patt   |   Niemand gewinnt das Spiel", "Unentschieden")
                inputAllowed = False
                break

            receivedTuple = pickle.loads(data)
            sField, mField = int(receivedTuple[0]), int(receivedTuple[1])
            figureMove(sField, mField)  # Erhaltene Bewegung umsetzen
            decolor()  # Entfärben aller Felder sowie leeren der dazugehörigen Listen
            playerChange()
            if activePlayer != playerEnemy:
                check = checkCheck()  # Überprüfen, ob der König des aktuellen Spielers im Schach steht
                if check:  # Aufrufen der Schachmatt-funktion nur, wenn ein König im Schach steht
                    rochadeAllowed = False
                    checkMate = checkCheckMate()
                if not check:
                    rochadeAllowed = True
                    stalemate = checkStalemate()
                if checkMate:
                    playerChange()  # Wechseln des Gegners, da für seine Figuren die möglichen Züge ermittelt werden sollen, und seine Figuren die Figuren des aktiven Spielers schlagen könnten
                    inputAllowed = False  # Weiteren Input nach Spielende verhindern
                    cSocket.send("You Won".encode())
                    pygame.mixer.music.load(Skin.loseSound)
                    pygame.mixer.music.play(0, 0.0)
                    informationDialog("Schachmatt   |   " + playerEnemyText + " gewinnt das Spiel", playerEnemyText + " hat das Spiel gewonnen!")
                    break
                    
                if not checkMate and check:
                    pygame.mixer.music.load(Skin.checkSound)
                    pygame.mixer.music.play(0, 0.0)
                    informationDialog("SCHACH", "Du stehst im Schach\nSchütze deinen König!")
                    
                if stalemate:
                    inputAllowed = False  # Weiteren Input nach Spielende verhindern
                    cSocket.send("Draw".encode())
                    pygame.mixer.music.load(Skin.pattSound)
                    pygame.mixer.music.play(0, 0.0)
                    informationDialog("Patt   |   Niemand gewinnt das Spiel", "Unentschieden")
                    break

    except Exception as e:
        informationDialog("ERROR", "Fehler beim Erhalten der Nachrichten: {}".format(e))


def informationDialog(title, text, inputStr="", returnInputAsBool=False, autoDestroy=False):  # Funktion zum Anzeigen eines Dialogfensters, mit welchem interagiert werden muss!
    global returnValue

    root = tkinter.Tk()
    root.title(title)

    returnValue = None

    def closeDialog():
        global returnValue

        if inputStr != "":
            inputValue = inputString.get()
            if inputValue is not None and inputValue != "":
                root.destroy()
                returnValue = inputValue
        else:
            root.destroy()

    label = ttk.Label(root, text=text + "\n\n" + inputStr)
    label.pack(expand=True, padx=25,  pady=10)

    if inputStr != "":
        inputString = ttk.Entry(root, width=40)
        inputString.pack(side="top", pady=10)

    continueButton = ttk.Button(root, text="Ok", command=closeDialog)
    continueButton.pack(side="bottom")

    if autoDestroy:
        root.destroy()
    root.mainloop()

    if returnInputAsBool:
        if returnValue == "True":
            returnValue = True
        else:
            returnValue = False
    return returnValue


def possiblePawnMoves():  # Funktion die alle möglichen Bewegungen für den ausgewählten Bauern zurückgibt
    global sEPHit
    
    repaintX, repaintY, rFigure, rFieldNumber, rColumn, rRow = selectedField[0]  # Entpacken des ausgewählten Feldes
    possibleMoves = []
    possibleHitFieldsPawn = []
    
    indexes = [-16, -9, -8, -7, 7, 8, 9, 16]  # Alle Indexe, um die sich ein Bauer bewegen kann | Negativ: Weiß Positiv: Schwarz
    for index in indexes:  # Durchlaufen aller Indexe
        sEPColor = False  # Falls True wird das Feld hinter dem Bauern rot gefärbt
        if (rFigure.startswith("black") and index > 0) or (rFigure.startswith("white") and index < 0):  # Überspringen der Indexe, um die sich ein schwarzer bzw. weißer Bauer nicht bewegen kann
            if 64 > rFieldNumber + index - 1 > -1:  # Überprüfen des Indexes, sodass keine Indexe außerhalb der Listenlänge abgefragt wird und es einen Fehler gibt
                field = chessField[rFieldNumber + index - 1]
                if (rRow == 1 and field[10] == 8) or (rRow == 8 and field[10] == 1):  # Abfrage, ob der Bauer am Spielfeldrand herauslaufen würde
                    continue
                if field[8] == "" or field[8] == enemy:  # Falls das zu überprüfende Feld leer ist oder ein Gegner auf diesem steht
                    if not (schlagenEnPassant[0] == moves and field[1] == schlagenEnPassant[1]):  # Implementierung der Regel 'Schlagen en passant' hier falsch, falls diese eine Anwendung finden würde
                        if (abs(index) == 7 or abs(index) == 9) and field[8] != enemy:
                            continue
                    elif abs(index) == 7 or abs(index) == 9:
                        sEPField = chessField[schlagenEnPassant[2] - 1]  # Feld auf dem der 'Schlagen en passant' Bauer steht einlesen
                        sEPColor = True
                        sEPHit = [(sEPField[6], sEPField[7], sEPField[1], field[6], field[7])]  # Speichern der Felder, damit diese korrekt gefärbt und falls der Bauer den anderen en passant schlägt dieser entfernt wird
                    if abs(index) == 8 and field[8] != "":  # Bauern können nur nach vorne laufen, wenn das Feld vor ihnen Frei ist
                        continue
                    if abs(index) == 16 and not ((rColumn == 2 and rFigure == "black_pawn") or (rColumn == 7 and rFigure == "white_pawn")):  # Falls der abzufragende Index 16 ist und es sich nicht um einen Bauern handelt, der noch auf seinem Startfeld steht, wird mit dem nächsten Schleifendurchlauf fortgefahren
                        continue
                    if abs(index) == 16:  # Prüft, ob beide Felder (das über welches der Bauer läuft und das auf welchem er landet) frei sind
                        rField = chessField[rFieldNumber + (index // 2) - 1]
                        if rField[8] != "" or field[8] != "":
                            continue
    
                    possibleMoves.append((field[6], field[7], field[1]))
                    
                    if field[8] == enemy or sEPColor:
                        possibleHitFieldsPawn.append((field[6], field[7], field[1]))  # Liste mit Feldern, die Rot gefärbt werden sollen: Eine Figur steht auf diesen

    return possibleMoves, possibleHitFieldsPawn  # Zurückgeben aller ermittelten möglichen Bewegungen


def possibleKnightMoves():  # Funktion, die alle möglichen Bewegungen für ein ausgewähltes Pferd zurückgibt
    
    repaintX, repaintY, rFigure, rFieldNumber, rColumn, rRow = selectedField[0]  # Entpacken des ausgewählten Feldes
    possibleMoves = []
    possibleHitFieldsKnight = []
    
    indexes = [-17, -15, -10, -6, 6, 10, 15, 17]  # Alle möglichen Pferd bewegungen, falls die entsprechenden Felder frei oder von Gegnern besetzt sind
    for index in indexes:  # Durchlaufen jedes indexes und überprüfen, ob das entsprechende Feld frei oder von einem Gegner besetzt ist
        if 64 > rFieldNumber + index - 1 > -1:  # Verhindern eines Index out of Range Errors, indem überprüft wird, ob der Anzufragende Index innerhalb der Range liegt
            field = chessField[rFieldNumber + index - 1]
            if ((rRow == 8 or rRow == 7) and field[10] < 5) or ((rRow == 1 or rRow == 2) and field[10] > 4):  # Verhindern, dass Pferde über die Seitenränder des Schachfeldes springen können
                continue
            if field[8] == "" or field[8] == enemy:
                possibleMoves.append((field[6], field[7], field[1]))
                if field[8] == enemy:
                    possibleHitFieldsKnight.append((field[6], field[7], field[1]))  # Liste mit Feldern, die Rot gefärbt werden sollen: Eine Figur steht auf diesen

    return possibleMoves, possibleHitFieldsKnight  # Zurückgeben aller möglichen Pferd bewegungen


def possibleRookMoves():  # Funktion zum Ermitteln aller möglichen Turmzüge

    repaintX, repaintY, rFigure, rFieldNumber, rColumn, rRow = selectedField[0]  # Entpacken des ausgewählten Feldes
    possibleMoves = []
    possibleHitFieldsRook = []
        
    tupleList = [(rColumn, 8, 0, -1), (rColumn, 8, 9, 1), (rRow, 1, 0, -1), (rRow, 1, 9, 1)]  # [0]: Spalte oder Zeile [1]: Felder, die im index vor / zurückgegangen werden müssen, um das nächste Feld in der Reihe oder Spalte zu ermitteln [2]: Ende, falls die Zeile oder Spalte vor Ende überprüft wird bricht die Schleife nach dieser ab [3]: zum Negieren der Laufrichtung und des Indexes
    for t in tupleList:
        line, number, end, step = t  # Entpacken der tuple aus tupleList
        m = 0  # wird mit dem Index multipliziert pro Durchlauf, damit immer das nächste Feld in die entsprechende Richtung abgefragt wird
        for i in range(line + step, end, step):
            m += 1
            index = number * m * step  # Ermitteln des Indexes, der abgefragt werden soll
            field = chessField[rFieldNumber + index - 1]
            if field[8] == "" or field[8] == enemy:
                possibleMoves.append((field[6], field[7], field[1]))
            if field[8] != "":  # Schleifenabbruch bei Gegner oder bei eigner Figur | Bei Gegner wird dieser zuvor noch ermittelt und in die möglichen Züge aufgenommen
                possibleHitFieldsRook.append((field[6], field[7], field[1]))  # Liste mit Feldern, die Rot gefärbt werden sollen: Eine Figur steht auf diesen
                break
    
    return possibleMoves, possibleHitFieldsRook  # Zurückgeben aller möglichen Bewegungen für den ausgewählten Turm


def possibleBishopMoves():  # Funktion zum Ermitteln aller möglichen Läufer bewegungen

    repaintX, repaintY, rFigure, rFieldNumber, rColumn, rRow = selectedField[0]  # Entpacken des ausgewählten Feldes
    possibleMoves = []
    possibleHitFieldsBishop = []
    
    tupleList = [(-9, 0, -1, 1), (-7, 0, -1, 2), (7, 9, 1, 3), (9, 9, 1, 4)]  # [0]: Feldindex, auf das sich bewegt werden soll, [1]: Reihenende, [2]: Schritt, [3]: Runde (Nummer des Tuples)
    for t in tupleList:
        line = 0 + rColumn
        number, end, step, runde = t  # Entpacken des aktuellen Tuples aus tupleList
        m = 0  # wird mit dem Index multipliziert pro Durchlauf, damit immer das nächste Feld in die entsprechende Richtung abgefragt wird
        for i in range(line + step, end, step):
            m += 1
            index = number * m  # Ermitteln des Indexes, der abgefragt werden soll
            if 64 > rFieldNumber + index - 1 > -1:  # Falls der Index außerhalb des Schachfeldes liegen würde, wird hier abgebrochen, damit ein Error verhindert wird
                field = chessField[rFieldNumber + index - 1]
                if (field[10] == 1 and runde % 2 == 0.0) or (field[10] == 8 and runde % 2 != 0.0):  # Falls das ermittelte Feld den entsprechenden Wert hat und der Läufer sich entgegen der Richtung bewegt, also über den Rand gelaufen ist, bricht die Schleife ab, und die Bewegung über den Rand wird nicht mehr erfasst
                    break 
                if field[8] == "" or field[8] == enemy:
                    possibleMoves.append((field[6], field[7], field[1]))
                if field[8] != "":
                    possibleHitFieldsBishop.append((field[6], field[7], field[1]))  # Liste mit Feldern, die Rot gefärbt werden sollen: Eine Figur steht auf diesen
                    break
    
    return possibleMoves, possibleHitFieldsBishop  # Zurückgeben aller ermittelten möglichen Läufer bewegungen
        
        
# Bedient sich an der Läufer- und Turmfunktion, da sich die Dame wie eine Kombination aus beiden bewegt
def possibleQueenMoves():  # Funktion zum Ermitteln aller möglichen Bewegungen für die Dame
    rook, hitFieldsRook = possibleRookMoves()
    bishop, hitFieldsBishop = possibleBishopMoves()
    
    possibleMoves = rook + bishop  # Zusammen führen der möglichen Felder aus beiden Klassen, da sich nicht Turm oder Läufer, sondern Turm und Läufer ist
    possibleHitFieldsQueen = hitFieldsRook + hitFieldsBishop
    
    return possibleMoves, possibleHitFieldsQueen  # Zurückgeben aller möglichen Zugfelder

            
def possibleKingMoves():  # Funktion zum Ermitteln aller möglichen Bewegungen für den König
    global rochadeFigurePlace
    
    repaintX, repaintY, rFigure, rFieldNumber, rColumn, rRow = selectedField[0]  # Entpacken des ausgewählten Feldes
    possibleMoves = []
        
    indexes = [-9, -8, -7, -1, 1, 7, 8, 9]  # Alle möglichen Indexe, um die sich der König bewegen kann (rochieren hierbei ausgeschlossen folgt weiter unten in der Funktion)
    for index in indexes:
        if 64 > rFieldNumber + index - 1 > -1:  # Falls der Index außerhalb des Schachfeldes liegen würde, wird hier abgebrochen, damit ein Error verhindert wird
            field = chessField[rFieldNumber + index - 1]
            if (field[10] == 1 and rRow == 8) or (field[10] == 8 and rRow == 1):  # Falls der König vor der Bewegung auf der anderen Seite des Schachfeldes war, wird hier in den nächsten Durchlauf gesprungen und der Wert nicht mehr zu den möglichen Zügen hinzugefügt
                continue
            if field[8] == "" or field[8] == enemy:
                possibleMoves.append((field[6], field[7], field[1]))
                
            if field[8] == enemy:
                possibleHitFields.append((field[6], field[7], field[1]))  # Liste mit Feldern, die Rot gefärbt werden sollen: Eine Figur steht auf diesen
            
    kingColor = rFigure.rstrip("king").rstrip("_")  # Festschreiben der Farbe des Königs in einer Variablen
    oddNumbers = [-2, -1, 1, -4]  # [0]: Bewegung des Königs bei einer Rochade [1]: Bewegung des Turms bei einer Rochade [2]: ID des Turms [3]: Index, bei dem die Überprüfung nach leeren Feldern aufhört
    evenNumbers = [2, 1, 2, 3]   # [0]: Bewegung des Königs bei einer Rochade [1]: Bewegung des Turms bei einer Rochade [2]: ID des Turms [3]: Index, bei dem die Überprüfung nach leeren Feldern aufhört
    odd = [-1, -2, -3, -4]  # Indexe große Rochade
    even = [1, 2, 3]  # Indexe kleine Rochade

    if rochadeAllowed:
        for i in [(0, "white"), (3, "black")]:  # [0]: Index in rochadeMoved zum Überprüfen, ob sich der König bereits bewegt hat [1]: Farbe des zu überprüfenden Königs
            if (not rochadeMoved[i[0]]) and rFigure.startswith(i[1]):  # Falls sich der König noch nicht bewegt hat und die Farbe des Königs mit der Farbe des ausgewählten Königs übereinstimmt
                r = 0
                for j in [1, 2, 4, 5]:  # Indexe in rochadeMoved zum Überprüfen, ob sich die Türme, mit denen rochiert werden soll bereits bewegt haben
                    r += 1
                    if r % 2 == 0.0:
                        evenOddIndex = [] + evenNumbers
                        evenOrOdd = [] + even
                    else:
                        evenOddIndex = [] + oddNumbers
                        evenOrOdd = [] + odd

                    if (i[0] == 0 and (not rochadeMoved[j]) and j < 3) or (i[0] == 3 and (not rochadeMoved[j]) and j > 3):  # Falls sich der zu überprüfende Turm sich noch nicht bewegt hat
                        for index in evenOrOdd:
                            if 64 > rFieldNumber + index - 1 > -1:  # Falls der Index außerhalb des Schachfeldes liegen würde, wird hier abgebrochen, damit ein Error verhindert wird
                                field = chessField[rFieldNumber + index - 1]
                                if index == evenOddIndex[3] and field[2] == kingColor + "_" + str(evenOddIndex[2]) + "_rook":  # Falls der letzte Index für die Rochade erreicht wurde und auf dem letzten Feld der Turm steht, der zu Beginn des Spiels auf dem entsprechenden Feld stand
                                    kingField = chessField[rFieldNumber + evenOddIndex[0] - 1]  # Feld auf das der König bei der entsprechenden Rochade zieht
                                    rookField = chessField[rFieldNumber + evenOddIndex[1] - 1]  # Feld auf das der Turm bei der entsprechenden Rochade zieht
                                    if kingColor == "white":
                                        king = Skin.whiteKing
                                        rook = Skin.whiteRook
                                    else:
                                        king = Skin.blackKing
                                        rook = Skin.blackRook
                                    rochadeFigurePlace.append((field[1], kingField[1], kingColor + "_king", king, kingColor, (kingField[6], kingField[7]), rookField[1], kingColor + "_" + str(evenOddIndex[2]) + "_rook", rook, kingColor, (rookField[6], rookField[7])))
                                    possibleMoves.append((field[6], field[7], field[1]))
                                if field[8] != "":
                                    break

    return possibleMoves, possibleHitFields  # Zurückgeben aller möglichen Bewegungen
                                        
                                                                                                    
def figureMove(sourceIndex, moveToIndex, automatic=False, illegalMoveTest=False):  # Funktion, die Figuren bewegt / die Schachfeldliste an den bestimmten Stellen überschreibt
    global schlagenEnPassant
    global sEPHit
    global chessField
    global moves
    global rochadeMoved
    global rochadeFigurePlace
    global moveList

    prefix = ""
    action = "-"
    addition = ""
    promote = ""
    enPas = ""

    rochadeNotation = ""

    skipSound = False
    rochade = False
    
    lastChessField = [] + chessField  # Für den Durchlauf eine Kopie des Feldes erstellen, um bei einem illegalen Zug alle Figuren leicht zurücksetzen zu können
    lastRochadeMoved = [] + rochadeMoved  # Für den Durchlauf eine Kopie der Liste erstellen, um bei einem illegalen Zug die Liste mit den bewegten Figuren zurücksetzen zu können
    
    sourceField = chessField[sourceIndex]  # s = source / Ausgangsfeld | Das Feld von dem aus sich die Figur bewegt
    moveToField = chessField[moveToIndex]  # m = moveto / Endfeld | Das Feld auf das die Figur bewegt werden soll
    
    sFieldKey, sFieldNumber, sFigure, sFigureTexture, sLeftX, sYAbove, sCenterX, sCenterY, sFigureColor, sColumn, sRow = sourceField  # Entpacken des source_fields
    mFieldKey, mFieldNumber, mFigure, mFigureTexture, mLeftX, mYAbove, mCenterX, mCenterY, mFigureColor, mColumn, mRow = moveToField  # Entpacken des move_to_fields
    
    if not automatic and not illegalMoveTest:  # Die folgenden 3 Methoden dürfen nur bei einem Zug und nicht bei einer Zugüberprüfung des Computers aufgerufen werden

        # Zusammensetzen der Zug-Notation
        if sFigure.endswith("rook"):
            prefix = "T"
        elif sFigure.endswith("knight"):
            prefix = "S"
        elif sFigure.endswith("bishop"):
            prefix = "L"
        elif sFigure.endswith("queen"):
            prefix = "D"
        elif sFigure.endswith("king"):
            prefix = "K"

        if mFigure != "":
            action = "x"

        if onlineMode:
            if not automatic and not illegalMoveTest:
                if sFigure.endswith("pawn"):
                    if playerEnemy != activePlayer:
                        dataToSend = pickle.dumps(sEPHit)
                        clientSocket.send(dataToSend)
                    data = clientSocket.recv(1024)
                    sEPHit = list(pickle.loads(data))

        if len(sEPHit) != 0 and sFigure.endswith("pawn"):  # Falls im letzten Zug sich ein Bauer um 2 Felder nach vorne bewegt hat und somit von einem gegnerischen Bauern, der nun neben ihm steht geschlagen werden könnte
            fX, fY, fFieldNumber, fTargetFieldX, fTargetFieldY = sEPHit[0]  # Entpacken des 'schlagen en passant' hit
            if fTargetFieldX == mCenterX and fTargetFieldY == mCenterY:  # Falls das 'schlagen en passant' Feld mit den Koordinaten des Feldes, auf das sich die Figur gerade bewegt übereinstimmen
                hittetPawn = chessField[fFieldNumber - 1]
                hPFieldKey, hPFieldNumber, hPFigure, hPFigureTexture, hPLleftX, hPYAbove, hPCenterX, hPCenterY, hPFigureColor, hPColumn, hPRow = hittetPawn  # Entpacken des Feldes mit dem geschlagenen Bauern, da dieser sich nicht auf dem move_to Feld befindet, jedoch trotzdem entfernt werden muss
                chessField[fFieldNumber - 1] = (hPFieldKey, hPFieldNumber, "", "", hPLleftX, hPYAbove, hPCenterX, hPCenterY, "", hPColumn, hPRow)  # Verpacken des entsprechenden Feldes / überschreiben

                pygame.mixer.music.load(Skin.hitEnPassanteSound)
                pygame.mixer.music.play(0, 0.0)

                enPas = "e.p."
                action = "x"

                skipSound = True

            sEPHit = []
        
        if sFigure.endswith("pawn"):  # Abfrage, ob sich ein Bauer in diesem Zug um 16 Felder nach vorne bewegt, um diesen dann in die 'Schlagen en passant' Möglichkeit einzuschreiben
            if sFieldNumber - 16 == mFieldNumber:
                schlagenEnPassant = [moves + 1, sFieldNumber - 8, mFieldNumber]
            elif sFieldNumber + 16 == mFieldNumber:
                schlagenEnPassant = [moves + 1, sFieldNumber + 8, mFieldNumber]
        
            if (mColumn == 1 and sFigure.startswith("white")) or (mColumn == 8 and sFigure.startswith("black")):  # Falls ein Bauer sich auf die gegnerische letzte Linie begibt, tauscht er seinen Bauern gegen einen Turm, Pferd, Läufer oder eine Dame ein
                sFigure = ""
                while sFigure == "":
                    if onlineMode:
                        if playerEnemy != activePlayer:
                            try:
                                eFigure = int(informationDialog("Bauern ersetzen durch: ", "", "Bauern ersetzen durch '1' Turm, '2' Pferd, '3' Läufer, '4' Dame: "))
                            except TypeError as e:
                                eFigure = 0
                            clientSocket.send(str(eFigure).encode())
                        try:
                            eFigure = int(clientSocket.recv(1024).decode())
                        except TypeError as e:
                            eFigure = 0
                    
                    else:
                        try:
                            eFigure = int(informationDialog("Bauern ersetzen durch: ", "", "Bauern ersetzen durch '1' Turm, '2' Pferd, '3' Läufer, '4' Dame: "))
                        except TypeError as e:
                            eFigure = 0
                    
                    if eFigure == 1:
                        eFigure = "_rook"
                        promote = "T"
                        if sFigureColor == "white":
                            rFigure = Skin.whiteRook
                        else:
                            rFigure = Skin.blackRook
                    elif eFigure == 2:
                        eFigure = "_knight"
                        promote = "S"
                        if sFigureColor == "white":
                            rFigure = Skin.whiteKnight
                        else:
                            rFigure = Skin.blackKnight
                    elif eFigure == 3:
                        eFigure = "_bishop"
                        promote = "L"
                        if sFigureColor == "white":
                            rFigure = Skin.whiteBishop
                        else:
                            rFigure = Skin.blackBishop
                    elif eFigure == 4:
                        eFigure = "_queen"
                        promote = "D"
                        if sFigureColor == "white":
                            rFigure = Skin.whiteQueen
                        else:
                            rFigure = Skin.blackQueen
                    else:
                        continue  # Hier ein else mit contínue, um den restlichen Schleifendurchlauf, also die 'sure' Zuweisung mit der Frage zu überspringen, da eine Zahl eingegeben wurde, der keine Figur zugeordnet ist

                    sFigure = sFigureColor + eFigure
                    sFigureTexture = rFigure

                    pygame.mixer.music.load(Skin.promoteSound)
                    pygame.mixer.music.play()

                    skipSound = True

        if sFigure.endswith("king"):  # Deaktivieren der Rochade-Möglichkeit für die entsprechende Figur, falls sich diese bewegt
            if sFigure.startswith("white"):
                rochadeMoved[0] = True
            if sFigure.startswith("black"):
                rochadeMoved[3] = True
        if sFigure.endswith("rook"):
            if sFigure.startswith("white"):
                if sFigure == "white_1_rook":
                    rochadeMoved[1] = True
                if sFigure == "white_2_rook":
                    rochadeMoved[2] = True
            if sFigure.startswith("black"):
                if sFigure == "black_1_rook":
                    rochadeMoved[4] = True
                if sFigure == "black_2_rook":
                    rochadeMoved[5] = True 
                    
        if onlineMode:
            if not automatic and not illegalMoveTest:
                if sFigure.endswith("king"):
                    if playerEnemy != activePlayer:
                        dataToSend = pickle.dumps(rochadeFigurePlace)
                        clientSocket.send(dataToSend)
                    data = clientSocket.recv(1024)
                    rochadeFigurePlace = list(pickle.loads(data))

    if not automatic and not illegalMoveTest:
        if mFigure != "" and not skipSound:
            pygame.mixer.music.load(Skin.hitSound)
            pygame.mixer.music.play(0, 0.0)
    
    mFigure = "" + sFigure
    mFigureTexture = "" + sFigureTexture
    mFigureColor = "" + sFigureColor
    
    sFigure = ""
    sFigureTexture = ""
    sFigureColor = ""
    
    if len(rochadeFigurePlace) != 0:  # Falls eine Rochade durchgeführt werden könnte
        for t in rochadeFigurePlace:
            clickedField, kFieldNumber, k, kTexture, kColor, kT, rookFieldNumber, rook, rookTexture, rookColor, rookT = t
            if clickedField - 1 == moveToIndex:  # Prüft für jede Rochade, die in diesem Zug hätte durchgeführt werden können, ob sie durchgeführt wurde
                rochade = True
                
                kingField = chessField[kFieldNumber - 1]  # weder source noch moveto Feld, da sich König und Turm bei der Rochade auf andere Felder bewegen, weshalb hier diese Felder entpackt werden müssen
                rookField = chessField[rookFieldNumber - 1]  # weder source noch moveto Feld, da sich König und Turm bei der Rochade auf andere Felder bewegen, weshalb hier diese Felder entpackt werden müssen
                
                eKFieldKey, eKFieldNumber, eKFigure, eKFigureTexture, eKLeftX, eKYAbove, eKCenterX, eKCenterY, eKFigureColor, eKColumn, eKRow = kingField
                eRookFieldKey, eRookFieldNumber, eRookFigure, eRookFigureTexture, eRookLeftX, eRookYAbove, eRookCenterX, eRookCenterY, eRookFigureColor, eRookColumn, eRookRow = rookField
                
                # Einpacken der überschriebenen Felder
                chessField[kFieldNumber - 1] = (eKFieldKey, eKFieldNumber, k, kTexture, eKLeftX, eKYAbove, eKCenterX, eKCenterY, kColor, eKColumn, eKRow)
                chessField[rookFieldNumber - 1] = (eRookFieldKey, eRookFieldNumber, rook, rookTexture, eRookLeftX, eRookYAbove, eRookCenterX, eRookCenterY, rookColor, eRookColumn, eRookRow)
            
                rochadeFigurePlace = []    
                # Moveto leeren, da sich Turm und König ja bereits auf andere Felder bewegt haben 
                mFigure = ""
                mFigureTexture = ""
                mFigureColor = ""

                if abs(mFieldNumber - eRookFieldNumber) == 2:
                    rochadeNotation = "0_0"
                elif abs(mFieldNumber - eRookFieldNumber) == 3:
                    rochadeNotation = "0_0_0"
    
    chessField[sourceIndex] = (sFieldKey, sFieldNumber, sFigure, sFigureTexture, sLeftX, sYAbove, sCenterX, sCenterY, sFigureColor, sColumn, sRow)
    chessField[moveToIndex] = (mFieldKey, mFieldNumber, mFigure, mFigureTexture, mLeftX, mYAbove, mCenterX, mCenterY, mFigureColor, mColumn, mRow)
    
    kingGetter()  # Ermitteln der neuen Königsfelder
            
    if illegalMoveTest:
        check = checkCheck()  # Überprüfung auf einen illegalen Zug
        kingGetter() 
        chessField = [] + lastChessField  # Feld mit der erstellten Kopie überschreiben
        rochadeMoved = [] + lastRochadeMoved  # Liste mit den bewegten Rochade-Figuren auf Stand vor dem illegalen Zug zurücksetzen
        return check

    if not automatic and not illegalMoveTest:  # Bei automatischem Programmdurchlauf würden im folgendem weitere automatische Programmdurchläufe entstehen
        playerChange()

        checkTest = checkCheck()
        if checkTest:
            addition = "+"
            checkMateTest = checkCheckMate()
            if checkMateTest:
                addition = "#"
        if not rochade:
            notation = prefix + sFieldKey + action + mFieldKey + addition + promote + enPas
        else:
            notation = rochadeNotation

        playerChange()

        moves += 1
        moveList[moves] = str(moves) + ": " + notation
        
        if not onlineMode:
            playerChange()  # Spielerwechsel mit Spieler text, enemy und Zug counter
    
    if automatic:
        return lastChessField, lastRochadeMoved  # Beim Automatischen durchlaufen die Ursprungsfelder zurückgeben, damit diese nach der automatischen Figur bewegung sich nicht ändern


def decolor():  # Funktion zum Entfärben der gefärbten Felder
    global lastPossibleFields
    global rochadeFigurePlace
    global possibleHitFields
    global selectedField

    lastPossibleFields = []  # Leeren der Listen und danach repainten wichtig, um Feld neu zu "malen"
    rochadeFigurePlace = []
    possibleHitFields = []
    selectedField = []    
    
    repaint()  # Repainten, um alle Färbungen zu entfernen


def checkCheck():  # Funktion zum Überprüfen, ob der König im Schach steht
    global selectedField
    
    Check = False
    runde = 0
    for largeTuple in chessField:  # Für jedes Feld prüfen, ob eine gegnerische Figur auf diesem steht
        selectedField = [(largeTuple[6], largeTuple[7], largeTuple[2], largeTuple[1], largeTuple[9], largeTuple[10]), runde]  # Neue Werte des Feldes zuweisen, wichtig da sonst die Überprüfung der Möglichen bewegungen der Figuren nicht funktioniert
        if largeTuple[8] == enemy:
            playerChange()  # Wechseln des Gegners wichtig, da für gegnerische Figuren ermittelt werden soll, ob diese den eigenen König schlagen könnten
            lastPossibleFieldsCheck, possibleHitFieldsCheck = checkFigureType(largeTuple[2])  # Funktionsaufruf mit der Figur, die auf dem aktuell überprüften Feld steht
            playerChange()  # Wichtig, da die Schlagmöglichkeit der gegnerischen Figuren gegen den EIGENEN König getestet werden soll
            for fieldTuple in lastPossibleFieldsCheck:  # Überprüfen für jedes mögliche Feld, das zuvor ermittelt wurde, ob die Figur den gegnerischen König schlagen könnte
                for king in kingFields:
                    if king[2] == activePlayer and (fieldTuple[0] == king[0] and fieldTuple[1] == king[1]):
                        Check = True  # Schach-Situation durch eine Figur erkannt
        runde += 1
    return Check  # Zurückgeben von 'False' oder 'True', je nachdem, ob ein König im Schach steht oder nicht

         
def checkCheckMate():  # Funktion zum Überprüfen, ob ein Spieler Schachmatt ist. (Wird nur aufgerufen, falls ein König im Schach steht)
    global selectedField
    global chessField
    global rochadeMoved
    
    check = True
    runde = 0
    for tTuple in chessField:
        selectedField = [(tTuple[6], tTuple[7], tTuple[2], tTuple[1], tTuple[9], tTuple[10]), runde]  # Neue Werte des Feldes zuweisen, wichtig da sonst die Überprüfung der Möglichen bewegungen der Figuren nicht funktioniert
        if tTuple[8] == activePlayer:
            lastPossibleFieldsCheckMate, possibleHitFieldsCheckMate = checkFigureType(tTuple[2])
            for possibleField in lastPossibleFieldsCheckMate:
                lRunde = 0
                for largeTuple in chessField:
                    if possibleField[0] == largeTuple[6] and possibleField[1] == largeTuple[7]:
                        lSelectedField = [(largeTuple[6], largeTuple[7], largeTuple[2], largeTuple[1], largeTuple[9], largeTuple[10]), runde]  # Neue Werte des Feldes zuweisen, wichtig da sonst die Überprüfung der Möglichen bewegungen der Figuren nicht funktioniert
                        lastChessField, lastRochadeMoved = figureMove(lSelectedField[1], lRunde, True)
                        check = checkCheck()  # Prüfen, ob König noch im Schach steht. Wenn nicht, wird die Funktion abgebrochen
                        chessField = [] + lastChessField  # Zurücksetzen der Figuren auf ihre Ursprungsfelder
                        rochadeMoved = [] + lastRochadeMoved
                        
                        kingGetter()  # Ermitteln, auf welchen Feldern die Könige stehen, da diese möglicherweise bewegt wurden
                        
                    if not check:
                        return check  # Bricht Funktion ab, da es eine Möglichkeit gibt aus dem "Schach" herauszukommen
                    lRunde += 1  
        runde += 1                   
    return check  # Zurückgeben von 'False' oder 'True', je nachdem, ob ein König im Schachmatt ist oder nicht

                          
def checkStalemate():  # Funktion zum Überprüfen auf ein Unentschieden
    stalemate = checkCheckMate()  # Prüfen, ob sich eine Figur bewegen kann, ohne dass der König nach der Bewegung im Schach steht
    
    if not stalemate:  # Falls dies möglich ist, wird geguckt, ob es nur noch 2 Könige gibt, wodurch ebenfalls ein Unentschieden entsteht
        for field in chessField:
            if not (field[2].endswith("king") or field[2] == ""):  # Falls es ein Feld gibt, auf dem etwas anderes als nichts oder ein König steht, wird die Schleife abgebrochen
                break  # Hier sehr nützlich, da nur durch dieses Break das Else-Statement nicht ausgelöst wird
        else:  # Fall das Break nicht einmal aufgerufen wurde, gibt es ein Unentschieden
            stalemate = True
                
    return stalemate  # Zurückgeben von False oder True, je nachdem, ob das Spiel unentschieden ist oder nicht


def playerChange():  # Funktion zum Wechseln der Spieler
    global activePlayer
    global activePlayerText
    global enemy
    
    if activePlayer == "white":
        activePlayer = "black"
        activePlayerText = "Schwarz"
        enemy = "white"
    else:
        activePlayer = "white"
        activePlayerText = "Weiss"
        enemy = "black"


def kingGetter():  # Funktion zum Ermitteln der Positionen der Könige
    global kingFields
    
    for t in chessField:  # Neu ermitteln des König feldes, falls dieses durch das Programm verändert wurde
        if t[2].endswith("king"):
            if t[2].startswith("black"):
                kingFields[0] = t[6], t[7], "black"
            elif t[2].startswith("white"):
                kingFields[1] = t[6], t[7], "white"
                                                                                    
        
def checkFigureType(figure):  # Funktion zum Überprüfen, für welche Figur die nächstmöglichen Felder ausgegeben werden soll
    lastPossibleFields1 = None
    possibleHitFields1 = None

    if figure.endswith("pawn"):
        lastPossibleFields1, possibleHitFields1 = possiblePawnMoves()
    if figure.endswith("knight"):
        lastPossibleFields1, possibleHitFields1 = possibleKnightMoves()
    if figure.endswith("rook"):
        lastPossibleFields1, possibleHitFields1 = possibleRookMoves()
    if figure.endswith("bishop"):
        lastPossibleFields1, possibleHitFields1 = possibleBishopMoves()
    if figure.endswith("queen"):
        lastPossibleFields1, possibleHitFields1 = possibleQueenMoves()
    if figure.endswith("king"):
        lastPossibleFields1, possibleHitFields1 = possibleKingMoves()
    
    return lastPossibleFields1, possibleHitFields1  # Zurückgeben der möglichen ermittelten Felder


def figureSelect(posX, posY):  # Funktion die auf Aufruf des obigen Maus-callbacks aufgerufen und ausgeführt wird | Das Maus-callback übergibt die angeklickten Koordinaten, mit welchen im Folgenden die angeklickte Position überprüft wird
    global rochadeAllowed
    global selectedField
    global lastPossibleFields
    global inputAllowed
    global possibleHitFields
    global rochadeFigurePlace
    
    if not onlineMode:
        checkMate = False
        stalemate = False
    index = 0
    if inputAllowed and (not onlineMode or playerEnemy != activePlayer):  # Solange True, bis ein König fällt
        for largeTuple in chessField:  # Durchgehen jedes Feldes bis ein Feld mit den angeklickten Koordinaten übereinstimmt, auf diesem werden dann die weiteren Schritte ausgeführt
            moved = False
            fieldKey, fieldNumber, figure, figureTexture, leftX, yAbove, centerX, centerY, figureColor, column, row = largeTuple  # Entpacken des Schachfeld Tupels
            if (posX >= leftX and posY >= yAbove) and (posX <= (leftX + 100 * mScreenW) and posY <= (yAbove + 100 * mScreenH)):  # Prüft ob das oben entpackte Schachfeld zu den angeklickten Koordinaten passt
                kingGetter()  # Wichtig, da es sonst zu illegalen Zugmöglichkeiten kommen kann, da die Könige noch auf anderen Feldern registriert sind
                if len(lastPossibleFields) != 0:  # Falls bereits eine Figur ausgewählt wurde und Bewegungsmöglichkeiten für die Figur grün gefärbt wurden wir als erstes geprüft, ob das angeklickte Feld eines derer ist, auf die sich die Figur bewegen kann
                    for possibleField in lastPossibleFields: 
                        if centerX == possibleField[0] and centerY == possibleField[1]:  # Falls die Center mit den Centern des aktuellen Feldes übereinstimmen
                            moved = True
                            if onlineMode:
                                dataToSend = pickle.dumps((selectedField[1], index))
                                clientSocket.send(dataToSend)  # Senden der Bewegung an den Server, damit beide Clients ihre Spielfelder updaten
                                selectedField = []
                                break
                            else:
                                figureMove(selectedField[1], index)  # Übergibt an die Move-Funktion das ausgewählte Feld, sowie das Feld, auf welches sich die Figur bewegen soll
                                decolor()  # Entfärben aller Felder sowie leeren der dazugehörigen Listen
                        
                                check = checkCheck()  # Überprüfen, ob der König des aktuellen Spielers im Schach steht
                                if check:  # Aufrufen der Schachmatt-funktion nur, wenn ein König im Schach steht
                                    rochadeAllowed = False
                                    checkMate = checkCheckMate()
                                if not check:
                                    rochadeAllowed = True
                                    stalemate = checkStalemate()
                                
                                if checkMate:
                                    playerChange()

                                    pygame.mixer.music.load(Skin.winSound)
                                    pygame.mixer.music.play(0, 0.0)

                                    inputAllowed = False  # Weiteren Input nach Spielende verhindern
                                    pygame.display.set_caption("SPIELENDE   |   " + activePlayerText + " hat das Spiel gewonnen")  # Titel am Spielende aktualisieren
                                    toast(activePlayerText + " hat das Spiel gewonnen!")
                                    
                                if not checkMate and check:
                                    pygame.mixer.music.load(Skin.checkSound)
                                    pygame.mixer.music.play(0, 0.0)
                                    toast(activePlayerText + ", du stehst im Schach")
                                    
                                if stalemate:
                                    pygame.mixer.music.load(Skin.pattSound)
                                    pygame.mixer.music.play(0, 0.0)
                                    inputAllowed = False  # Weiteren Input nach Spielende verhindern
                                    pygame.display.set_caption("SPIELENDE   |   Unentschieden")  # Titel am Spielende aktualisieren
                                    toast("Unentschieden!")
                                    
                                selectedField = []
                                break
                if moved:
                    break  # Keine andere Möglichkeit gefunden | Schleife muss im if Fall sofort abgebrochen werden, da es sonst zu verheerenden Fehlern kommen kann
                if figure != "" and figureColor == activePlayer:  # Falls das angeklickte Feld nicht leer und die Figurenfarbe mit dem aktiven Spieler übereinstimmt
                    decolor()
                    selectedField.append((centerX, centerY, figure, fieldNumber, column, row))  # Nach leeren und entfärben wird hier die neu ausgewählte Figur aufgenommen
                    selectedField.append(index)  # Speichern des Indexes des ausgewählten Feldes | Wichtig für die move Funktion
                    if not onlineMode:
                        if activePlayer == "black" and turnChessField:
                            fX = -centerX + screenW
                            fY = -centerY + screenH
                        else:
                            fX = centerX
                            fY = centerY
                    else:
                        if playerEnemy == "white":
                            fX = -centerX + screenW
                            fY = -centerY + screenH
                        else:
                            fX = centerX
                            fY = centerY

                    pygame.draw.rect(pygameWindow, (173, 216, 230), (fX - 50 * mScreenW, fY - 50 * mScreenH, 100 * mScreenW, 100 * mScreenH))
                    figureRepaint()

                    lastPossibleFields, possibleHitFields = checkFigureType(figure)  # Funktionsaufrufe je nach ausgewählter Figur
                    newPossibleMoves = []
                    for largeT in lastPossibleFields:  # Für jedes possible Field wird geguckt, ob der Zug legal wäre, wenn nicht, wird das Feld nicht zur neuen Liste hinzugefügt, die die Alte dann ersetzt
                        selectedCopy = [] + selectedField  # Copy von selectedField, da dieses sich ändert und sonst nichts mehr funktioniert
                        figureHitCopy = [] + possibleHitFields
                        rochadeCopy = [] + rochadeFigurePlace
                        
                        check = figureMove(selectedField[1], largeT[2] - 1, False, True)  # Hier wird die legalität des möglichen Zuges überprüft
                        
                        selectedField = [] + selectedCopy  # selectedField mit der erzeugten Kopie überschreiben
                        possibleHitFields = [] + figureHitCopy
                        rochadeFigurePlace = [] + rochadeCopy
                        
                        if not check:  # Falls der mögliche Zug nicht illegal ist, wird er zu den neuen möglichen Zügen hinzugefügt
                            newPossibleMoves.append(largeT)
                    lastPossibleFields = [] + newPossibleMoves  # Überschreiben der Liste mit den möglichen Feldern, mit den möglichen legalen Feldern
                    
                    newHitFields = []
                    for f in possibleHitFields:  # Überprüfen, ob eine Schlagmöglichkeit soeben als illegal erkannt wurde, falls dies der Fall ist MUSS dieses Feld aus figure_hit_field entfernt sein
                        for i in lastPossibleFields:
                            if f == i:  # Falls das Hit-field noch in den möglichen ist, wird es der neuen Liste hinzugefügt
                                newHitFields.append(f)
                    possibleHitFields = [] + newHitFields  # Überschreiben der alten möglichen Schläge mit den möglichen legalen Schlägen
                    
                    newRochadeFields = []
                    for f in rochadeFigurePlace:
                        for i in lastPossibleFields:
                            if f[0] == i[2]:  # Wenn die Feldnummern übereinstimmen
                                newRochadeFields.append(f)
                    rochadeFigurePlace = [] + newRochadeFields

                    for f in lastPossibleFields:  # Färben der möglichen Züge
                        fX, fY, fNumber = f
                        if not onlineMode:
                            if activePlayer == "black" and turnChessField:
                                fX = -fX + screenW
                                fY = -fY + screenH
                        else:
                            if playerEnemy == "white":
                                fX = -fX + screenW
                                fY = -fY + screenH

                        pygame.draw.rect(pygameWindow, (63, 255, 0), (fX - 50 * mScreenW, fY - 50 * mScreenH, 100 * mScreenW, 100 * mScreenH))

                    for f in rochadeFigurePlace:  # Färben der Felder für König und Turm bei einer Rochade
                        for t in f:
                            if type(t) is tuple:
                                tX, tY, = t
                                if not onlineMode:
                                    if activePlayer == "black" and turnChessField:
                                        tX = -tX + screenW
                                        tY = -tY + screenH
                                else:
                                    if playerEnemy == "white":
                                        tX = -tX + screenW
                                        tY = -tY + screenH

                                pygame.draw.rect(pygameWindow, (192, 0, 255), (tX - 50 * mScreenW, tY - 50 * mScreenH, 100 * mScreenW, 100 * mScreenH))

                    for f in possibleHitFields:
                        fX, fY, fNumber = f
                        if not onlineMode:
                            if activePlayer == "black" and turnChessField:
                                fX = -fX + screenW
                                fY = -fY + screenH
                        else:
                            if playerEnemy == "white":
                                fX = -fX + screenW
                                fY = -fY + screenH

                        pygame.draw.rect(pygameWindow, (250, 0, 0), (fX - 50 * mScreenW, fY - 50 * mScreenH, 100 * mScreenW, 100 * mScreenH))

                    figureRepaint()

            index += 1  # Nach einem Schleifendurchlauf wird der Index um 1 erhöht


def startGame(bot=False, online=False):
    global pygameWindow
    global showPygameWindow
    global gameStart
    global gameExit
    global onlineMode
    global chessField
    global turnChessField
    
    onlineMode = online
    gameStart = time.time()  # Zeit des Spielstarts speichern
    
    if not onlineMode:
        showPygameWindow = True
    else:
        startClient()

    if onlineMode:
        clientSocket.send(Values.chosenSkinPacket.encode())
        time.sleep(1)

    resetChessField()
    pygame.init()

    pygameWindow = pygame.display.set_mode((1000 * mScreenW, 1000 * mScreenH))
    icon = pygame.image.load(Skin.icon)
    pygame.display.set_icon(icon)

    if not onlineMode:
        pygame.display.set_caption("Python-Schach")
    else:
        pygame.display.set_caption("Python-Online-Schach auf jythonchess.de")

    repaint()  # Erstes Zeichnen des Spielfeldes

    while showPygameWindow:  # Spiel-loop findet hier statt
        if activePlayer == "white" or not bot:
            for event in pygame.event.get():  # Event-Abfrage
                if event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = event.pos
                    if event.pos <= (100, 100):
                        if not turnChessField:
                            turnChessField = True
                        else:
                            turnChessField = False
                        repaint()
                    if (activePlayer == "black" and turnChessField) or playerEnemy == "white":
                        x = -x + screenW
                        y = -y + screenH
                    figureSelect(x, y)  # Aufrufen der select-Funktion mit den von dem Event gegebenen Positionswerten
                if event.type == pygame.QUIT:
                    if not onlineMode:
                        showPygameWindow = False
                    else:
                        gameExit = True
                        clientSocket.send("Mitspieler left game".encode())
        else:
            BC.getMove()
    pygame.quit()
