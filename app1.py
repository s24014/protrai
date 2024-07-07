import tkinter as tk # tkinterをimpoterしてtkと略して使う

def dispLabel():
    lbl.config(text="こんにちは")
    
root = tk.Tk() # 画面を作る
root.geometry("400x200") # 画面の大きさを決める

lbl= tk.Label(text="LABEL") # ラベルを作る
btn =tk.Button(text="PUSH", command=dispLabel) # ボタンを作る

lbl.pack() # 画面にラベルを配置する
lbl2 = tk.Label(text="ラベル2", font=("Helvetica", 20)).pack()

btn.pack() # 画面にボタンを配置する
lbl2 = tk.Label(text="", font=("Helvetica", 20)).pack()

btn2 = tk.
Button(text="何もしないボタン", command=dispLabel, font=("Helvetica")).pack()

tk.mainloop() # 作ったウィンドウを表示する
