from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, world!'


@app.route('/pokemon')
def pokemon():
    return 'pokemon is alive !'