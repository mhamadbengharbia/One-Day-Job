from flask import render_template,redirect,session,request, flash
from flask_app import app
from flask_app.models.contact import Contact

# CONTACT PAGE
@app.route('/contact')
def contact():
      return render_template("contact.html")

@app.route('/contact_admin', methods=['POST'])
def contact_admin():
    Contact.contact_admin(request.form)

    return redirect('/contact')

