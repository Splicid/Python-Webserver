from flask import Flask, render_template, request
from flask.helpers import url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
# Initialize the database
db = SQLAlchemy(app)

#Create db model
class Friends(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)
# Create a function to return a string
    def _repr_(self):
        return '<Name %r>' % self.id

#Webpage Routes
@app.route('/')
def index():
    title = "Database Book"
    name = ["Luis", "John", "Sid"]
    return render_template("./index.html", title=title, name=name)

@app.route('/about')
def about():
    name = ["Luis", "John", "Sid"]
    return render_template("./about.html", name=name)

