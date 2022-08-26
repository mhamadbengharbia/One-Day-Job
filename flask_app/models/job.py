from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash

class Job():
    db_name = 'project_schema'
    def __init__(self ,data):
            self.id=data['id']
            self.company_id=data['company_id']
            self.salary=data['salary']
            self.title=data['title']
            self.industry=data['industry']
            self.experience=data['experience']
            self.description=data['description']
            self.end_at=data['end_at']
            self.is_accepted=data['is_accepted']
            self.company_name=data['company_name']
            self.created_at=data['created_at']
            self.updated_at=data['updated_at']

    # CREATE NEW JOB
    @classmethod
    def add_job(cls ,data):
        query="INSERT INTO jobs (company_id, salary, title, industry, experience, description, end_at)  Values (%(company_id)s, %(salary)s, %(title)s, %(industry)s, %(experience)s, %(description)s, %(end_at)s);"
        return connectToMySQL(cls.db_name).query_db(query,data)

    # GET ALL COMPANY Jobs
    @classmethod
    def get_all_jobs(cls, data):
        query="SELECT companies.company as company_name, jobs.* FROM jobs JOIN companies ON jobs.company_id = companies.id WHERE companies.id = %(id)s;"
        result = connectToMySQL(cls.db_name).query_db(query, data)
 
        all_jobs = []
        for row in result:
            all_jobs.append(cls(row))
        
        return all_jobs

     # GET ONE JOB BY ID
    @classmethod
    def get_job_id(cls ,data):
        query="SELECT companies.company as company_name, jobs.* FROM jobs JOIN companies ON jobs.company_id=companies.id WHERE jobs.id = %(id)s"
        result = connectToMySQL(cls.db_name).query_db(query ,data)
 
        return cls(result[0])

    # DELETE JOB
    @classmethod
    def delete_job(cls, data):
        query="DELETE FROM jobs WHERE id = %(id)s;"
        return connectToMySQL(cls.db_name).query_db(query, data)

    # UPDATE JOB
    @classmethod
    def edit_job(cls, data):
        query = "UPDATE jobs SET title=%(title)s, salary=%(salary)s, industry=%(industry)s, experience=%(experience)s, description=%(description)s, end_at=%(end_at)s WHERE id=%(id)s;"
        return connectToMySQL(cls.db_name).query_db(query, data)

    
    # SELECT LATEST JOBS
    @classmethod
    def select_latest_jobs(cls):
        query="SELECT companies.company as company_name, jobs.* FROM jobs LEFT JOIN companies ON jobs.company_id=companies.id ORDER BY jobs.id DESC LIMIT 5;"
        result = connectToMySQL(cls.db_name).query_db(query)
 
        select_jobs = []
        for row in result:
            select_jobs.append(cls(row))

        return select_jobs

    # SELECT ALL JOBS
    @classmethod
    def select_all_jobs(cls):
        query="SELECT companies.company as company_name, jobs.* FROM jobs LEFT JOIN companies ON jobs.company_id=companies.id ORDER BY jobs.id DESC;"
        result = connectToMySQL(cls.db_name).query_db(query)
 
        select_jobs = []
        for row in result:
            select_jobs.append(cls(row))

        return select_jobs