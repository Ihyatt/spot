"""Utility file to seed spot database"""


from sqlalchemy import func
import json
from model import User, Contact, connect_to_db, db
from server import app

def seed_spot():
	"""info into database"""



	user = User(first="Becky", last="James", phone="4085551234", latitude = 1.0, longitude = 1.0)
	contact = Contact(contact_first = "Jenny", contact_last= "Jake", contact_phone="4085550987")
			
	db.session.add(user)
	db.session.add(contact)
	db.session.commit()





if __name__ == "__main__":
    connect_to_db(app)
    print seed_spot()