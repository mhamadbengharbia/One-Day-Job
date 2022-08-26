from flask import render_template,redirect,session,request, flash
from flask_app import app
from flask_app.models import user
from flask_app.models import company
from flask_app.models import job
from flask_app.models import contact
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt(app)


# HOME PAGE
@app.route('/')
def index():
      latest_jobs = job.Job.select_latest_jobs();
      all_jobs = job.Job.select_all_jobs();
      top_users = user.User.get_top_users()
      return render_template("index.html", latest_jobs=latest_jobs, all_jobs=all_jobs, top_users=top_users)

# ABOUT PAGE
@app.route('/about')
def about():
      top_companies = company.Company.get_best_companies()
      top_users = user.User.get_top_users()
      return render_template("about.html", top_companies=top_companies, top_users=top_users)

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

# ADMIN DASHBOARD
@app.route('/admin_dashboard/<int:id>')
def admin_dashboard(id):
      if not session.get('uuid'):
        return redirect('/login')
      logged_user = user.User.get_user_id({"id": session['uuid']})
      if logged_user.type != 1:
            return redirect('/') # TODO ADD PAGE NOT FOUND TEMPLATE
      # GET ALL COMPANIES
      all_companies = company.Company.get_all_companies()
     
      return render_template('admin_dashboard.html', logged_user=logged_user, all_companies=all_companies)

# DISPLAY ALL COMPANIES
@app.route('/display_companies')
def display_companies():
      logged_user = user.User.get_user_id({"id": session['uuid']})
      if logged_user.type != 1:
            return redirect('/') # TODO ADD PAGE NOT FOUND TEMPLATE
      # GET ALL COMPANIES
      all_companies = company.Company.get_all_companies()
      return render_template('admin_dashboard.html', logged_user=logged_user, all_companies=all_companies)

# DISPLAY ALL USERS
@app.route('/display_users')
def display_users():
      logged_user = user.User.get_user_id({"id": session['uuid']})
      if logged_user.type != 1:
            return redirect('/') # TODO ADD PAGE NOT FOUND TEMPLATE

      # GET ALL USERS EXCEPT ADMINS
      all_users = user.User.get_all_users()
      return render_template('admin_dashboard.html', logged_user=logged_user, all_users=all_users)

# DISPLAY ADMIN CONTACTS
@app.route('/sellect_msgs')
def sellect_msgs():
      logged_user = user.User.get_user_id({"id": session['uuid']})
      if logged_user.type != 1:
            return redirect('/') # TODO ADD PAGE NOT FOUND TEMPLATE
      admin_contacts=contact.Contact.sellect_msgs()
      return render_template('admin_dashboard.html', logged_user=logged_user, admin_contacts=admin_contacts)
# DELETE MESSAGE
@app.route('/delete_msg/<int:id>')
def delete_msg(id):
      if not session.get('uuid'):
        return redirect('/login')
      logged_user = user.User.get_user_id({"id": session['uuid']})
      if logged_user.type != 1:
            return redirect('/') # TODO ADD PAGE NOT FOUND TEMPLATE
      contact.Contact.delete_msg({'id': id})
      return redirect('/sellect_msgs')

# USER DASHBOARD
@app.route('/user_dashboard/<int:id>')
def user_dashboard(id):
      if not session.get('uuid'):
        return redirect('/login')
      return render_template('user_profile.html', logged_user=user.User.get_user_id({"id": id}))

# USER PROFILE
@app.route('/user_profile/<int:id>')
def user_profile(id):
      if not session.get('uuid'):
        return redirect('/login')
      return render_template('user_profile.html', logged_user=user.User.get_user_id({"id": id}))

# USER UPDATE PROFILE
@app.route('/update_user_profile/<int:id>')
def update_user_profile(id):
     
      if not session.get('uuid'):
        return redirect('/login')
      return render_template('update_user_profile.html', selected_user=user.User.get_user_id({'id': id}))

# EDIT USER PROFILE
@app.route('/edit_user_profile/<int:id>', methods=['POST'])
def edit_user_profile(id):
      if not user.User.validate_user_register(request.form):
        return redirect(f'/update_user_profile/{id}')
      user.User.edit_user_profile({**request.form, 'id': id})
      return redirect(f'/user_profile/{id}')

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

    if selected_user.type == 1:
      return redirect(f"/admin_dashboard/{session['uuid']}")
    
    return redirect(f"/user_dashboard/{session['uuid']}")

@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")

# DELETE COMPANY
@app.route("/delete_company/<int:id>")
def delete_company(id):
      logged_user=user.User.get_user_id({"id": session['uuid']})
      if logged_user.type != 1:
            return redirect('/not_found.html') # TODO CREATE not_found..html PAGE

      company.Company.delete_company({"id": id})

      return redirect(f"/admin_dashboard/{session['uuid']}")

# DELETE USER
@app.route("/delete_user/<int:id>")
def delete_user(id):
      logged_user=user.User.get_user_id({"id": session['uuid']})
      if logged_user.type != 1:
            return redirect('/not_found.html') # TODO CREATE not_found.html PAGE

      user.User.delete_user({"id": id})

      return redirect(f"/admin_dashboard/{session['uuid']}")

# SHOW ALL TALENTS IN all_job_seekers.html TEMPLATE
@app.route('/show_all_talents')
def show_all_talents():
    all_talents = user.User.get_all_users()
    return render_template('all_job_seekers.html', all_talents=all_talents)