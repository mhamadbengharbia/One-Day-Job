from flask import session,render_template,redirect,request
from flask_app import app
 
@app.route('/')
def index():
      return render_template("index.html")