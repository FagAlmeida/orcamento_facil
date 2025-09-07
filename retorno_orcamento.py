from flask import Flask, redirect, render_template, request, url_for, session
from flask_pymongo import PyMongo


app = Flask(__name__)

@app.route('/', methods=['GET'])
def inicial():
    return render_template('inicial.html')



if __name__ == '__main__':
    app.run(debug=True)