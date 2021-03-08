from flask import Flask
#from flask import Flask, render_template, url_for, flash, redirect
from flask import Flask, render_template, redirect, url_for, request
import json
import requests
app = Flask(__name__)

@app.route('/home', methods=['GET', 'POST'])
@app.route('/', methods=['GET', 'POST'])
def home():

    if request.method == 'GET':
        
        return render_template('hello.html')

    if request.method == 'POST':
        char = request.form['text']
        char = f"https://api.tibiadata.com/v2/characters/{char}.json"
        char = requests.get(char)
        
        char_content = char.content
        char = json.loads(char_content)
        print(char)
        #render_template('hello.html', char = char)
        return char

@app.route('/registrar')
def registrar_celo():

    return 'registrar.html'

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = 'Invalid Credentials. Please try again.'
        else:
            return redirect(url_for('home'))
    return render_template('login.html', error=error)

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)

if __name__ == '__main__':
    app.run(debug=True)