from flask_app import app
import flask_app.controllers.users
import flask_app.controllers.companies
if __name__ == "__main__":
    app.run(debug=True)