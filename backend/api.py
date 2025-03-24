from fastapi import FastAPI
from database import *

app = FastAPI()

@app.get("/")
async def root():
   return {"message": "askthem"}


@app.get("home/users/{name}")
async def query_get_user(name: str):
   db = sqlite3.connect("db/database.db")
   user = get_user(db, name)
   db.close()
   return {"user": user}


@app.get("home/users/")
async def query_get_all_users():
   db = sqlite3.connect("db/database.db")
   users = get_all_users(db)
   db.close()
   return {"users": users}


@app.get("home/questions/{id}")
async def query_get_question(id: int):
   db = sqlite3.connect("db/database.db")
   question = get_question_by_id(db, id)
   db.close()
   return {"question": question}


@app.get("home/groups/{name}")
async def query_get_usergroup(name: str):
   db = sqlite3.connect("db/database.db")
   usergroup = get_usergroup(db, name)
   db.close()
   return {"group": usergroup}


@app.get("home/groups/byUserName/{name}")
async def query_get_user_usergroups(name: str):
   db = sqlite3.connect("db/database.db")
   usergroup = get_user_usergroups(db, name)
   db.close()
   return {"group": usergroup}
