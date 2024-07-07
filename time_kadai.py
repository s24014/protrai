# s24014
# 実行が確認出来たら時間を表示させる「時計アプリ」を作ってみたいと思います
# 時計アプリはモジュール名「time_kadai.py」で作成します
#　時計アプリをバージョンアップしていきます

import datetime
import tkinter as tk # GUIでアプリを作ることのできるモジュール

# 時間を処理する部分を関数で実装
def update_time():
    now = datetime.datetime.now()
    current_time = now.strftime("%Y年%m月%d日 %H時%M分%S秒")#日付、時刻などを表示（自分なりに考えたやつ）
    #
    lbl.config(text=current_time)# フォントを自由に設定できる（自分..）(重要)
    root.after(1000, update_time)# 自分をもう1回

# Tkineのウィンドウを作成
root = tk.Tk()

root.title("現在の時刻")

lbl = tk.Label()
lbl.config(text="", font=("Helvetica", 70))
lbl.pack()

# 関数の呼び出し
update_time()

root.mainloop() # 終わりのまじない
