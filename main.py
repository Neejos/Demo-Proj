
from flask import Flask, render_template,redirect,request
from flex import app,event,ui
app.init()

app= Flask(__name__)

@app.route("/home")
def Session():
    import game
    return game_start()
   

if __name__ == "__main__":
    app.run(debug=True)


