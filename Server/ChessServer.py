import Values
import socket
import threading
import random
import datetime

games = {}
version = Values.version


def handleClient(clientSocket):
    messageTime = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    try:
        decision = clientSocket.recv(1024).decode()

        if decision == "versionsabfrage":
            clientSocket.send(version.encode())
            clientSocket.close()

        elif decision == "spielen":
            openGames = ', '.join(games.keys()) or "Keine offenen Games"  # Liste der offenen Game-rooms an den Client senden
            clientSocket.send("Verfügbare Games: '{}'".format(openGames).encode())
            gameCode = clientSocket.recv(1024).decode()  # Auf Beitrittsentscheidung des Clients warten

            if gameCode not in games:  # Überprüfen, ob das Game bereits existiert oder erstellt werden muss
                games[gameCode] = [clientSocket]  # Falls das Spiel nicht existiert neues erstellen
                clientSocket.send("Game {} erstellt \nWarte auf weitere Mitglieder...".format(gameCode).encode())
                print("[" + messageTime + "]: Game {} erstellt".format(gameCode))
            else:
                if len(games[gameCode]) >= 2:  # Bestehendem Game beitreten
                    clientSocket.send("Das Game {} ist voll! Bitte erstelle ein neues Game oder joine einem anderem".format(gameCode).encode())
                else:
                    games[gameCode].append(clientSocket)
                    clientSocket.send("Du bist dem Game {} beigetreten".format(gameCode).encode())

                while len(games[gameCode]) < 2:  # Auf Beitritt des 2.ten Spielers warten
                    clientSocket.send("Warte auf weiteren Spieler...".encode())

                randomNumber = random.randint(0, 1)  # Farbzufallsgenerator, damit der Spieler, der sich als Erstes verbindet nicht zwangsweise Weiß spielt
                if randomNumber == 0:
                    member = games[gameCode]
                    member[0].send("black".encode())
                    clientSocket.send("white".encode())
                else:
                    member = games[gameCode]
                    member[0].send("white".encode())
                    clientSocket.send("black".encode())

            while True:
                data = clientSocket.recv(1024)
                if not data:
                    break
                message = data
                broadcast(message, games[gameCode])

    except Exception as e:
        print("[" + messageTime + "]: Fehler beim Umgang mit Client: {}".format(e))
    finally:  # Client aus dem Game entfernen, wenn ein Fehler vorliegt
        for code, members in games.items():
            if clientSocket in members:
                members.remove(clientSocket)
                if not members:
                    print("[" + messageTime + "]: Game", code, "geschlossen")
                    del games[code]
                break
        clientSocket.close()


def broadcast(message, members):
    for memberSocket in members:  # Sende die Nachricht an alle Mitglieder des Games
        messageTime = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        try:
            memberSocket.send(message)
        except Exception as e:
            print("[" + messageTime + "]: Fehler beim übermitteln der Nachricht: {}".format(e))


def startServer():
    messageTime = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    serverSocket.bind(('0.0.0.0', 8888))
    serverSocket.listen(787)

    print("[" + messageTime + "]: Server gestartet auf Port 8888...")

    try:
        while True:
            messageTime = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

            clientSocket, addr = serverSocket.accept()
            print("[" + messageTime + "]: Verbindung von: {}".format(addr))
            clientHandler = threading.Thread(target=handleClient, args=(clientSocket,))
            clientHandler.start()
    except KeyboardInterrupt:
        print("[" + messageTime + "]: Server fährt herunter...")
    finally:
        serverSocket.close()


if __name__ == "__main__":
    startServer()
