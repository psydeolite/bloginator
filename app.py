from flask import Flask, render_template, session, request, redirect, url_for
from pymongo import MongoClient
#import sqlite3
import auth
import data_david


app = Flask(__name__)


@app.route("/", methods=["GET","POST"])
@app.route("/home", methods=["GET","POST"])
@app.route("/home/", methods=["GET","POST"])
def home():
    if request.method == "GET":
        conn = MongoClient()
        db = conn.database
        posts = db.post
        entries = posts.find()
        '''print '\n entries'
        for e in entries:
            print e'''
        results = db.comment
        r_comments = results.find()
        comments = []
        for comment in r_comments:
            comments.append(comment)
                
        loggedin = False
        if 'username' in session:
            loggedin = True
            username = session['username']
        else:
            username = ""
        return render_template("home.html", entries=entries, loggedin=loggedin, uname=username, comments=comments)
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
        else:
            session['post_title'] = button
            return redirect(url_for("create_comment"))



@app.route("/login", methods=["GET","POST"])
@app.route("/login/", methods=["GET","POST"])

def login():
    if request.method == "GET":
        return render_template("login.html")
    else:
        username = request.form.get('username')
        password = request.form.get('password')
        button = request.form.get('button')
        print request.form
        if button=="Cancel":
            return redirect(url_for('home'))

        if auth.authenticate(username, password):
            if 'username' not in session:
                session['username'] = username
                return redirect(url_for("home"))
        else:
            err = "INVALID USERNAME OR PASSWORD!!"
            return render_template("login.html", err = err)

@app.route("/logout")
@app.route("/logout/")
def logout():
    del session['username']
    return redirect(url_for("home"))

@app.route("/create/post", methods=["GET","POST"])
@app.route("/create/post/", methods=["GET","POST"])
def create_post():
    if 'username' not in session:
        return """<h2> You must login in to write a post. </h2> <br><hr><br><a href = "/login">Login Here</a>""" 
    else:
        if request.method == "GET":
            return render_template("write_post.html")
        else:
            title = request.form.get('title')
            body = request.form.get('body')
            button = request.form.get('button')
            print 'aboutaprint'
            print button
            if button == "Cancel":
                return redirect(url_for('home'))
            elif title == "" or body == "":
                err = "Error: Title and Body must have text." 
                return render_template("write_post.html", err = err)
            else:
                username = session['username']
                data_david.add_post(body, username, title)
                return redirect(url_for("home"))


@app.route("/create/account", methods=["GET","POST"])
@app.route("/create/account/", methods=["GET","POST"])
def create_account():
        if 'username' in session:
            return "<h1> You are already signed in </h1>"
        else: 
            if request.method == "GET":
                return render_template("create_account.html")
            else:
                print request.form
                username = request.form['username']
                password = request.form['password']
                password_again = request.form['password_again']
                button = request.form['button']
                if button == "Cancel":
                    return redirect(url_for('home'))
                elif len(username) < 6 or len(password) < 6:
                    err = "Error: Username & Password both must be at least 6 characters." 
                    return render_template("create_account.html", err = err)
                elif password != password_again:
                    err = "Passwords entered do not match. Try again"
                    return render_template("create_account.html", err = err)
                else:
                    conn = MongoClient()
                    db = conn.database
                    result = db.users.find()
                                        
                    for r in result:
                        print '\n---------'
                        print r.keys()
                        print 'username' in r.keys()
                        if username==r['username']:
                            err = "Username already exists."
                            return render_template("create_account.html", err = err)
                    # should be good to add
                    data_david.add_user(username, password, "hefhebf")
                    if 'username' not in session:
                        session['username'] = username
                    return redirect(url_for("home"))

@app.route("/create/comment", methods=["GET","POST"])
@app.route("/create/comment/", methods=["GET","POST"])
def create_comment():
    if 'username' not in session:
        return """<h2> You must login in to write a comment. </h2> <br><hr><br><a href = "/login">Login Here</a>""" 
    else:
        if request.method == "GET":
            if session['post_title'] != "":
                print session['post_title']
                return render_template("comment_post.html")
            else:
                return """<h2> You must select a post to comment on. </h2> <br><hr><br><a href = "/home">View Posts Here</a>"""
        else:
            print request.form
            body = request.form.get('body')
            button = request.form.get('button')
            if button == "Cancel":
                return redirect(url_for('home'))
            elif body == "":
                err = "Error: Body must have text." 
                return render_template("write_post.html", err = err)
            else:
                aname = session['username']
                data_david.add_comment(body,session['post_title'],aname)
                session['post_title'] = ""
                return redirect(url_for("home"))

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
    app.run(host="0.0.0.0", port=4000)
