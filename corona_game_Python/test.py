from flask_login import UserMixin
#############
from flask import Flask, render_template,redirect,request,flash,url_for,jsonify
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

# class FormDetails(db.Model):
#     __tablename__ = 'corona_user_data'

#     # id = db.Column(db.Integer, primary_key=True,  autoincrement=True)
#     name = db.Column(db.String(), unique=True, nullable=False)
#     email = db.Column(db.String(), primary_key=True)
#     phone = db.Column(db.String(20), nullable=False)
#     User_Message = db.Column(db.Unicode(), nullable=False)
#     Blood_Group_Type = db.Column(db.String(), nullable=False)
#     Corona_Survivor_Details = db.Column(db.String(), nullable=False)
#     Date_of_registration = db.Column(db.Date(), nullable=False)

#     def __init__(self, name, email,phone,User_Message,Blood_Group_Type,
#     Corona_Survivor_Details,
#     Date_of_registration):
#         self.name = name
#         self.email = email
#         self.phone = phone
#         self.User_Message = User_Message
#         self.Blood_Group_Type = Blood_Group_Type
#         self.Corona_Survivor_Details = Corona_Survivor_Details
#         self.Date_of_registration = Date_of_registration
        # self.id = id
           
    # def __repr__(self):
    #     return f"<Car {self.name}>"

    # def __repr__(self):
    #     return f"<Name {self.name}>"

# class ReusableForm(Form):
#     name = TextField('Name:', validators=[validators.required()])
#     email = TextField('Email:', validators=[validators.required()])
#     CS = TextField('Corona Survivor(Yes/No):', validators=[validators.required()])
#     BG = TextField('Blood Group:', validators=[validators.required()])
############################################################################################################
#Models
class User(UserMixin, db.Model):
    
    __tablename__ = 'corona_user_data'

    # id = db.Column(db.Integer, primary_key=True,  autoincrement=True)
    name = db.Column(db.String(), unique=True, nullable=False)
    email = db.Column(db.String(), primary_key=True)
    phone = db.Column(db.String(20), nullable=False)
    User_Message = db.Column(db.Unicode(), nullable=False)
    Blood_Group_Type = db.Column(db.String(), nullable=False)
    Corona_Survivor_Details = db.Column(db.String(), nullable=False)
    Date_of_registration = db.Column(db.Date(), nullable=False)
    # id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    # username = db.Column(db.String(15), unique=True, nullable=False)
    # email = db.Column(db.String(50), unique=True, nullable=False)
    # password = db.Column(db.String(120), unique=True, nullable=False)
    # created_on = db.Column(db.DateTime, server_default=db.func.now())
    # updated_on = db.Column(db.DateTime, server_default=db.func.now(), server_onupdate=db.func.now())
    # tasks = db.relationship('Task', backref='author', lazy='dynamic')

    @classmethod
    def is_user_name_taken(cls, name):
      return db.session.query(db.exists().where(User.name==name)).scalar()

    @classmethod
    def is_email_taken(cls, email):
      return db.session.query(db.exists().where(User.email==email)).scalar()

    def __repr__(self):
        return '<User %r>' % (self.name)

@app.route("/")
def home():
    
    return render_template('index.html')

#User Signup Api
@app.route('/post_user', methods=['POST'])
def post_user():

    if 'Name' not in request.json:
        return jsonify({'Name': 'must include name'})
    # if 'email' not in request.json:
    #     return jsonify({'email': 'must include email'})
    if 'Email' not in request.json:
        return jsonify({'Email' : 'must include email' })

    if User.is_user_name_taken(request.json['Name']):
         return jsonify({'Name': 'This username is already taken!'}), 409
    if User.is_email_taken(request.json['Email']):
         return jsonify({'Email': 'This email is already taken!'}), 409

    if request.json :
        # hashed_password = generate_password_hash(request.json['password'], method='sha256')
        new_user = User(name=request.json['Name'], email=request.json['Email'],phone=request.json['Phone'],User_Message=request.json['form_message'],Blood_Group_Type=request.json['Blood_Group'],Corona_Survivor_Details=request.json['Corona Survivor(Yes/No)'],Date_of_registration=request.json['Date'])
        db.session.add(new_user)
        db.session.commit()
        return jsonify({'user': 'user created successfully'}), 201
    return jsonify({'username': 'must include username', 
            'email' : 'must include email' })

@app.route("/appointment")
def appointment():
  
    # return render_template('login.html', message=message
    return render_template('appointment.html')

# @app.route("/sign_user", methods=['POST'])
# def sign_user():


   



@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/insight")
def insight():
    return render_template('insight.html')


@app.route("/submit.html")
def submit():
    
    return render_template('submit.html')


if __name__ == "__main__":
    app.run(debug=True) 




##########################################################################################
# @app.route('/')
# def home():
#     if not db.session['logged_in']:
#         return render_template('index.html')
#     else:
#         # return "Hello Boss!  <a href="/logout">Logout</a>"
#         return redirect(url_for('insight'))

# @app.route("/post_user",methods=['POST'])
# def post_user():
#     user = FormDetails(request.form['Name'],request.form['Email'],
#     request.form['Phone'],request.form['form_message'],
#     request.form['Blood Group'],request.form['Corona Survivor(Yes/No)'],
#     request.form['Date']
#     )
#     db.session.add(user)
#     db.session.commit()
#     return redirect(url_for('aappointment'))

# @app.route('/sign_user', methods=['POST'])
# def sign_user():

#     POST_USERNAME = str(request.form['Name'])
#     POST_EMAIL = str(request.form['Email'])

#     # Session = sessionmaker(bind=engine)
#     # s = Session()
#     query = db.session.query(FormDetails).filter(FormDetails.name.in_([POST_USERNAME]), FormDetails.email.in_([POST_EMAIL]) )
#     result = query.first()
#     if result:
#        db.session['logged_in'] = True
#     else:
#         flash('wrong password!')
#     return home()

# @app.route("/logout")
# def logout():
#     db.session['logged_in'] = False
#     return home()  

# if __name__ == "__main__":
#     app.run(debug=True) 