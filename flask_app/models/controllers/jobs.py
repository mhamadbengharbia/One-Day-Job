from flask import session,render_template,redirect,request, flash
from flask_app import app
from flask_app.models import job
from flask_app.models import company

# ADD NEW JOB
@app.route('/create_job', methods=['POST'])
def create_job():
    if not company.Company.validate_company_addjob(request.form):
        return redirect('/company/add_job')
    data={
        "company_id":request.form['company_id'],
        "salary":request.form['salary'],
        "title":request.form['title'],
        "industry":request.form['industry'],
        "experience":request.form['experience'],
        "description":request.form['description'],
        "end_at":request.form['end_at'],
    }
    
 
    job.Job.add_job(data)
    return redirect(f'/company_dashboard/{session["uuid"]}')


# DISPLAY ALL JOBS
@app.route('/display_jobs')
def display_jobs():
    if not session.get('uuid'):
        return redirect('/login')
      # GET ALL JOBS
    all_jobs =job.Job.get_all_jobs({'id': session['uuid']})

    return render_template('company_dashboard.html', all_jobs=all_jobs, logged_company=company.Company.get_company_id({"id": session['uuid']}))

# DISPLAY JOB DETAILS
@app.route('/job_details/<int:id>')
def job_details(id):
    if not session.get('uuid'):
        return redirect('/login')
    return render_template('job_details.html', sellected_job=job.Job.get_job_id({'id': id}))

# DELETE JOB
@app.route('/delete_job/<int:id>')
def delete_job(id):
    if not session.get('uuid'):
        return redirect('/login')
    job.Job.delete_job({'id': id})
    return redirect('/display_jobs')

# UPDATE JOB TEMPLATE
@app.route('/update_job/<int:id>')
def update_job(id):
      if not session.get('uuid'):
        return redirect('/login')
      return render_template('update_job.html', sellected_job=job.Job.get_job_id({'id': id}))

# EDIT JOB
@app.route('/edit_job/<int:id>', methods=['POST'])
def edit_job(id):
    job.Job.edit_job({**request.form, 'id': id})
    return redirect(f'/job_details/{id}')


# SHOW ALL JOBS IN all_jobs.html TEMPLATE
@app.route('/show_all_jobs')
def show_all_jobs():
    all_jobs = job.Job.select_all_jobs()
    return render_template('all_jobs.html', all_jobs=all_jobs)

