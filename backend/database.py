import sqlite3
from objects import *


def insert_user(db: sqlite3.Connection, name: str):
    try:
        cur = db.cursor()
        cur.execute("INSERT INTO USER(NAME) VALUES (?)", (name,))
        db.commit()
        print(f"User {name} inserted correctly")

    except sqlite3.DatabaseError as e:
        print(f"Error querying database: {e}")
    finally:
        cur.close()


def get_user(db: sqlite3.Connection, name: str) -> User:
    try:
        cur = db.cursor()
        cur.execute("SELECT * FROM USER WHERE NAME = ?", (name,))
        row = cur.fetchone()

        if row is None:
            return None
        return User(row[0], row[1])
    
    except sqlite3.DatabaseError as e:
        print(f"Error querying database: {e}")
        return None
    finally:
        cur.close()


def get_user(db: sqlite3.Connection, id: int) -> User:
    try:
        cur = db.cursor()
        cur.execute("SELECT * FROM USER WHERE ID = ?", (id,))
        row = cur.fetchone()

        if row is None:
            return None
        return User(row[0], row[1])
    
    except sqlite3.DatabaseError as e:
        print(f"Error querying database: {e}")
        return None
    finally:
        cur.close()


def insert_option(db: sqlite3.Connection, desc: str, question_id: int):
    try:
        cur = db.cursor()
        cur.execute("INSERT INTO OPTION(DESC, QUESTION_ID) VALUES (?, ?)", (desc, question_id,))
        db.commit()
        print(f"Option {desc} inserted correctly")

    except sqlite3.DatabaseError as e:
        print(f"Error querying database: {e}")
    finally:
        cur.close()


def get_options(db: sqlite3.Connection, question_id: int) -> list[Option]:
    try:

        cur = db.cursor()
        cur.execute("SELECT * FROM OPTION WHERE QUESTION_ID = ?", (question_id,))
        rows = cur.fetchall()
        options = []
        for row in rows:
            options.append(Option(row[0], row[1], row[2]))
        
        return options
     
    except sqlite3.DatabaseError as e:
        print(f"Error querying database: {e}")
        return []
    finally:
        cur.close()


def insert_question(db: sqlite3.Connection, name: str, type: str):
    try:
        cur = db.cursor()
        cur.execute("INSERT INTO QUESTION(NAME, TYPE) VALUES (?, ?)", (name, type,))
        db.commit()
        print(f"Question {name} inserted correctly")
    
    except sqlite3.DatabaseError as e:
        print(f"Error querying database: {e}")
    finally:
        cur.close()


def get_question(db: sqlite3.Connection, name: str) -> Question:
    try:
        cur = db.cursor()
        cur.execute("SELECT * FROM QUESTION WHERE NAME = ?", (name,))
        row = cur.fetchone()

        if row is None:
            return None
        options = get_options(db, row[0])
        return Question(row[0], row[1], row[2], options)
    
    except sqlite3.DatabaseError as e:
        print(f"Error querying database: {e}")
        return None
    finally:
        cur.close()


def insert_response(db: sqlite3.Connection, user_id: int, question_id: int, option_id: int):
    try:
        cur = db.cursor()
        cur.execute("INSERT INTO RESPONSE VALUES (?, ?, ?)", (user_id, question_id, option_id,))
        db.commit()
        print(f"Response with option ID {option_id} inserted correctly")
    
    except sqlite3.DatabaseError as e:
        print(f"Error querying database: {e}")
    finally:
        cur.close()


def get_respose_option(db: sqlite3.Connection, user_id: int, question_id: int) -> Response:
    try:
        cur = db.cursor()
        cur.execute("SELECT * FROM RESPONSE WHERE QUESTION_ID = ? AND USER_ID = ?", (question_id, user_id,))
        row = cur.fetchone()

        if row is None:
            return None
        return Response(row[0], row[1], row[2])
    
    except sqlite3.DatabaseError as e:
        print(f"Error querying database: {e}")
        return None
    finally:
        cur.close()


def get_all_responses(db: sqlite3.Connection, question_id: int) -> list[Response]:
    try:
        cur = db.cursor()
        cur.execute("SELECT * FROM RESPONSE WHERE QUESTION_ID = ?", (question_id,))
        rows = cur.fetchall()

        responses = []
        for row in rows:
            responses.append(Response(row[0], row[1], row[2]))

        return responses

    except sqlite3.DatabaseError as e:
        print(f"Error querying database: {e}")
        return []
    finally:
        cur.close()


def create_usergroup(db: sqlite3.Connection, name: str):
    try:
        cur = db.cursor()
        cur.execute("INSERT INTO USERGROUP(NAME) VALUES (?)", (name,))
        db.commit()
    
    except sqlite3.DatabaseError as e:
        print(f"Error querying database: {e}")
    finally:
        cur.close()


def add_user_to_usergroup(db: sqlite3.Connection, group_id: int, user_id: int):
    try:
        cur = db.cursor()
        cur.execute("INSERT INTO JOINS VALUES (?, ?)", (group_id, user_id,))
        db.commit()
        print(f"User with ID {user_id} added to group with ID {group_id} added correctly")
    
    except sqlite3.DatabaseError as e:
        print(f"Error querying database: {e}")
    finally:
        cur.close()


def get_usergroup_id(db: sqlite3.Connection, name: str) -> int:
    try:
        cur = db.cursor()
        cur.execute("SELECT ID FROM USERGROUP WHERE NAME = ?", (name,))
        row = cur.fetchone()
        if row is None:
            return None
        return row[0]
    
    except sqlite3.DatabaseError as e:
        print(f"Error querying database: {e}")
        return None
    finally:
        cur.close()


def get_usergroup(db: sqlite3.Connection, name: str) -> UserGroup:
    try:
        cur = db.cursor()
        cur.execute("SELECT * FROM USERGROUP WHERE NAME = ?", (name,))
        group_row = cur.fetchone()

        if group_row is None:
            return None
        
        id = get_usergroup_id(db, name)
        cur.execute("SELECT * FROM JOINS WHERE GROUP_ID = ?", (id,))
        rows = cur.fetchall()

        users = []
        for row in rows:
            user = get_user(db, row[1])
            users.append(user)

        return UserGroup(group_row[0], group_row[1], users)
    
    except sqlite3.DatabaseError as e:
        print(f"Error querying database: {e}")
        return None
    finally:
        cur.close()
