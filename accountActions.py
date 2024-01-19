import pickle
import socket
import time


def connect():
    start = time.time()
    onlineConnection = False
    while time.time() - start <= 3 and not onlineConnection:
        try:  # Falls keine Verbindung mit dem Server zustande kommt: Fehler abfangen, Programm durch Sys-exit beenden mit entsprechender Nachricht
            clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            clientSocket.connect(('jythonchess.de', 8888))  # Verbinden mit dem Server, falls möglich

            onlineConnection = True

            return clientSocket
        except Exception as e:
            return False


def register(*payload):
    cSocket = connect()

    if cSocket:
        cSocket.send("manageAccount".encode())
        data = pickle.dumps(("REGISTER", *payload))
        cSocket.send(data)
        response = cSocket.recv(1024).decode()

        return response


def logIn(*payload):
    cSocket = connect()

    if cSocket:
        cSocket.send("manageAccount".encode())
        data = pickle.dumps(("LOGIN", *payload))
        cSocket.send(data)
        response = cSocket.recv(1024).decode()

        return response
