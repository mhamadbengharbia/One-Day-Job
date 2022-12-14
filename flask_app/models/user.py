from flask_app.config.mysqlconnection import connectToMySQL
import re	 
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
from flask import flash

class User():
    db_name = 'project_schema'
    def __init__(self ,data):
            self.id=data['id']
            self.type=data['type']
            self.address_id=data['address_id']
            self.first_name=data['first_name']
            self.last_name=data['last_name']
            self.education=data['education']
            self.experience=data['experience']
            self.email=data['email']
            self.phone=data['phone']
            self.password=data['password']
            self.birth_date=data['birth_date']
            self.information=data['information']
            self.picture=data['picture']
            self.created_at=data['created_at']
            self.updated_at=data['updated_at']
 

    @classmethod
    def add_user(cls ,data):
        query="INSERT INTO users (first_name, last_name, education, experience, email, phone, password, birth_date, information, picture, address_id) Values ( %(first_name)s, %(last_name)s, %(education)s, %(experience)s, %(email)s, %(phone)s, %(password)s, %(birth_date)s, %(information)s,%(picture)s, %(address_id)s);"
        return connectToMySQL(cls.db_name).query_db(query,data)


    # GET ONE USER BY EMAIL
    @classmethod
    def get_user_by_email(cls, data):
        query = "SELECT * FROM users WHERE email = %(email)s;"
        result = connectToMySQL(cls.db_name).query_db(query, data)

        if result:
            return cls(result[0])
        return False
    
    # GET ONE USER BY ID
    @classmethod
    def get_user_id(cls ,data):
        query="SELECT * FROM users WHERE id = %(id)s"
        result = connectToMySQL(cls.db_name).query_db(query ,data)
 
        return cls(result[0])
    
    # GET ALL USERS
    @classmethod
    def get_all_users(cls):
        query="SELECT * FROM users WHERE type != 1;"
        result = connectToMySQL(cls.db_name).query_db(query)
 
        all_users = []
        for row in result:
            all_users.append(cls(row))
        
        return all_users

    # DELETE USER
    @classmethod
    def delete_user(cls, data):
        query="DELETE FROM users WHERE id = %(id)s;"
        return connectToMySQL(cls.db_name).query_db(query, data)


    # GET TOP USERS
    @classmethod
    def get_top_users(cls):
        query="SELECT * FROM users WHERE type != 1 LIMIT 5;"
        result = connectToMySQL(cls.db_name).query_db(query)
 
        all_users = []
        for row in result:
            all_users.append(cls(row))
        
        return all_users

    # UPDATE USER
    @classmethod
    def edit_user_profile(cls, data):
        query = "UPDATE users SET first_name=%(first_name)s, last_name=%(last_name)s, address_id=%(address_id)s, education=%(education)s, experience=%(experience)s, email=%(email)s, phone=%(phone)s, information=%(information)s WHERE id=%(id)s;"
        return connectToMySQL(cls.db_name).query_db(query, data)



    @staticmethod
    def validate_user_register(user):
        is_valid = True
        query = "SELECT * FROM users WHERE email = %(email)s;"
        results = connectToMySQL(User.db_name).query_db(query,user)
        if len(results) >= 1:
            flash("This email is taken.","register")
            is_valid=False
        if not EMAIL_REGEX.match(user['email']):
            flash("Invalid Email!!!","register")
            is_valid=False
        if len(user['first_name']) < 3:
            flash("First name must be at least 3 characters","register")
            is_valid= False
        if len(user['last_name']) < 3:
            flash("Last name must be at least 3 characters","register")
            is_valid= False
        if len(user['password']) < 8:
            flash("Password must be at least 8 characters","register")
            is_valid= False
        if user['password'] != user['confirm_password']:
            flash("Passwords don't match","register")
        if  'accept' not in user.keys() :
            flash("Please accept out term and conditions","register")
            is_valid= False
        return is_valid
