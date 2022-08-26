from flask import session,render_template,redirect,request, flash
from flask_app import app
from flask_app.models import company
from flask_app.models import job
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
      if not session.get('uuid'):
        return redirect('/login')
      return render_template('company_dashboard.html', logged_company=company.Company.get_company_id({"id": session['uuid']}), all_jobs =job.Job.get_all_jobs({'id': session['uuid']}))

# COMPANY PROFILE
@app.route('/company_profile/<int:id>')
def company_profile(id):
      if not session.get('uuid'):
        return redirect('/login')
      return render_template('company_profile.html', logged_company=company.Company.get_company_id({"id": id}))

# COMPANY UPDATE PROFILE
@app.route('/update_company_profile/<int:id>')
def update_company_profile(id):
      if not session.get('uuid'):
        return redirect('/login')
      return render_template('update_company_profile.html', up_company=company.Company.get_company_id({'id': id}))

# EDIT COMPANY PROFILE
@app.route('/edit_company_profile/<int:id>', methods=['POST'])
def edit_company_profile(id):
      company.Company.edit_company_profile({**request.form, 'id':id})
      return redirect(f'/company_profile/{id}')

# COMPANY ADD JOB
@app.route('/company/add_job')
def add_job():
      if not session.get('uuid'):
        return redirect('/login')
      return render_template('add_job.html')

# ALL JOBS
@app.route('/jobs')
def all_jobs():
      return render_template('all_jobs.html')


# CREATE NEW COMPANY ROUTE
@app.route('/add_company', methods=['POST'])
def add_company():
    # CHECK IF INPUTS NOT VALIDE REDIRECT TO THE ROOT
    if not company.Company.validate_company_register(request.form):
        return redirect('/company_register')
    # IF INPUTS VALID
    # HASH THE PASSWORD & CONFIRM PASSWORD
    hash_pass = bcrypt.generate_password_hash(request.form['password'])

    company.Company.add_company({**request.form, 'password': hash_pass})

    return redirect('/company_login')

# Company  LOGIN
@app.route('/login_company', methods=['POST'])
def login_company():
    selected_company = company.Company.get_company_by_email(request.form)
    if not selected_company:
        flash("Invalid Email / Password ", 'login')
        return redirect('/company_login')
    if not bcrypt.check_password_hash(selected_company.password, request.form['password']):
        flash("Invalid Email / Password ", 'login')
        return redirect('/company_login')
    
    session['uuid'] = selected_company.id
    
    return redirect(f"/company_dashboard/{session['uuid']}") 

