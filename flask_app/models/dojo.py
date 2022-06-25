from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models.ninja import Ninja

class Dojo:
    def __init__(self,data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.ninjas = []

    @classmethod
    def get_dojo(cls,data):
        print('B'*50)
        print(data)
        query = '''
                SELECT * FROM dojos 
                LEFT JOIN ninjas 
                ON dojos.id = ninjas.dojo_id 
                WHERE dojos.id=%(dojo_id)s;
                '''
        result = connectToMySQL('dojos_and_ninjas').query_db(query,data)
        print("result[0] = ",result)
        dojo = cls(result[0])
        print("dojo.ninjas = ",dojo.ninjas,)
        for row in result:
            data = {
                "id":row["ninjas.id"]
            }
            print(data)
            if data['id']:
                ninja = Ninja.get_ninja(data)
                dojo.ninjas.append(ninja)
                print(ninja.first_name,ninja.last_name)
        return dojo

    @classmethod
    def get_all_dojos(cls):
        query = 'SELECT * FROM dojos;'
        results = connectToMySQL('dojos_and_ninjas').query_db(query)
        dojos = []
        for row in results:
            dojos.append(cls(row))
        return dojos

    @classmethod
    def save_dojo(cls,data):
        query = """
                INSERT INTO dojos (name)
                VALUES (%(name)s)
                """
        return connectToMySQL('dojos_and_ninjas').query_db(query,data)

# FINSH BUILDING BELOW LATER

    # @classmethod
    # def delete(cls,data):
    #     query = 'DELETE FROM users WHERE id=%(id)s;'
    #     connectToMySQL('dojos_and_ninjas').query_db(query,data)

    # @classmethod
    # def update(cls,data):
    #     query = """
    #             UPDATE users 
    #             SET first_name=%(first_name)s, last_name=%(last_name)s, email=%(email)s 
    #             WHERE id=%(id)s;
    #             """
    #     connectToMySQL('dojos_and_ninjas').query_db(query,data)
 
