from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return "Selamat datang di halaman utama!"

@app.route('/about')
def about():
    return "Ini adalah halaman tentang kami."

if __name__ == '__main__':
    app.run()
