from shopping import app, mysql
from flask import render_template, url_for, flash, redirect,request, session
from shopping.forms import ContactForm, RegistrationForm,LoginForm
from shopping.models import footer
from flask_mysqldb import MySQL 
import MySQLdb.cursors 
import re 

@app.route('/home')
def home():
    contact= footer.footer()

    return render_template('home.html', contact=contact)

@app.route('/login',methods=['GET', 'POST'])
def login():
    form = LoginForm()
    msg = '' 
    if request.method == 'POST': 
        email = request.form['email'] 
        password = request.form['password']
        remember = request.form['remember']
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor) 
        cursor.execute('SELECT * FROM users WHERE email = % s AND password = % s', (email, password, )) 
        account = cursor.fetchone() 
        if account: 
            session['loggedin'] = True
            session['id'] = account['id'] 
            session['email'] = account['email'] 
            msg = 'Logged in successfully !'
            return redirect(url_for('home')) 
        else: 
            msg = 'Incorrect email / password !'
    return render_template('login.html', title='Login', form=form,msg=msg)

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
    return render_template('register.html', msg = msg,form=form, title='Register') 
    
    