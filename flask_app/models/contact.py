from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
import re	 
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class Contact():
    db_name = 'project_schema'
    def __init__(self ,data):
            self.id=data['id']
            self.user_id=data['user_id']
            self.name=data['name']
            self.email=data['email']
            self.subjuct=data['subjuct']
            self.description=data['description']
            self.created_at=data['creates_at']
            self.updated_at=data['updated_at']

    # SEND MESSAGE TO THE ADMIN
    @classmethod
    def contact_admin(cls, data):
        query="INSERT INTO contacts (name, email, subjuct, description, user_id) Values ( %(name)s, %(email)s, %(subjuct)s, %(description)s, %(user_id)s);"
        return connectToMySQL(cls.db_name).query_db(query,data)