<<<<<<< HEAD
import tkinter as tk
import tkinter.filedialog as fd
import PIL.Image
import PIL.ImageTk

def disphoto(path):
    newImage = PIL.Image.open(path).resize((300,300))
    imageData = PIL.ImageTk.PhotoImage(newImage)
    imageLabel.configure(image = imageData)
    imageLabel.image = imageData

def openFile():
    fpath = fd.askopenfilename()
    if fpath:
        disphoto(fpath)

root = tk.Tk()
root.geometry("400x350")

btn = tk.Button (text="ファイルを開く", command = openFile)
imageLabel = tk.Label()
btn.pack()
imageLabel.pack()

tk.mainloop()
=======
import tkinter as tk
import tkinter.filedialog as fd
import PIL.Image
import PIL.ImageTk

def disphoto(path):
    newImage = PIL.Image.open(path).resize((300,300))
    imageData = PIL.ImageTk.PhotoImage(newImage)
    imageLabel.configure(image = imageData)
    imageLabel.image = imageData

def openFile():
    fpath = fd.askopenfilename()
    if fpath:
        disphoto(fpath)

root = tk.Tk()
root.geometry("400x350")

btn = tk.Button (text="ファイルを開く", command = openFile)
imageLabel = tk.Label()
btn.pack()
imageLabel.pack()

tk.mainloop()
>>>>>>> e1fe15809f50b1742ddbe075234d70a030202ab4
