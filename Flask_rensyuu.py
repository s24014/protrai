#flaskの練習
#s24014

#事前にflaskモジュールをインストールする
#render_tmplateはhtmlファイルを扱う際必要
from flask import Flask, render_template
# Flaskライブラリをインスタンス化し、app変数に割り当て
#　その際、コンストラクタへの引数は実行中のモジュールを指定する
app = Flask(__name__)

#ルートURLに対するリクエストを処理する関数を定義するデコレーター
#　引数にルートに'/'を指定するアクセスした際index（）関数が呼び出される
@app.route('/')
def index():
    # template/index.htmlをあらかじめ作成しておく
    return "<h1>Hello World</h1>"
if __name__ == '__main__':
    app.run(debug=True)
