#!/usr/bin/python3
from flask import Flask, render_template, request, redirect, url_for, session
from users import create_table, create_account, check_account

app = Flask(__name__)

app.secret_key = "E.vXVq=adsfadsfbjgfvEIqKk~6wP2&IbDIY-F"

with app.app_context():
    create_table()


@app.route("/")
def meme_generator():
    if session.get("logged_in"):
        return render_template("memes.html")
    else:
        return redirect(url_for("login_page"))


@app.route("/login", methods=["GET", "POST"])
def login_page():
    error = ""
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        if check_account(username, password):
            session["logged_in"] = True
            return redirect(url_for("meme_generator"))
        else:
            error = "Wrong username/password"
    if session.get("logged_in"):
        return redirect(url_for("meme_generator"))
    else:
        return render_template("login.html", error=error)


@app.route("/logout")
def logout():
    session["logged_in"] = False
    return redirect(url_for("login_page"))


@app.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "GET":
        return redirect(url_for("login_page"))
    else:
        username = request.form["username"]
        password = request.form["password"]
        confirm = request.form["confirm-password"]

        if password != confirm:
            msg = "Passwords don't match"
        else:
            msg = create_account(username, password)

        return render_template("login.html", error=msg)

    # Stopped at slide 17 (Start with Ex. 2)


# Hw:

# Exercise 2 (slide 17 - 26) --> Gives full credit
