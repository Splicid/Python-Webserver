from flask import Flask, render_template, request, redirect
from werkzeug.wrappers import Request, Response
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
@app.route('/data', methods=['POST', 'GET'])
def data():
    title = "Database Book"

    if request.method == "POST":
        friend_name = request.form['name']
        new_friend = Friends(name=friend_name)
        #push
        try:
            db.session.add(new_friend)
            db.session.commit()
            return redirect('/data')
        except:
            return "There was an error adding to database"
    else:
        friends = Friends.query.order_by(Friends.date_created)
        return render_template("data.html", title=title, friends=friends)

@app.route('/update/<int:id>', methods=['POST', 'GET'])
def update(id):
    friend_to_update = Friends.query.get_or_404(id)
    if request.method == "POST":
        friend_to_update.name = request.form['name']
        try:
            db.session.commit()
            return redirect('/data')
        except:
            return "There was a problem updating the database"
    else:
        return render_template('update.html',friend_to_update=friend_to_update)



@app.route('/')
def index():
    title = "Database Book"
    return render_template("index.html", title=title)

@app.route('/about')
def about():
    name = ["Luis", "John", "Sid"]
    return render_template("./about.html", name=name)

