import sqlite3
import psycopg2
import random
import string

class Conn_postgres():
    conn = None
    cursor = None

    def __init__(self):
        self.open()

    def open(self):
        self.conn = psycopg2.connect(user = "webappuser",
                                    password = "mysecurepassword",
                                    host = "localhost",
                                    port = "5432",
                                    database = "website")
        self.cursor = self.conn.cursor()

    def close(self):
        self.conn.close()

    def isclosed(self):
        try:
            resultset = self.conn.closed
            if resultset == 1:
                return True
            else:
                return False
        except:
            return True

    def createTable(self, tablename, query):
        self.cursor.execute("DROP TABLE IF EXISTS " + tablename + "; " + query)
        self.conn.commit()

    def randPassword(self, length):
        letters = string.ascii_lowercase
        result_str = ''.join(random.choice(letters) for i in range(length))
        return result_str

    def setup(self):
        if self.isclosed():
            self.open()
            
        self.createTable('users', 'CREATE TABLE users (id SERIAL PRIMARY KEY, role TEXT NOT NULL, firstname TEXT, lastname TEXT, username TEXT NOT NULL, password TEXT NOT NULL);')
        self.cursor.execute("INSERT INTO users (role, firstname, lastname, username, password) VALUES ('admin','Super','User','admin','" + self.randPassword(16) + "');")
        self.conn.commit()
        self.close()

    def upsert(self, query):
        if self.isclosed():
            self.open()
        self.cursor.execute(query)
        self.conn.commit()

    def select(self, query):
        if self.isclosed():
            self.open()
        self.cursor.execute(query)
        data = self.cursor.fetchall()
        return data
