import tkinter
from tkinter import ttk
import sys

import Values

gamemode = None
screenH = 800
screenW = 800

if __name__ == "__main__":
    sys.exit("Starte Gamemode.py, um das Spiel zu starten")


def gamemodeDialog():
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
        def setSkinPack():
            Values.chosenSkinPacket = selectedSkin.get()
            root2.destroy()

        root2 = tkinter.Tk()
        root2.geometry("400x250")
        root2.title("Wähle dein Skin-paket!")

        selectedSkin = tkinter.StringVar(root2)

        defaultSkinPack = ttk.Radiobutton(root2, text="Default Skin-paket", variable=selectedSkin, value="default")
        defaultSkinPack.pack(pady=(60, 5))
        SkinPack2 = ttk.Radiobutton(root2, text="Paket 2", variable=selectedSkin, value="paket2")
        SkinPack2.pack(pady=5)
        SkinPack3 = ttk.Radiobutton(root2, text="Paket 3", variable=selectedSkin, value="paket3")
        SkinPack3.pack(pady=(5, 30))

        confirmButton = ttk.Button(root2, text="Wählen", command=setSkinPack)
        confirmButton.pack()

        root2.mainloop()

    selectedFullscreen = tkinter.IntVar(root)
    selectedOption = tkinter.IntVar(root)
    screenH = tkinter.IntVar(root)
    screenW = tkinter.IntVar(root)

    skinButton = ttk.Button(root, text="Wähle dein Skin-paket", command=openSkinDialog)
    skinButton.place(relx=0.0, rely=0.0, anchor='nw')

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
    close.pack(pady=10)

    root.mainloop()

    return gamemode, screenH, screenW
