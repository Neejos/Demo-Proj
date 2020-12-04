from flask import Flask, render_template,redirect,request,flash
from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
# from flex import app,event,ui
# app.init()
# Create an instance of Flask app
app= Flask(__name__,static_url_path='/static')
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:postgres@localhost:5432/Corona_Hit"
db = SQLAlchemy(app)
migrate = Migrate(app, db)
app.config.from_object(__name__)
app.config['SECRET_KEY'] = '7d441f27d441f27567d441f2b6176a'

class FormDetails(db.Model):
    __tablename__ = 'corona_user_data'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    email = db.Column(db.String())
    phone = db.Column(db.Integer())
    message = db.column(db.String())
    BG = db.column(db.String())
    CS = db.column(db.String())
    Date = db.column(db.Date())



    # def __repr__(self):
    #     return f"<Name {self.name}>"

class ReusableForm(Form):
    name = TextField('Name:', validators=[validators.required()])
    email = TextField('Email:', validators=[validators.required()])
    CS = TextField('Corona Survivor(Yes/No):', validators=[validators.required()])
    BG = TextField('Blood Group:', validators=[validators.required()])
@app.route("/", methods=['GET', 'POST'])
def home():
    form = ReusableForm(request.form)

    print(form.errors)
    if request.method == 'POST':
        name=request.form['Name']
        email = request.form['Email']
        phone = request.form['Phone']
        date = request.form['Date']
        BG = request.form['Blood Group']
        CS = request.form['Corona Survivor(Yes/No)']
        message = request.form['form_message']
        print(name,email,phone,date,message,BG,CS,message)

    def __init__(self, name, email,phone,message,BG,CS,Date):
        self.name = name
        self.email = email
        self.phone = phone
        self.message = message
        self.BG = BG
        self.CS = CS
        self.Date = Date
        self.id = id
    def __repr__(self):
        return f"<Car {self.name}>"

    

    if form.validate():
        # Save the comment here.
        flash('Hello ' + name)
    else:
        flash('All the form fields are required. ')
    
    # return render_template('hello.html', form=form)
    return render_template('index.html')

@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/insight")
def insight():
    return render_template('insight.html')

@app.route("/appointment")
def appointment():
    return render_template('appointment.html')

@app.route("/submit.html")
def submit():
    
    return render_template('submit.html')

# @app.route("/home")
# def Session():
#     import game
#     return game_start()
   

if __name__ == "__main__":
    app.run(debug=True)


