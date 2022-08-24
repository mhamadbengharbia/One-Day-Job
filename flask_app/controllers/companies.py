from flask import session,render_template,redirect,request
from flask_app import app
from flask_app.models import company
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt(app)
 

# COMPANY REGISTER
@app.route('/company_register')
def company_register():
      return render_template("company_register.html")

# COMPANY LOGIN
@app.route('/company_login')
def company_login():
      return render_template("company_login.html")

# COMPANY DASHBOARD
@app.route('/company_dashboard/<int:id>')
def company_dashboard(id):
      return render_template('company_dashboard.html')

# COMPANY PROFILE
@app.route('/company_profile/<int:id>')
def company_profile(id):
      return render_template('company_profile.html')

# COMPANY UPDATE PROFILE
@app.route('/update_company_profile/<int:id>')
def update_company_profile(id):
      return render_template('update_company_profile.html')

# COMPANY ADD JOB
@app.route('/company/add_job')
def add_job():
      return render_template('add_job.html')

# COMPANY UPDATE JOB
@app.route('/company/update_job')
def update_job():
      return render_template('update_job.html')

# ALL JOBS
@app.route('/jobs')
def all_jobs():
      return render_template('all_jobs.html')


# CREATE NEW COMPANY ROUTE
@app.route('/add_company', methods=['POST'])
def add_company():
    # CHECK IF INPUTS NOT VALIDE REDIRECT TO THE ROOT
#     if not company.Company.validate_user_register(request.form):
#         return redirect('/user_register')
    # IF INPUTS VALID
    # HASH THE PASSWORD & CONFIRM PASSWORD
    hash_pass = bcrypt.generate_password_hash(request.form['password'])

    company.Company.add_company({**request.form, 'password': hash_pass})

    return redirect('/user_login')




 

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