from flask import Flask, render_template, session, request, redirect, url_for

import sqlite3
import auth
import data_david

app = Flask(__name__)

@app.route("/", methods=["GET","POST"])
@app.route("/home", methods=["GET","POST"])
@app.route("/home/", methods=["GET","POST"])
def home():
    if request.method == "GET":
        conn = sqlite3.connect("database.db")
        c = conn.cursor()
        q = " SELECT * FROM post "
        results = c.execute(q)
        loggedin = False
        if 'username' in session:
            loggedin = True
            uname = session['username']
        else:
            uname = ""
        return render_template("home.html", results=results, loggedin=loggedin, uname=uname)
    else: 
        button = request.form['button']
        print button
        if button == "login":
            return redirect(url_for("login"))
        elif button == "logout":
            return redirect(url_for("logout"))
        elif button == "write_post":
            return redirect(url_for("create_post"))

        elif button == "create_account":
            return redirect(url_for("create_account"))



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
                return redirect(url_for("home"))
        else:
            err = "INVALID USERNAME OR PASSWORD!!"
            return render_template("login.html", err = err)

@app.route("/logout")
@app.route("/logout/")
def logout():
    del session['username']
    return redirect(url_for("home"))

@app.route("/create/post/")
@app.route("/create/post")
def create_post():
    return render_template("write_post.html")

@app.route("/create/account/")
@app.route("/create/account")
def create_account():
    return render_template("create_account.html")



@app.route("/blog")
@app.route("/blog/")
def blog():
    return redirect(url_for('home'))

# @app.route("/blog/<username>")
# def blog():
#    if username not in session:
#        return redirect(url_for('login'))
#    load_last10 = data.get(10)
#    return render_template("blog.html",load_last10)

if __name__ == "__main__":
    app.debug = True
    app.secret_key = "cronut"
    app.run(host="0.0.0.0", port=8000)
