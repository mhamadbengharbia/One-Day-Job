from flask import render_template,redirect,session,request, flash
from flask_app import app
from flask_app.models.user import User
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)
# HOME PAGE
@app.route('/')
def index():
      return render_template("index.html")

# ABOUT PAGE
@app.route('/about')
def about():
      return render_template("about.html")

# CONTACT PAGE
@app.route('/contact')
def contact():
      return render_template("contact.html")

# USER REGISTER
@app.route('/user_register')
def user_register():
      return render_template("user_register.html")

# USER LOGIN
@app.route('/user_login')
def user_login():
      return render_template("user_login.html")

# USER DASHBOARD
@app.route('/user_dashboard/<int:id>')
def user_dashboard(id):
      return render_template('user_dashboard.html')

# USER PROFILE
@app.route('/user_profile/<int:id>')
def user_profile(id):
      return render_template('user_profile.html')

# USER UPDATE PROFILE
@app.route('/update_user_profile/<int:id>')
def update_user_profile(id):
      return render_template('update_user_profile.html')



# @app.route("/logout")
# def logout():
#     session.clear()
#     return redirect("/")

# @app.route('/login',methods=['POST'])
# def login():
#     user = User.get_user_email(request.form)
#     if not user:
#         flash("Email not valid","login")
#         return redirect('/')
#     if not bcrypt.check_password_hash(user.password, request.form['password']):
#         flash("Password not valid","login")
#         return redirect('/')
#     session['user_id'] = user.id
#     return redirect('/dashboard')