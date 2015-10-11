from flask import Flask, render_template, session, request

import sqlite3
import auth

app = Flask(__name__)

@app.route("/")
@app.route("/home")
@app.route("/home/")
def home():
    return render_template("home.html")

@app.route("/login")
@app.route("/login/")

@app.route("/login", methods=["GET","POST"])
@app.route("/login/", methods=["GET","POST"])

def login():
    if request.method == "GET":
        return render_template("login.html")
    else:
        uname = request.form['username']
        pword = request.form['password']
        button = request.form['button']

        if button=="cancel":
            return render_template('login.html')

        if auth.authenticate(uname, pword):
            if 'username' not in session:
                session['username'] = uname
                return redirect(url_for("secret"))
        else:
            err = "INVALID USERNAME OR PASSWORD!!"
            return render_template("login.html", err = err)


if __name__ == "__main__":
    app.debug = True
    app.run(host="0.0.0.0", port=8000)
