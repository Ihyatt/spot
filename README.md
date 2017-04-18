
# Spot

## Spot is an app that allows users to alert 911 of their location and emergency!

## Contents
* [Technologies Used](#technologiesused)
* [Features](#feautures)
* [Main Page](#main)
* [How to locally run Spot](#run)

### <a name="technologiesused"></a>Technologies Used

* [SQLAlchemy](http://www.sqlalchemy.org/)
* [PostgreSQL](https://www.postgresql.org/)
* [Python](https://www.python.org/)
* [Flask](http://flask.pocoo.org/)
* [Jinja](http://jinja.pocoo.org/)
* [Javascript](https://www.javascript.com/)
* [JQuery](https://jquery.com/)
* [Twilio API](https://www.twilio.com/?mkwid=so15S8OY0&pdv=c&pcrid=178300256561&pmt=e&pkw=twilio%20api&campaign=G_S_Brand_Alpha_NA&utm_source=google&utm_medium=cpc&utm_term=twilio+api&utm_campaign=G_S_Brand_Alpha_NA&utm_content=Brand&gclid=Cj0KEQjwicfHBRCh6KaMp4-asKgBEiQA8GH2x3wyqNz_PwY8NZiDdwfliPwG5LIQCPpNrGTZz5gkXkcaAi-U8P8HAQ)
* [Google Maps API](https://developers.google.com/maps/)
* [HTML/CSS](http://www.w3schools.com/html/html_css.asp)
* [Bootstrap](http://getbootstrap.com/)

### <a name="features"></a>Features

- [x] Personal information and emergency contact information repository
- [x] Google Maps grabs your geo location to send to 911
- [x] Twilio allows for fast text to 911. 

#### <a name="main"></a>Main Page
![spot](https://cloud.githubusercontent.com/assets/11432315/25067333/d790523c-21f4-11e7-8d23-825bbee77e44.gif)

#### <a name="run"></a>How to Run Spot Locally

##### General Setup
* Set up and activate a python virtualenv, and install all dependencies:
    * `pip install -r requirements.txt`
* Make sure you have PostgreSQL running. Create a new database named spot:
  * `createdb spot`
 * Create the tables in your database:
    * `python -i model.py`
 * Then seed database
   * `python seed.py`
 * Start up the flask server:
    * `python server.py`
 * Go to localhost:5000 to see the web app
