__author__ = 'gjacoby'

class User:
    user_id = None
    first_name = None
    last_name = None
    email = None
    login_name = None
    address = None

    def __init__(self):
        pass

    def __init__(self, dict):
        user_id = dict["userid"]
        first_name = dict["firstname"]
        last_name = dict["lastname"]
        email = dict["email"]
        loginname = dict["loginname"]
        address = dict["address"]

