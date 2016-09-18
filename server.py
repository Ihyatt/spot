"""Spot server : ) """


import os
from jinja2 import StrictUndefined
import twilio.twiml
import send_sms


from flask import Flask, render_template, redirect, request, flash, jsonify
from flask_debugtoolbar import DebugToolbarExtension

from model import User, Contact, connect_to_db, db


app = Flask(__name__)


app.config['TEMPLATES_AUTO_RELOAD'] = True

app.secret_key = "19kittiesareawesome89"

app.jinja_env.undefined = StrictUndefined

@app.route('/')
def localhost():

	user = User.query.get(1)


	return render_template("home.html", user=user)

@app.route('/sendmessage', methods=['POST'])
def message():
    """sends message"""
    
    m = request.form.get("emergency")
    lat = request.form.get("lat")
    lng = request.form.get("lng")
    body = "my emergency is: " + m + " my location is:" + str(lat) + " " + str(lng)

    print body

    send_sms.send_message(body)

    return "done"



if __name__ == "__main__":

	app.debug = True
	connect_to_db(app)
	# Use the DebugToolbar
	DebugToolbarExtension(app)
	app.run()