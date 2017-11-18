# hello_db.py

import os

from flask import Flask
from flask_script import Manager
from flask_sqlalchemy import SQLAlchemy
#from flask.ext.sqlalchemy import SQLAlchemy


basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
manager = Manager(app)
app.config["SQLALCHEMY_DATABASE_URI"] =\
    "sqlite:///" + os.path.join(basedir, "data.sqlite")
app.config["SQLAlCHEMY_COMMIT_ON_TEARDOWN"] = True
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_ECHO"] = True

db = SQLAlchemy(app)

###### Single ForeignKey ######
"""
class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    #users = db.relationship('User') # relationship (from Role link to User)
    users = db.relationship('User', backref='role')

    def __repr__(self):
        return '<Role %r>' % self.name


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, index=True)
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))
    #role = db.relationship('Role') # relationship (from User link to Role)

    def __repr__(self):
        return '<User %r>' % self.username
"""
###############################

##### Multiple ForeignKeys #####

class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)

    #users_primary_role = db.relationship('User', primaryjoin='Role.id==User.primary_role_id')
    #users_secondary_role = db.relationship('User', primaryjoin='Role.id==User.secondary_role_id')
    users_primary_role = db.relationship('User', backref='primary_role', primaryjoin='Role.id==User.primary_role_id')
    users_secondary_role = db.relationship('User', backref='secondary_role', primaryjoin='Role.id==User.secondary_role_id')

    def __repr__(self):
        return '<Role %r>' % self.name


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, index=True)
    primary_role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))
    secondary_role_id =  db.Column(db.Integer, db.ForeignKey('roles.id'))

    #primary_role = db.relationship('Role', foreign_keys='User.primary_role_id')
    #secondary_role = db.relationship('Role', foreign_keys='User.secondary_role_id')

    def __repr__(self):
        return '<User %r>' % self.username

################################

if __name__ == '__main__':
    manager.run()
