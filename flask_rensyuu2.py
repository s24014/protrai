#flaskの練習
#s24014

#事前にflaskモジュールをインストールする
from flask import Flask, render_template
# Flaskライブラリをインスタンス化し、app変数に割り当て
#　その際、コンストラクタへの引数は実行中のモジュールを指定する
app = Flask(__name__)

#ルートURLに対するリクエストを処理する関数を定義するデコレーター
#　引数にルートに'/'を指定するアクセスした際index（）関数が呼び出される
@app.route('/')
def index():
    return render_template('index.html')

#秘密のページ
@app.route('/himitsu')
def himitsu():
    return render_template('himitsu.html')

if __name__ == '__main__':
#それぞれのユニークなIPアドレスでアクセスするように設定
    app.run(host='0.0.0.0', port=5000, debug=True)


    
# python flask_rensyu2.pyで実行し
# ブラウザから表示させてみましょう

