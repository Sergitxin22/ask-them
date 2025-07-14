class User:
    def __init__(self, id, name, passwd, coins):
        self.id = id
        self.name = name
        self.passwd = passwd
        self.coins = coins

class UserGroup:
    def __init__(self, id, name, users):
        self.id = id
        self.name = name
        self.users = users

class Using_Question:
    def __init__(self, id, groupId, questionId, date):
        self.id = id
        self.groupId = groupId
        self.questionId = questionId 
        self.date = date

class Question:
    def __init__(self, id, question, type):
        self.id = id
        self.question = question
        self.type = type

class Response:
    def __init__(self, user_id, question_id, responseid, usersSelected, date):
        self.id = id
        self.user_id = user_id
        self.question_id = question_id
        self.responseid = responseid
        self.usersSelected = usersSelected
        self.date = date

