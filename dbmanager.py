from flask import jsonify
from main import app
from types import NoneType

import sqlite3

class DBManager:
    dbfile = ""
    def __init__(self, dbfile: str):
        self.dbfile = dbfile

    def get_connection(self):
        db = sqlite3.connect(self.dbfile)
        db.row_factory = sqlite3.Row
        return db
    
    def read_sql_file(self, filepath: str):
        db = self.get_connection()
        with app.open_resource(filepath, mode='r') as sql:
            db.cursor().executescript(sql.read()) 
        db.commit()

    def get_all(self, tablename: str):
        try:
            db = self.get_connection()
            cursor = db.cursor()
            cursor.execute("SELECT * FROM " + tablename)
            response = cursor.fetchall()
            return jsonify([dict(row) for row in response])  
        except sqlite3.Error as error:
            return jsonify({'error': str(error)}), 500   
        finally:
            db.close()

    def get_by_id(self, tablename: str, value: str, id_column: str = "id"):
        try:
           db = self.get_connection()
           cursor = db.cursor()
           cursor.execute("SELECT * FROM " + tablename + " WHERE " + id_column + " = " + value) 
           response = cursor.fetchone()
           return jsonify(dict(response or [])) 
        except sqlite3.Error as error:
            return jsonify({'error': str(error)}), 500
        finally:
            db.close()
        


