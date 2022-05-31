<<<<<<< HEAD
from unicodedata import name
=======
>>>>>>> d60d0658bdfdcad3cd58957f6189025abeda0a4a
from app import app
from flask import render_template

@app.route('/')
@app.route('/index/<name>')
def index(name="<<Hello World>>"):
<<<<<<< HEAD
    return render_template("index.html", text = name)


=======
    return render_template("index.html", text=name)
>>>>>>> d60d0658bdfdcad3cd58957f6189025abeda0a4a
