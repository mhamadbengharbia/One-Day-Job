from flask import render_template,redirect,session,request, flash
from flask_app import app
from flask_app.models import user
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

# LOGIN TYPE
@app.route('/login')
def login():
      return render_template('/login_type.html')

# REGISTER TYPE
@app.route('/register')
def register():
      return render_template('/register_type.html')

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
      return render_template('user_dashboard.html', logged_user=user.User.get_user_id({"id": session['uuid']}))

# USER PROFILE
@app.route('/user_profile/<int:id>')
def user_profile(id):
      return render_template('user_profile.html')

# USER UPDATE PROFILE
@app.route('/update_user_profile/<int:id>')
def update_user_profile(id):
      return render_template('update_user_profile.html')



# CREATE NEW USER ROUTE
@app.route('/add_user', methods=['POST'])
def add_user():
    # CHECK IF INPUTS NOT VALIDE REDIRECT TO THE ROOT
    if not user.User.validate_user_register(request.form):
        return redirect('/user_register')
    # IF INPUTS VALID
    # HASH THE PASSWORD & CONFIRM PASSWORD
    hash_pass = bcrypt.generate_password_hash(request.form['password'])

    user.User.add_user({**request.form, 'password': hash_pass})

    return redirect('/user_login')

#USER  LOGIN
@app.route('/login_user', methods=['POST'])
def login_user():
    selected_user = user.User.get_user_by_email(request.form)
    if not selected_user:
        flash("Invalid Email / Password ", 'login')
        return redirect('/user_login')
    if not bcrypt.check_password_hash(selected_user.password, request.form['password']):
        flash("Invalid Email / Password ", 'login')
        return redirect('/user_login')
    
    session['uuid'] = selected_user.id
    
    return redirect(f"/user_dashboard/{session['uuid']}")

# @app.route("/logout")
# def logout():
#     session.clear()
#     return redirect("/")
