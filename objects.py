class User:
    def __init__(self, id, name):
        self.id = id
        self.name = name

class UserGroup:
    def __init__(self, id, name, users):
        self.id = id
        self.name = name
        self.users = users

class Question:
    def __init__(self, id, name, type, options):
        self.id = id
        self.name = name
        self.type = type
        self.options = options

class Option:
    def __init__(self, id, name, question_id):
        self.id = id
        self.name = name
        self.question_id = question_id

class Response:
    def __init__(self, user_id, question_id, option_id):
        self.id = id
        self.user_id = user_id
        self.question_id = question_id
        self.option_id = option_id
