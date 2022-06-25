from flask_app.config.mysqlconnection import connectToMySQL

class Ninja:
    def __init__(self,data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.age = data['age']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.dojo_id = data['dojo_id']

    @classmethod
    def get_ninja(cls,data):
        query = 'SELECT * FROM ninjas WHERE id=%(id)s;'
        result = connectToMySQL('dojos_and_ninjas').query_db(query,data)
        # print("result[0] = ",result[0])
        user = cls(result[0])
        return user

    # @classmethod
    # def get_all(cls):
    #     query = 'SELECT * FROM users;'
    #     results = connectToMySQL('dojos_and_ninjas').query_db(query)
    #     users = []
    #     for user in results:
    #         users.append(cls(user))
    #     return users

    @classmethod
    def save_ninja(cls,data):
        query = """
                INSERT INTO ninjas (dojo_id,first_name, last_name, age)
                VALUES (%(dojo_id)s,%(first_name)s,%(last_name)s,%(age)s)
                """
        return connectToMySQL('dojos_and_ninjas').query_db(query,data)

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
 
