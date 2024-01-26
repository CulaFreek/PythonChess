import Gamemode
import Values
import accountActions

import pickle
import tkinter
from tkinter import ttk
import sys

ACC_FILE = 'files/acc_data.txt'

gamemode = None
screenH = 1000
screenW = 1000

if __name__ == "__main__":
    sys.exit("Starte Gamemode.py, um das Spiel zu starten")

secDialog = False
accAction = None


def load_user_data():
    try:
        with open(ACC_FILE, 'rb') as file:
            return pickle.load(file)
    except FileNotFoundError:
        return {}


def save_user_data(users):
    with open(ACC_FILE, 'wb') as file:
        pickle.dump(users, file)


def gamemodeDialog():
    global secDialog
    global gamemode
    global screenH
    global screenW

    root = tkinter.Tk()
    root.geometry("400x250")
    root.title("Wähle deine Spieleinstellungen")

    screenHMax = root.winfo_screenheight()
    screenWMax = root.winfo_screenwidth()

    def getValues():
        global gamemode
        global screenH
        global screenW

        try:
            if 500 <= int(screenHEntry.get()) <= screenHMax and 500 <= int(screenWEntry.get()) <= screenWMax:
                gamemode = int(selectedOption.get())
                screenH = int(screenHEntry.get())
                screenW = int(screenWEntry.get())
                root.destroy()

        except ValueError:
            screenH.set(1000)
            screenW.set(1000)

    def setScreen():
        global screenH
        global screenW

        if selectedFullscreen.get() == 1:
            screenH.set(screenHMax)
            screenW.set(screenWMax)

            screenHEntry.configure(state=tkinter.DISABLED)
            screenWEntry.configure(state=tkinter.DISABLED)
        else:
            screenHEntry.configure(state=tkinter.NORMAL)
            screenWEntry.configure(state=tkinter.NORMAL)

    def openSkinDialog():
        global secDialog

        def setSkinPack():
            global secDialog

            if selectedSkin.get() != Values.chosenSkinPacket:
                Values.chosenSkinPacket = selectedSkin.get()
                Gamemode.newSound()

            Values.chosenSkinPacket = selectedSkin.get()
            secDialog = False
            root2.destroy()

        if not secDialog:

            secDialog = True

            root2 = tkinter.Tk()
            root2.geometry("400x250")
            root2.title("Wähle dein Skin-paket!")

            selectedSkin = tkinter.StringVar(root2)

            defaultSkinPack = ttk.Radiobutton(root2, text="Default Skin-paket", variable=selectedSkin, value="default")
            defaultSkinPack.pack(pady=(100, 5))
            selectedSkin.set(Values.chosenSkinPacket)
            SkinPack2 = ttk.Radiobutton(root2, text="Weihnachts Skin-paket", variable=selectedSkin, value="christmas")
            SkinPack2.pack(pady=(5, 30))

            confirmButton = ttk.Button(root2, text="Wählen", command=setSkinPack)
            confirmButton.pack()

            root2.mainloop()

    def openAccountDialog():
        global secDialog
        global accAction

        accAction = None

        def enterPassword():
            def registerUser():
                global secDialog

                if accountName.get() != "" and accountPassword.get() != "" and len(accountName.get()) >= 4 and len(accountPassword.get()) >= 4:
                    success = accountActions.register(accountName.get(), accountPassword.get())
                    if success is not None:
                        save_user_data(accountName.get())

                        accountMessage.set(success)
                        secDialog = False
                        root3.destroy()
                    else:
                        accountName.delete(0, "end")
                        accountName.insert(0, "Server nicht erreichbar")
                        accountPassword.delete(0, "end")

            def logInUser():
                global secDialog

                if accountName.get() != "" and accountPassword.get() != "":
                    success = accountActions.logIn(accountName.get(), accountPassword.get())
                    if success is not None:
                        save_user_data(accountName.get())

                        accountMessage.set(success)
                        secDialog = False
                        root3.destroy()
                    else:
                        accountName.delete(0, "end")
                        accountName.insert(0, "Server nicht erreichbar")
                        accountPassword.delete(0, "end")

            root3 = tkinter.Tk()
            root3.geometry("400x250")
            root3.title("Logge dich in deinen Account ein!")

            Label1 = ttk.Label(root3, text="Gib deinen Account-Namen ein:")
            Label1.pack()
            accountName = ttk.Entry(root3)
            accountName.pack(pady=(10, 50))
            Label2 = ttk.Label(root3, text="Gib deinen Account-Passwort ein:")
            Label2.pack()
            accountPassword = ttk.Entry(root3, show="*")
            accountPassword.pack(pady=(10, 50))

            if accAction == "Register":
                confirmButton = ttk.Button(root3, text="Registrieren", command=registerUser)
                confirmButton.pack()
            elif accAction == "logIn":
                confirmButton = ttk.Button(root3, text="Einloggen", command=logInUser)
                confirmButton.pack()

            root3.mainloop()

        def setReg():
            global accAction

            accAction = "Register"
            loginOrRegister.destroy()
            enterPassword()

        def setLog():
            global accAction

            accAction = "logIn"
            loginOrRegister.destroy()
            enterPassword()

        if not secDialog:
            secDialog = True

            loginOrRegister = tkinter.Tk()
            loginOrRegister.title("Anmelden oder Registrieren?")

            register = ttk.Button(loginOrRegister, text="Registrieren", command=setReg)
            register.pack(side="left")

            logIn = ttk.Button(loginOrRegister, text="Einloggen", command=setLog)
            logIn.pack(side="right")

            loginOrRegister.mainloop()

    selectedFullscreen = tkinter.IntVar(root)
    selectedOption = tkinter.IntVar(root)
    screenH = tkinter.IntVar(root)
    screenW = tkinter.IntVar(root)

    accountMessage = tkinter.StringVar(root)

    user = load_user_data()
    if str(user) != "{}":
        accountMessage.set("Eingeloggt als " + str(user))

    accountOptions = ttk.Button(root, text="Account", command=openAccountDialog)
    accountOptions.place(x=0, y=0, anchor="nw")
    accountMessageLabel = ttk.Label(root, textvariable=accountMessage)
    accountMessageLabel.place(x=80, y=2, anchor="nw")

    fullscreen = ttk.Checkbutton(root, text="Vollbild", command=setScreen, variable=selectedFullscreen)
    fullscreen.pack(pady=(25, 0))

    screenHEntry = ttk.Entry(root, textvariable=screenH)
    screenHEntry.pack()
    screenH.set(1000)
    screenWEntry = ttk.Entry(root, textvariable=screenW)
    screenWEntry.pack(pady=(0, 10))
    screenW.set(1000)

    oDR = ttk.Radiobutton(root, text="Spiele mit einem Freund auf diesem Gerät", variable=selectedOption, value=0)
    oDR.pack(pady=(20, 5))
    oPR = ttk.Radiobutton(root, text="Spiele online", variable=selectedOption, value=1)
    oPR.pack(pady=5)
    bER = ttk.Radiobutton(root, text="Spiele gegen einen bot", variable=selectedOption, value=2)
    bER.pack(pady=5)

    close = ttk.Button(root, text="Spielen", command=getValues)
    close.pack(pady=10, side="right", padx=(0, 75))

    skinButton = ttk.Button(root, text="Wähle dein Skin-paket", command=openSkinDialog)
    skinButton.pack(pady=10, side="left", padx=(75, 0))

    root.mainloop()

    return gamemode, screenH, screenW
