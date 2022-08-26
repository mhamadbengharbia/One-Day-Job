from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
import re	 
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
URL_REGEX = re.compile(r'^https?:\\/\\/(?:www\\.)?[-a-zA-Z0-9@:%._\\+~#=]{1,256}\\.[a-zA-Z0-9()]{1,6}\\b(?:[-a-zA-Z0-9()@:%_\\+.~#?&\\/=]*)$')

class Company():
    db_name = 'project_schema'
    def __init__(self ,data):
            self.id=data['id']
            self.address_id=data['address_id']
            self.company=data['company']
            self.email=data['email']
            self.phone=data['phone']
            self.web_site=data['web_site']
            self.password=data['password']
            self.logo=data['logo']
            self.description=data['description']
            self.unique_identfier=data['unique_identfier']
            self.activite_area=data['activite_area']
            self.created_at=data['created_at']
            self.updated_at=data['updated_at']

    # CREATE NEW COMPANY
    @classmethod
    def add_company(cls ,data):
        query="INSERT INTO companies (company, email, phone, web_site, password, logo, description, unique_identfier, activite_area, address_id) Values ( %(company)s, %(email)s, %(phone)s, %(web_site)s, %(password)s, %(logo)s, %(description)s, %(unique_identfier)s, %(activite_area)s, %(address_id)s);"
        return connectToMySQL(cls.db_name).query_db(query,data)

            
     # GET ONE COMPANY BY EMAIL
    @classmethod
    def get_company_by_email(cls, data):
        query = "SELECT * FROM companies WHERE email = %(email)s;"
        result = connectToMySQL(cls.db_name).query_db(query, data)

        if result:
            return cls(result[0])
        return False

    # GET ONE COMPANY BY ID
    @classmethod
    def get_company_id(cls ,data):
        query="SELECT * FROM companies WHERE id = %(id)s;"
        result = connectToMySQL(cls.db_name).query_db(query ,data)
 
        return cls(result[0])

    # GET ALL COMPANIES
    @classmethod
    def get_all_companies(cls):
        query="SELECT * FROM companies;"
        result = connectToMySQL(cls.db_name).query_db(query)
 
        all_companies = []
        for row in result:
            all_companies.append(cls(row))
        
        return all_companies

    # GET BEST COMPANIES
    @classmethod
    def get_best_companies(cls):
        query="SELECT * FROM companies ORDER BY id DESC LIMIT 4;"
        result = connectToMySQL(cls.db_name).query_db(query)
 
        all_companies = []
        for row in result:
            all_companies.append(cls(row))
        
        return all_companies

    # DELETE COMPANY
    @classmethod
    def delete_company(cls, data):
        query="DELETE FROM companies WHERE id = %(id)s;"
        return connectToMySQL(cls.db_name).query_db(query, data)

    # UPDATE COMPANY
    @classmethod
    def edit_company_profile(cls, data):
        query = "UPDATE companies SET company=%(company)s, email=%(email)s, phone=%(phone)s, web_site=%(web_site)s, description=%(description)s, unique_identfier=%(unique_identfier)s WHERE id=%(id)s;"
        return connectToMySQL(cls.db_name).query_db(query, data)
 

    # COMPANY FORM VALIDATION
    @staticmethod
    def validate_company_register(company):
        is_valid = True
        query = "SELECT * FROM companies WHERE email = %(email)s;"
        results = connectToMySQL(Company.db_name).query_db(query,company)
        if len(results) >= 1:
            flash("This email is taken.","company_register")
            is_valid=False
        if not EMAIL_REGEX.match(company['email']):
            flash("Invalid Email!!!","company_register")
            is_valid=False
        if len(company['web_site']) < 2:
            flash("Invalid url!!!","company_register")
            is_valid=False
        # if not URL_REGEX.match(company['web_site']):
        #     flash("Invalid url!!!","company_register")
        #     is_valid=False
        if len(company['company']) < 3:
            flash("Company name must be at least 3 characters","company_register")
            is_valid= False
        if company['activite_area'] == "Activity area...":
            flash("Choose an activite","company_register")
            is_valid= False
        if len(company['logo']) < 3:
            flash("Logo can't be empty","company_register")
            is_valid= False
        if len(company['phone']) < 8:
            flash("Invalid phone number","company_register")
            is_valid= False
        if len(company['description']) < 8:
            flash("Description must be at least 10 characters","company_register")
            is_valid= False
        if len(company['password']) < 8:
            flash("Password must be at least 8 characters","company_register")
            is_valid= False
        if company['password'] != company['confirm_password']:
            flash("Passwords don't match","company_register")
        if  'accept' not in company.keys() :
            flash("Please accept out term and conditions","company_register")
            is_valid= False
        return is_valid



    # CAdd a job validation form
    @staticmethod
    def validate_company_addjob(company):
        is_valid = True
        if len(company['title']) < 2:
            flash("Invalid Title !!!","company_add")
            is_valid=False
        if (company['salary']) < "0":
            flash("Salary can't be emty or negative","company_add")
            is_valid= False
        if company['end_at'] == "":
            flash("Choose an end at date","company_add")
            is_valid= False
        if (company['industry']) == "Job type...":
            flash("Job type can't be empty","company_add")
            is_valid= False
        if len(company['experience']) < 10:
            flash("experience must be at least 10 characters","company_add")
            is_valid= False
        if len(company['description']) < 10:
            flash("description must be at least 10 characters","company_add")
            is_valid= False
        if  'accept' not in company.keys() :
            flash("Please accept out term and conditions","company_add")
            is_valid= False
        return is_valid
