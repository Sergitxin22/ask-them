import sqlite3
from objects import *

def insert_user(db, name):
    cur = db.cursor()
    cur.execute("INSERT INTO USER(NAME) VALUES (?)", (name,))
    db.commit()
    cur.close()

def get_user(db, name):
    cur = db.cursor()
    cur.execute("SELECT * FROM USER WHERE NAME = ?", (name,))
    row = cur.fetchone()
    cur.close()
    return User(row[0], row[1])

def get_user_by_id(db, id):
    cur = db.cursor()
    cur.execute("SELECT * FROM USER WHERE ID = ?", (id,))
    row = cur.fetchone()
    cur.close()
    return User(row[0], row[1])

def insert_option(db, desc, question_id):
    cur = db.cursor()
    cur.execute("INSERT INTO OPTION(DESC, QUESTION_ID) VALUES (?, ?)", (desc, question_id,))
    db.commit()
    cur.close()

def get_options(db, question_id):
    cur = db.cursor()
    cur.execute("SELECT * FROM OPTION WHERE QUESTION_ID = ?", (question_id,))
    rows = cur.fetchall()
    cur.close()

    options = []
    for row in rows:
        options.append(Option(row[0], row[1], row[2]))
    
    return options

def insert_question(db, name, type):
    cur = db.cursor()
    cur.execute("INSERT INTO QUESTION(NAME, TYPE) VALUES (?, ?)", (name, type,))
    db.commit()
    cur.close()

def get_question(db, name):
    cur = db.cursor()
    cur.execute("SELECT * FROM QUESTION WHERE NAME = ?", (name,))
    row = cur.fetchone()
    cur.close()

    options = get_options(db, row[0])
    return Question(row[0], row[1], row[2], options)

def insert_response(db, user_id, question_id, option_id):
    cur = db.cursor()
    cur.execute("INSERT INTO RESPONSE VALUES (?, ?, ?)", (user_id, question_id, option_id,))
    db.commit()
    cur.close()

def get_respose_option(db, user_id, question_id):
    cur = db.cursor()
    cur.execute("SELECT * FROM RESPONSE WHERE QUESTION_ID = ? AND USER_ID = ?", (question_id, user_id,))
    row = cur.fetchone()
    cur.close()
    return Response(row[0], row[1], row[2])

def get_all_responses(db, question_id):
    cur = db.cursor()
    cur.execute("SELECT * FROM RESPONSE WHERE QUESTION_ID = ?", (question_id,))
    rows = cur.fetchall()
    cur.close()

    responses = []
    for row in rows:
        responses.append(Response(row[0], row[1], row[2]))

    return responses

def create_usergroup(db, name):
    cur = db.cursor()
    cur.execute("INSERT INTO USERGROUP(NAME) VALUES (?)", (name,))
    db.commit()
    cur.close()

def add_user_to_usergroup(db, group_id, user_id):
    cur = db.cursor()
    cur.execute("INSERT INTO JOINS VALUES (?, ?)", (group_id, user_id,))
    db.commit()
    cur.close()

def get_usergroup_id(db, name):
    cur = db.cursor()
    cur.execute("SELECT ID FROM USERGROUP WHERE NAME = ?", (name,))
    row = cur.fetchone()
    return row[0]

def get_usergroup(db, name):
    cur = db.cursor()
    cur.execute("SELECT * FROM USERGROUP WHERE NAME = ?", (name,))
    group_row = cur.fetchone()
    id = get_usergroup_id(db, name)
    cur.execute("SELECT * FROM JOINS WHERE GROUP_ID = ?", (id,))
    rows = cur.fetchall()
    cur.close()

    users = []
    for row in rows:
        user = get_user_by_id(db, row[1])
        users.append(user)

    return UserGroup(group_row[0], group_row[1], users)
