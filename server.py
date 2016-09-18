"""Spot server : ) """


import os
from jinja2 import StrictUndefined
import twilio.twiml


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

@app.route("/", methods=['GET', 'POST'])
def hello_monkey():
    """Respond to incoming calls with a simple text message."""

    resp = twilio.twiml.Response()
    resp.message("Hello, Mobile Monkey")
    return str(resp)




if __name__ == "__main__":

	app.debug = True
	connect_to_db(app)
	# Use the DebugToolbar
	DebugToolbarExtension(app)
	app.run()