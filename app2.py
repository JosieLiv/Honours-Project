#   Josephine Livingstone - Honours Project

# import Flask tools
from flask import Flask, render_template, redirect, url_for, request, session, flash
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








@myWebApp.route('/account', methods=['GET', 'POST'])
def account():
    
    if request.method == 'POST':
        
        action = request.form.get('action')
        
        if action == 'register':
            username = request.form['username']
            email = request.form['email']
            password = generate_password_hash(request.form['password'])

            if len(username) <3 or len(username) >20:
                flash('Username must be between 3 and 20 characters long')
            elif len(password) <8:
                flash('Password must be at least 8 characters long')
            elif '@' not in email:
                flash('Please enter a valid email')
            else:
                connection = database()
                cursor = connection.cursor()
                # check if email has already been registered 
                cursor.execute('SELECT * FROM users WHERE email = %s', (email,))
                user_exists = cursor.fetchone()
                if user_exists:
                    flash('This email has already been registered. Please login or use another email')
                else:
                    cursor.execute('INSERT INTO users (username, email, password) VALUES (%s, %s, %s)', (username, email, password))
                    connection.commit()
                    flash('Success! Account has been created, please login.')
                connection.close()
            
        elif action == 'login':
            email = request.form['email']
            password = request.form['password']

            connection = database()
            cursor = connection.cursor()
            cursor.execute('SELECT * FROM users WHERE email = %s', (email,))
            user = cursor.fetchone()
            connection.close()

            if user and check_password_hash(user['password'], password):
                session['user_id'] = user['userID']
                session['username'] = user['username']
                return redirect(url_for('account'))
            else:
                flash('Invalid login details. Please try again.')
        
    if 'user_id' in session:
        connection = database()
        cursor = connection.cursor()
        cursor.execute('SELECT * FROM users WHERE userID = %s', (session['user_id'],))
        user = cursor.fetchone()
        connection.close()
        return render_template('account.html', user=user)
    
    return render_template('account.html', user=None)
    


@myWebApp.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('account'))



@myWebApp.route('/labs')
def labs():
    # if user is not logged in, redirect to login page and display message
    if 'user_id' not in session:
        flash('You are required to log in before accessing the labs.')
        return redirect(url_for('account'))
    return render_template('labs.html')


@myWebApp.route('/labs/beginner')
def beginner():
    # if user is not logged in, redirect to login page and display message
    if 'user_id' not in session:
        flash('You are required to log in before accessing the labs.')
        return redirect(url_for('account'))
    return render_template('beginner.html')


@myWebApp.route('/labs/intermediate')
def intermediate():
    # if user is not logged in, redirect to login page and display message
    if 'user_id' not in session:
        flash('You are required to log in before accessing the labs.')
        return redirect(url_for('account'))
    return render_template('intermediate.html')


@myWebApp.route('/labs/advanced')
def advanced():
    # if user is not logged in, redirect to login page and display message
    if 'user_id' not in session:
        flash('You are required to log in before accessing the labs.')
        return redirect(url_for('account'))
    return render_template('advanced.html')




if __name__ == '__main__': # check if file is being run directly
    myWebApp.run(debug=True) # start Flask server in debug mode
