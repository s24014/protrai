#s24014 entry_kadai.py
#エントリーウィジットで受け付けた金額を税込み(10%)価格として出力する

import tkinter as tk # tkinterをtkと略して使用する
#print("金額を入力してください")
#a = input()
#print(type(a))
    

    a = entry.get()
    print(f"aは{type(a)}")
    lbl.config(text=f"{a} * 1.1")

    input(lbl.config)
    print(lbl.config)

root = tk.Tk()
root.title("エントリーウィジット")
root.geometry("400x200")

lbl = tk.Label(text="税込み価格", font=("Helvetica", 20))
entry = tk.Entry(font=("Helvetica", 20))
btn = tk.Button(text="ボタン", font=("Helvetica", 20), command=dispLabel)

lbl.pack()
entry.pack()
btn.pack()

tk.mainloop()

