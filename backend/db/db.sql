CREATE TABLE USER(
	ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
	NAME TEXT UNIQUE
);

CREATE TABLE QUESTION(
	ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
	NAME TEXT,
	TYPE TEXT
);

CREATE TABLE OPTION(
	ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
	DESC TEXT,
	QUESTION_ID INTEGER,
	FOREIGN KEY(QUESTION_ID) REFERENCES QUESTION(ID) ON DELETE CASCADE
);

CREATE TABLE USERGROUP(
	ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
	NAME TEXT UNIQUE
);

CREATE TABLE JOINS(
	GROUP_ID INTEGER NOT NULL,
	USER_ID INTEGER NOT NULL,
	PRIMARY KEY(GROUP_ID, USER_ID)
);

CREATE TABLE RESPONSE(
	USER_ID INTEGER NOT NULL,
	QUESTION_ID INTEGER NOT NULL,
	OPTION_ID INTEGER NOT NULL,
	PRIMARY KEY(USER_ID, QUESTION_ID)
);