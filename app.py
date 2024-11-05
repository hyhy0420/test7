from flask import Flask, redirect, render_template
import random

app = Flask(__name__)

# GoogleフォームのURLリスト
form_urls = [
    'https://akeoblog.com/npmnotfound/',
    'https://docs.google.com/forms/d/15olhz0cd9GWvB9duOwhV-BpaIonSdeGaJhAWg5iOPdA/edit',
    'https://robogaku.jp/news/2020/past_31_9_8.html'
]

@app.route('/')
def home():
    # index.htmlをレンダリングして、JavaScriptがリダイレクトを行う
    return render_template('index.html')

@app.route('/open-form')
def open_form():
    # リストからランダムにURLを選択
    chosen_form_url = random.choice(form_urls)
    # 選択したURLにリダイレクト
    return redirect(chosen_form_url)

if __name__ == '__main__':
    app.run(debug=True)
