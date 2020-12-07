from flask import Flask
from flask import Flask, flash, redirect, render_template, request, session, abort
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
# from tabledef import *
engine = create_engine('postgresql://postgres:postgres@localhost:5432/Corona_Hit')

from flask import Flask, render_template,redirect,request,flash,url_for
from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
# from flex import app,event,ui
# app.init()
# Create an instance of Flask app
app= Flask(__name__,static_url_path='/static')
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:postgres@localhost:5432/Corona_Hit"
app.debug=True
db = SQLAlchemy(app)
# migrate = Migrate(app, db)
app.config.from_object(__name__)
app.config['SECRET_KEY'] = '7d441f27d441f27567d441f2b6176a'

class FormDetails(db.Model):
    __tablename__ = 'corona_user_data'

    # id = db.Column(db.Integer, primary_key=True,  autoincrement=True)
    name = db.Column(db.String(), unique=True, nullable=False)
    email = db.Column(db.String(), primary_key=True)
    phone = db.Column(db.String(20), nullable=False)
    User_Message = db.Column(db.Unicode(), nullable=False)
    Blood_Group_Type = db.Column(db.String(), nullable=False)
    Corona_Survivor_Details = db.Column(db.String(), nullable=False)
    Date_of_registration = db.Column(db.Date(), nullable=False)

    def __init__(self, name, email,phone,User_Message,Blood_Group_Type,
    Corona_Survivor_Details,
    Date_of_registration):
        self.name = name
        self.email = email
        self.phone = phone
        self.User_Message = User_Message
        self.Blood_Group_Type = Blood_Group_Type
        self.Corona_Survivor_Details = Corona_Survivor_Details
        self.Date_of_registration = Date_of_registration
        # self.id = id
           
    # def __repr__(self):
    #     return f"<Car {self.name}>"

    # def __repr__(self):
    #     return f"<Name {self.name}>"

class ReusableForm(Form):
    name = TextField('Name:', validators=[validators.required()])
    email = TextField('Email:', validators=[validators.required()])
    CS = TextField('Corona Survivor(Yes/No):', validators=[validators.required()])
    BG = TextField('Blood Group:', validators=[validators.required()])

@app.route("/")
def home():
    
    return render_template('index.html')

@app.route("/appointment")
def appointment():
  
    # return render_template('login.html', message=message
    return render_template('appointment.html')

@app.route("/post_user",methods=['GET','POST'])
def post_user():
    user = FormDetails(request.form['Name'],request.form['Email'],
    request.form['Phone'],request.form['form_message'],
    request.form['Blood Group'],request.form['Corona Survivor(Yes/No)'],
    request.form['Date']
    )
    db.session.add(user)
    db.session.commit()
    return redirect(url_for('appointment'))

# @app.route('/')
# def home():
#     if not session.get('logged_in'):
#         return render_template('index.html')
#     else:
#         # return "Hello Boss!  <a href="/logout">Logout</a>"
#         return render_template('gallery.html')

@app.route('/sign_user', methods=['GET','POST'])
def sign_user():
    if request.method == 'POST':
        POST_USERNAME = str(request.form['Name'])
        POST_Email = str(request.form['Email'])
        print(POST_USERNAME,POST_Email)
        if request.method == 'GET':
            Session = sessionmaker(bind=engine)
            s = Session()
            query = s.query(FormDetails).filter(FormDetails.name.in_([POST_USERNAME]), FormDetails.password.in_([POST_Email]) )
            result = query.first()
            print(result)
        if result:
            session['logged_in'] = True
            return render_template('index.html')
        else:
            flash('wrong password!')
            return insight()

@app.route("/logout")
def logout():
    session['logged_in'] = False
    return home()

@app.route("/insight")
def insight():
    return render_template('insight.html')

if __name__ == "__main__":
# app.secret_key = os.urandom(12)
    app.run(debug=True)