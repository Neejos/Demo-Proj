from flask import Flask, render_template,redirect,request,flash,url_for,send_from_directory
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

@app.route("/profile.html",methods=['POST'])
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

            phone_num = FormDetails.query.with_entities(FormDetails.phone).filter(FormDetails.name==username).filter(FormDetails.email == email_form).first()
        
            Corona_surv = FormDetails.query.with_entities(FormDetails.Corona_Survivor_Details).filter(FormDetails.name==username).filter(FormDetails.email == email_form).first()
            Blood_Type = FormDetails.query.with_entities(FormDetails.Blood_Group_Type).filter(FormDetails.name==username).filter(FormDetails.email == email_form).first()
            # Corona_Survivor = FormDetails.query.filter(FormDetails.name==username)..filter(FormDetails.email == email_form).
            return render_template('profile.html',message=message,username=username,email_form=email_form,phone_num=phone_num ,Corona_surv=Corona_surv,Blood_Type=Blood_Type)

@app.route("/appointment")
def appointment():
  
    # return render_template('login.html', message=message
    return render_template('appointment.html')

# def allowed_file(filename):
#     return '.' in filename and \
#            filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS
           
@app.route('/profile')
def profile():

    return render_template('profile.html')
# @app.route('/show/<filename>')
# def uploaded_file(filename):
#         filename = 'http://127.0.0.1:5000/uploads/' + filename
#     return render_template('profile.html', filename=filename)

# @app.route('/uploads/<filename>')
# def send_file(filename):
#     path = UPLOAD_FOLDER + "/" + filename
#     return send_from_directory(UPLOAD_FOLDER, filename)
    
@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/insight")
def insight():
    return render_template('insight.html')


@app.route("/submit.html")
def submit():
    
    return render_template('submit.html')

@app.route("/contact")
def contact():
    
    return render_template('contact.html')

@app.route("/blog")
def blog():
    
    return render_template('blog.html')
    
# @app.route("/profile")
# def profile():
    
#     return render_template('profile.html')

@app.route("/remedies")
def remedies():
    
    return render_template('remedies.html')

@app.route("/diabetes")
def diabetes():
    
    return render_template('diabetes.html')
@app.route("/hangover")
def hangover():
    
    return render_template('hangover.html')

@app.route("/stress")
def stress():
    
    return render_template('stress.html')

# @app.route("/fitness")
# def fitness():
    
#     return render_template('fitness.html')

@app.route("/fitness1")
def fitness1():
    
    return render_template('fitness1.html')

@app.route("/fitness2")
def fitness2():
    return render_template('fitness2.html')

@app.route("/fitness3")
def fitness3():
    return render_template('fitness3.html')

@app.route("/fitness4")
def fitness4():
    return render_template('fitness4.html')   

    
@app.route("/officestress")
def officestress():
    
    return render_template('officestress.html')
@app.route("/immunitysyrup")
def immunitysyrup():
    
    return render_template('immunitysyrup.html')



# @app.route("/home")
# def Session():
#     import game
#     return game_start()
   

if __name__ == "__main__":
    app.run(debug=True)

# $ export FLASK_APP=app.py
# $ flask run
