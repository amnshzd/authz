from flask_restful import Resource
from authz.controller.apiv1 import UserController

class UserResource(Resource):
    def get(self, user_id=None):
        """
        GET /users --> get list of users
        GET /users/<user_id> --> get user info
        """
        if user_id is None:
            return UserController.get_user_list()  # get list of users
        else:
            return UserController.get_user(user_id)  # get user info

    def post(self):
        """"
        POST /users --> create new user
        POST /users/<user_id> --> Not Allowed
        """
        return UserController.creat_user()  # Create User

    def patch(self, user_id):
        """"
        PATCH /users --> NOT Allowed
        PATCH /users --> Update user
        """
        return UserController.update_user(user_id)  # Update User

    def delete(self, user_id):
        """"
        DELETE /users --> Not Allowed
        DELETE /users/user_id --> Delete user
        """
        return UserController.delete_user(user_id)  # Delete User

