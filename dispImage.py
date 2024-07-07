import tkinter as tk # tkinterをtkと略して使用する
import tkinter.filedialog as fd
import PIL.Image, PIL.ImageTk

def dispLabel(path):
    newImage = PIL.Image.open(path).resize((300,300))
    imageData = PIL.ImageTK.PhotoImage(newImage)
    imageLabel.configure(image = imageData)
    imageLabel.image = imageDate

def openFie():
    fpath = fd.askopenfilename()

    if fpath:
        dispPhoto(fpath)

root = tk.Tk()
root.geometry("400x350")

btn = tk.Button(text="ファイルを開く", command = openFile)
imageLabel = tk.Label()
btn.pack()
imageLabel.pack()

tk.mainloop()
