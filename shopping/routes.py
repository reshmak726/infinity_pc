from shopping import app, mysql
from flask import render_template, url_for, flash, redirect,request, session
from shopping.forms import RegistrationForm,LoginForm
from flask_mysqldb import MySQL 
import MySQLdb.cursors 
import re 

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/login',methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('login.html', title='Login', form=form)

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    msg = '' 
    if request.method == 'POST': 
        username = request.form['username']
        email = request.form['email'] 
        phone= request.form['phone']
        password = request.form['password'] 
         
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor) 
        cursor.execute('SELECT * FROM users WHERE email = % s', (email, )) 
        account = cursor.fetchone() 
        if account: 
            msg = 'Account already exists !'
        elif not re.match(r'[^@]+@[^@]+\.[^@]+', email): 
            msg = 'Invalid email address !'
        elif not re.match(r'[A-Za-z0-9]+', username): 
            msg = 'Username must contain only characters and numbers !'
        elif not username or not password or not email: 
            msg = 'Please fill out the form !'
        else: 
            cursor.execute('INSERT INTO users VALUES (NULL, % s, % s, % s,%s)', (username,email,phone,password))  
            mysql.connection.commit() 
            cursor.close()
            msg = 'You have successfully registered !'
    elif request.method == 'POST': 
        msg = 'Please fill out the form !'
        msg = 'You have successfully registered !'
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', msg = msg,form=form,title='Register') 
    
    