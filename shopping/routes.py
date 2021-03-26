
import os
import secrets
from PIL import Image
from sqlalchemy.sql.functions import user
from shopping import app,db,bcrypt
from flask import render_template, url_for, flash, redirect,request, session
from shopping.forms import ContactForm, RegistrationForm,LoginForm, UpdateProfileForm
from shopping.models import User,Contact
from flask_login import login_user, current_user, logout_user, login_required
from sqlalchemy import insert,update,delete
import re 

class footer():
  def footer():
    contact= ContactForm()
    if request.method =='POST':
      name = request.form['name']
      email = request.form['email'] 
      phone = request.form['phone']
      message = request.form['message']
      query=Contact(username=name, email=email,phone=phone, message=message)
      db.session.add(query)
      db.session.commit()
      msg = "We got your query, we'll revert to u back soon.."
    return contact


@app.route('/home',methods=['GET', 'POST'])
def home():
    form= footer.footer()
    if request.method=='POST':
        return redirect(url_for('home'))
    return render_template('home.html',form=form)

@app.route('/login',methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
            return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check email and password', 'danger')
    return render_template('login.html', title='Login', form=form)

@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data,phone=form.phone.data,image_file=form.picture, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash('Your account has been created! You are now able to log in', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form) 
    
@app.route('/profile', methods=['GET', 'POST'])
@login_required
def profile():
    form = UpdateProfileForm()
    if form.validate_on_submit():
        if form.picture.data:
            picture_file = save_picture(form.picture.data)
            current_user.image_file = picture_file
        current_user.username = form.username.data
        current_user.email = form.email.data
        current_user.phone = form.phone.data
        user = User.query.filter_by(email=current_user.email).first()
        if current_user and bcrypt.check_password_hash(user.password, form.password.data):
            db.session.commit()
            flash('Your account has been updated!', 'success')
            return redirect(url_for('profile'))
    elif request.method == 'GET':
        form.username.data = current_user.username
        form.email.data = current_user.email
        form.phone.data = current_user.phone
    image_file = url_for('static', filename='images/profile_pics/' + current_user.image_file)
    return render_template('profile.html', title='Account',
                           image_file=image_file, form=form)
    

def save_picture(form_picture):
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(form_picture.filename)
    picture_fn = random_hex + f_ext
    picture_path = os.path.join(app.root_path, 'static/images/profile_pics', picture_fn)

    output_size = (125, 125)
    i = Image.open(form_picture)
    i.thumbnail(output_size)
    i.save(picture_path)

    return picture_fn

@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for('home'))

@app.route('/mother')
def mother():
    form= footer.footer()
    if request.method=='POST':
        return redirect(url_for('home'))
    return render_template('mother.html',form=form)

@app.route('/cpu')
def cpu():
    form= footer.footer()
    if request.method=='POST':
        return redirect(url_for('home'))
    return render_template('cpu.html', form=form)

@app.route('/gpu')
def gpu():
    form= footer.footer()
    if request.method=='POST':
        return redirect(url_for('home'))
    return render_template('gpu.html',form=form)

@app.route('/storage')
def storage():
    form= footer.footer()
    if request.method=='POST':
        return redirect(url_for('home'))
    return render_template('storage.html',form=form)

@app.route('/cart')
def cart():
    return render_template('cart.html')