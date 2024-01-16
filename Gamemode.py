import Skinpackets as Skin
import sys
import webbrowser
import Values
import time
import os
import socket
import pygame
import tkinter
from tkinter import ttk
import RequestGamemode as RG


def newSound():
    Skin.updateAll()

    pygame.mixer.music.stop()
    pygame.mixer.music.unload()

    pygame.mixer.music.load(Skin.lobbySound)
    pygame.mixer.music.play(-1, 0.0)

                
if __name__ == "__main__":

    fileDir = os.getcwd()  # Speichern des Verzeichnisses, in dem das Programm läuft
    files = "files/"  # Name des Ordners, indem sich die Dateien befinden
    dirLocation = os.path.join(fileDir, files)  # Anfügen des Ordnernamen an das Verzeichnis

    Values.dirLocation = dirLocation
    Skin.updateAll()

    pygame.init()

    pygame.mixer.music.load(Skin.lobbySound)
    pygame.mixer.music.play(-1, 0.0)

    chosenGamemode, screenH, screenW = RG.gamemodeDialog()

    pygame.mixer.music.stop()
    pygame.mixer.music.unload()

    Values.chosenGamemode = chosenGamemode
    Values.screenH = screenH
    Values.screenW = screenW

    def openLink(event):
        webbrowser.open("https://1drv.ms/f/s!AsiOx5207ybpgr9URqqRsS7UVUS1Yg?e=6P4kXf")

    start = time.time()
    onlineConnection = False
    while time.time() - start <= 10 and not onlineConnection and chosenGamemode == 1:
        try:  # Falls keine Verbindung mit dem Server zustande kommt: Fehler abfangen, Programm durch Sys-exit beenden mit entsprechender Nachricht
            clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            clientSocket.connect(('jythonchess.de', 8888))  # Verbinden mit dem Server, falls möglich
            clientSocket.send("versionsabfrage".encode())
            version = clientSocket.recv(1024).decode()
            clientSocket.close()
            onlineConnection = True

            if Values.version != version:
                root = tkinter.Tk()
                root.title("Veraltete Version!")

                style = ttk.Style()
                style.configure("Link.TLabel", foreground="blue", underline=True)

                label1 = ttk.Label(root, text="Veraltete Version! Lade hier die neue Version herunter: ")
                label1.pack(pady=10, padx=25)

                label2 = ttk.Label(root, text="https://1drv.ms/f/s!AsiOx5207ybpgr9URqqRsS7UVUS1Yg?e=6P4kXf", style="Link.TLabel")
                label2.pack(pady=10, padx=25)
                label2.bind("<Button-1>", openLink)

                continueButton = ttk.Button(text="Ok", command=root.destroy)
                continueButton.pack()

                root.mainloop()
                sys.exit("Veraltete Version")

            else:
                import Chess
                Chess.startGame(False, True)

        except Exception as e:
            sys.exit("Es konnte keine Verbindung zum Server hergestellt werden!")

    if chosenGamemode == 0:
        import Chess
        Chess.startGame()

    if chosenGamemode == 2:
        import Chess
        Chess.startGame(True)
