import tkinter
from tkinter import ttk
import sys

import Values

gamemode = None
screenH = 800
screenW = 800

if __name__ == "__main__":
    sys.exit("Starte Gamemode.py, um das Spiel zu starten")

secDialog = False


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
            if 400 <= int(screenHEntry.get()) <= screenHMax and 400 <= int(screenWEntry.get()) <= screenWMax:
                gamemode = int(selectedOption.get())
                screenH = int(screenHEntry.get())
                screenW = int(screenWEntry.get())
                root.destroy()
        except ValueError:
            screenH.set(800)
            screenW.set(800)

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

            print(selectedSkin.get())
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

    selectedFullscreen = tkinter.IntVar(root)
    selectedOption = tkinter.IntVar(root)
    screenH = tkinter.IntVar(root)
    screenW = tkinter.IntVar(root)

    fullscreen = ttk.Checkbutton(root, text="Vollbild", command=setScreen, variable=selectedFullscreen)
    fullscreen.pack(pady=(25, 0))

    screenHEntry = ttk.Entry(root, textvariable=screenH)
    screenHEntry.pack()
    screenH.set(800)
    screenWEntry = ttk.Entry(root, textvariable=screenW)
    screenWEntry.pack(pady=(0, 10))
    screenW.set(800)

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
