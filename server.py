from flask import Flask, render_template, request, redirect, url_for, jsonify
app = Flask(__name__)
from random import randint


# Routes
@app.route('/')
def layout():
    return render_template('layout.html')

if __name__ == '__main__':
    app.run(debug=True)