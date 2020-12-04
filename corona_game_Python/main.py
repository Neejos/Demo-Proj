
from flask import Flask, render_template,redirect,request
# from flex import app,event,ui
# app.init()
# Create an instance of Flask app
app= Flask(__name__,static_url_path='/static')

@app.route("/")
def home():
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



# @app.route("/home")
# def Session():
#     import game
#     return game_start()
   

if __name__ == "__main__":
    app.run(debug=True)


