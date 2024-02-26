import os

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from werkzeug.security import check_password_hash, generate_password_hash
from datetime import date

from helpers import apology, login_required

# Configure application
app = Flask(__name__)

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///workouts.db")

@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response

@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":
        # Check if "username" is empty
        if not request.form.get("username"):
            return apology("username field empty", 403)

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")
    
@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")

@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""

    if request.method == "POST":

        username = request.form.get("username")
        password = request.form.get("password")

        # Check if "username" is empty
        if not username:
            return apology("username field empty", 403)
        # Check if "password" is empty
        elif not password:
            return apology("password field empty", 403)
        # Check if "confirm" is empty
        elif not request.form.get("confirm"):
            return apology("pass confirmation field empty", 403)
        
        # Get the list of all usernames from the db
        usernames = db.execute("SELECT username FROM users")

        # Check if the username is not already used
        for name in usernames:
            if name["username"] == username:
                return apology("username already used", 403)
            
        # Password == Pass confirmation
        if password != request.form.get("confirm"):
            return apology("password != confirmation", 403)

        # Generate password hash
        hash = generate_password_hash(password, method='pbkdf2', salt_length=16)

        # Add the credentials to the db
        db.execute("INSERT INTO users (username, hash) VALUES (?,?)", username, hash) 

        return redirect("/login")
    else:
        return render_template("register.html")
    
@app.route("/")
@login_required
def index():
    return apology("TODO", 400)

@app.route("/add_exercise")
@login_required
def add_exercise():
    return apology("TODO", 400)

@app.route("/add_log")
@login_required
def add_log():
    return apology("TODO", 400)