#   Josephine Livingstone - Honours Project

# import Flask tools
from flask import Flask, render_template, redirect, url_for, session, flash
# import PyMySQL library (connects Python to MySQL/MariaDB)
import pymysql 
# import cursors module (to use DictCursor: returns DB rows as dictionaries)
import pymysql.cursors
# password hashing
from werkzeug.security import generate_password_hash, check_password_hash

# ------------------------------------------------------------------- #

# Create Flask app
myWebApp = Flask(__name__)
# Set secret_key, required for session
myWebApp.secret_key = 'secretkey'

# Open a database connection
def database():
    return pymysql.connect (
        host='localhost', # DB runs on same machine as Flask app
        user='myWebAppUser', # MariaDB username
        password='myWebAppPassword', # MariaDB password
        database='myWebAppDB', # MariaDB 
        cursorclass=pymysql.cursors.DictCursor # return results as dictionaries
    )

# ------------------------------------------------------------------- #

# when route is accessed, run the function below
# find .html file in templates/ folder and send it to browser
@myWebApp.route('/') 
def home():
    return render_template('home.html') 


@myWebApp.route('/account')
def account():
    return render_template('account.html')


@myWebApp.route('/labs')
def labs():
    # if user is not logged in, redirect to login page and display message
    if 'user' not in session:
        flash('You are required to log in before accessing the labs.')
        return redirect(url_for('account'))
    return render_template('labs.html')


@myWebApp.route('/easy')
def easy():
    # if user is not logged in, redirect to login page and display message
    if 'user' not in session:
        flash('You are required to log in before accessing the labs.')
        return redirect(url_for('account'))
    return render_template('easy.html')


@myWebApp.route('/medium')
def medium():
    # if user is not logged in, redirect to login page and display message
    if 'user' not in session:
        flash('You are required to log in before accessing the labs.')
        return redirect(url_for('account'))
    return render_template('medium.html')


@myWebApp.route('/hard')
def hard():
    # if user is not logged in, redirect to login page and display message
    if 'user' not in session:
        flash('You are required to log in before accessing the labs.')
        return redirect(url_for('account'))
    return render_template('difficult.html')




if __name__ == '__main__': # check if file is being run directly
    myWebApp.run(debug=True) # start Flask server in debug mode
