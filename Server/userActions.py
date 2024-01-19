import pickle
from hashlib import sha256

USER_FILE = 'user_data.txt'


def load_user_data():
    try:
        with open(USER_FILE, 'rb') as file:
            return pickle.load(file)
    except FileNotFoundError:
        return {}


def save_user_data(users):
    with open(USER_FILE, 'wb') as file:
        pickle.dump(users, file)


def register(username, password):
    users = load_user_data()

    if username in users:
        return "Nutzername bereits in Verwendung"

    hashed_password = sha256(password.encode()).hexdigest()
    users[username] = hashed_password

    save_user_data(users)
    return "Erfolgreich als " + username + " registriert"


def login(username, password):
    users = load_user_data()

    if username not in users:
        return "Dieser Nutzername existiert nicht!"

    hashed_password = sha256(password.encode()).hexdigest()

    if users[username] == hashed_password:
        return "Willkommen, " + username + "! Du bist nun registriert"
    else:
        return "Ungültiges Passwort"
