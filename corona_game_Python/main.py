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
    # form = ReusableForm(request.form)

    # print(form.errors)
    # if request.method == 'POST':
    #     name=request.form['Name']
    #     email = request.form['Email']
    #     phone = request.form['Phone']
    #     date = request.form['Date']
    #     BG = request.form['Blood Group']
    #     CS = request.form['Corona Survivor(Yes/No)']
    #     message = request.form['form_message']
    #     print(name,email,phone,date,message,BG,CS,message)
        # if request.is_json:
        #     data = request.get_json()
        # new_data = FormDetails(name=name, email=email,phone=phone,Date_of_registration=date,Blood_Group_Type=BG,Corona_Survivor_Details=CS,User_Message=message)
        # db.session.add(new_data)
        # db.session.commit()
        # return {"message": f"car {new_data.name} has been created successfully."}
        # else:
        #     return {"Unsuccessfull!!"}

    # elif request.method == 'GET':
    #     user_details = FormDetails.query.all()
    #     results = [
    #         {
    #             "name": user_detail.name,
    #             "email": user_detail.email,
    #         } for user_detail in user_details]

    #     return {"count": len(results), "User Data": results}



    

    # if form.validate():
    #     # Save the comment here.
    #     flash('Thanks for registration ' + name)
    # else:
    #     flash('All the form fields are required. ')
    
    # # return render_template('hello.html', form=form)
    return render_template('index.html')

@app.route("/post_user",methods=['POST'])
def post_user():
    user = FormDetails(request.form['Name'],request.form['Email'],
    request.form['Phone'],request.form['form_message'],
    request.form['Blood Group'],request.form['Corona Survivor(Yes/No)'],
    request.form['Date']
    )
    db.session.add(user)
    db.session.commit()
    return redirect(url_for('home'))

@app.route("/submit.html",methods=['POST'])
def sign_user():
    message = ''
    print("in sign_user")
    print(request.method)
    if request.method == 'POST':

        username = request.form.get('Name')  # access the data inside 
        email_form = request.form.get('Email')

        lst = FormDetails.query.filter(FormDetails.name==username).filter(FormDetails.email == email_form).all()
        if not lst:
            # return redirect(url_for('appointment'))
            flash("Wrong username or password")
            return render_template('appointment.html') 
        else:
            print(lst)
            message = "Correct username and password"
            return render_template('submit.html',message=message)

@app.route("/appointment")
def appointment():
  
    # return render_template('login.html', message=message
    return render_template('appointment.html')
    
   
    
@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/insight")
def insight():
    return render_template('insight.html')


@app.route("/submit.html")
def submit():
    
    return render_template('submit.html')

# @app.route("/home")
# def Session():
#     import game
#     return game_start()
   

if __name__ == "__main__":
    app.run(debug=True)

# $ export FLASK_APP=app.py
# $ flask run
