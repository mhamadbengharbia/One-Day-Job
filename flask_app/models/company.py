from flask_app.config.mysqlconnection import connectToMySQL
import re	 
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
from flask import flash

class Company():
    def __init__(self ,data):
            self.id=data['id']
            self.company=data['company']
            self.email=data['email']
            self.phone=data['phone']
            self.web_site=data['web_site']
            self.password=data['password']
            self.logo=data['data']
            self.description=data['description']
            self.unique_identifier=data['unique_identifier']
            self.activite_area=data['activite_area']
            self.created_at=data['created_at']
            self.updated_at=data['updated_at']

    @classmethod
    def add_company(cls ,data):
        query="INSERT INTO companies (company, email, phone, web_site, password, logo, description, unique_identifier, activite_area) Values ( %(company)s, %(email)s, %(phone)s, %(web_site)s, %(password)s, %(logo)s, %(description)s, %(unique_identifier)s, %(activite_area)s);"
        return connectToMySQL(cls.db_name).query_db(query,data)

            
    #  @classmethod
    # def add_show(cls ,data):
    #     query="INSERT INTO shows (user_id ,title , network , release_date , description) Values (%(user_id)s,%(title)s,%(network)s,%(release_date)s,%(description)s);"
    #     return connectToMySQL('tv_shows').query_db(query,data)
        
    # @classmethod
    # def get_all_shows(cls ):
    #     query="SELECT * FROM shows LEFT JOIN users on shows.user_id=shows.id GROUP BY shows.id;"
    #     results = connectToMySQL('tv_shows').query_db(query)
    #     all_shows = []
    #     for row in results:
    #         all_shows.append(cls(row))
    #     return all_shows


    # @classmethod
    # def get_show_id(cls ,data):
    #     query="SELECT  * FROM shows LEFT JOIN users on shows.user_id=users.id WHERE shows.id=%(id)s"
    #     result = connectToMySQL('tv_shows').query_db(query ,data)
 
    #     return cls(result[0])

    # @classmethod
    # def delete(cls ,data):
    #     query="DELETE FROM shows WHERE id=%(id)s"
    #     return connectToMySQL('tv_shows').query_db(query ,data)
 
    # @classmethod
    # def update(cls ,data):
    #     query="UPDATE shows SET title=%(title)s,network=%(network)s,release_date=%(release_date)s,description=%(description)s WHERE id=%(id)s"
    #     return connectToMySQL('tv_shows').query_db(query ,data)      

    # @staticmethod
    # def validate_show(show):
    #     is_valid = True

    #     if len(show['title']) < 3:
    #         flash("Tv show title must be at least 3 characters","show")
    #         is_valid= False
    #     if len(show['network']) < 3:
    #         flash("Network must be at least 3 characters","show")
    #         is_valid= False
    #     if len(show['release_date']) < 8:
    #         flash("Date must not be empty","show")
    #         is_valid= False
    #     if show['description'] == "":
    #         flash("description is empty","show")
    #     return is_valid