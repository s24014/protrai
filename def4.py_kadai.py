# def4.py
# メインの処理をmain()関数に行わせるおみくじプログラム
#

import random

#ランダムでkujiの中の一つを返す関数 
def omikuji():
    kuji = ["大吉","中吉","小吉","凶"]
    return random.choice(kuji)

def main():
    kekka = omikuji()
    print("結果は", kekka, "です")

if __name__ == "__main__":
    main()
