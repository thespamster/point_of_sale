"""
 this file is the main entry point for the application. 
 creates the flask application and the database object.
 also imports the routes module from the pointofsale package.
"""

import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
if os.path.exists("env.py"):
    import env


app = Flask(__name__)
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY")
if os.environ.get("DEVELOPMENT") == "True":
     app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DB_URL")
else:
     uri = os.environ.get("DATABASE_URL")
     if uri.startswith("postgres://"):
         uri = uri.replace("postgres://", "postgresql://", 1)
     app.config["SQLALCHEMY_DATABASE_URI"] = uri


db = SQLAlchemy(app)
from pointofsale import routes


