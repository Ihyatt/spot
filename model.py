"""Database for Spot"""

from flask_sqlalchemy import SQLAlchemy
import os

db = SQLAlchemy()


#Model definitions 
##############################################################################

class User(db.Model):
	"""User info"""

	__tablename__ = "users"

	user_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
	first = db.Column(db.String(64), nullable=True)
	last = db.Column(db.String(64), nullable=True)
	phone = db.Column(db.String(20), nullable=True)
	latitude = db.Column(db.Float, nullable=True)
	longitude = db.Column(db.Float, nullable=True)


##############################################################################

class Contact(db.Model):
	"""users contact"""
	__tablename__ = "contacts"

	contact_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
	user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))
	contact_first = db.Column(db.String(64), nullable=True)
	contact_last = db.Column(db.String(64), nullable=True)
	contact_phone = db.Column(db.String(20), nullable=True)

	user = db.relationship('User', backref=db.backref("contacts"))


##############################################################################

 #Helper functions

def connect_to_db(app, db_uri=None):
	"""Connect the database to our Flask app."""

	# Configure to use our PstgreSQL database
	app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///spot'
	db.app = app
	db.init_app(app)

if __name__ == "__main__":
	# As a convenience, if we run this module interactively, it will leave
	# you in a state of being able to work with the database directly.

	from server import app
	connect_to_db(app)
	print "Connected to DB."
	db.create_all()
	

