from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField,FileField
from wtforms.validators import DataRequired, Length, Email, EqualTo, NumberRange,ValidationError    
from flask_wtf.file import FileField, FileAllowed
from flask_login import current_user
from shopping.models import User


class RegistrationForm(FlaskForm):
    username = StringField('Username',
                           validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    phone= StringField('Phone No',validators=[DataRequired(),Length(min=7,max=15)])
    picture = FileField('Update Profile Picture', validators=[FileAllowed(['jpg', 'png'])])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password',
                                     validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')

class LoginForm(FlaskForm):
    email = StringField('Email',render_kw={"placeholder": "Enter email"},
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password',render_kw={"placeholder": "Enter password"}, validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')

class ContactForm(FlaskForm):
    name = StringField('Name',
                           validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    phone= StringField('Phone No',validators=[DataRequired(),Length(min=7,max=15)])
    message = TextAreaField('Message',
                           validators=[DataRequired()])
    submit = SubmitField('Submit')

class UpdateProfileForm(FlaskForm):
    username = StringField('Username',
                           validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    phone = StringField('Username',
                           validators=[DataRequired(), Length(min=7, max=15)])
    picture = FileField('Update Profile Picture', validators=[FileAllowed(['jpg', 'png'])])
    phone= StringField('Phone No',validators=[DataRequired(),Length(min=7,max=15)])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Confirm')

    def validate_username(self, username):
        if username.data != current_user.username:
            user = User.query.filter_by(username=username.data).first()
            if user:
                raise ValidationError('That username is taken. Please choose a different one.')

    def validate_email(self, email):
        if email.data != current_user.email:
            user = User.query.filter_by(email=email.data).first()
            if user:
                raise ValidationError('That email is taken. Please choose a different one.')
    def validate_phone(self, phone):
        if phone.data != current_user.phone:
            user = User.query.filter_by(phone=phone.data).first()
            if user:
                raise ValidationError('Aldready have an account with this Phone No')
    
    def validate_password(self, password):
        if password.data != current_user.password:
            user = User.query.filter_by(password=password.data).first()
            if user:
                raise ValidationError('Aldready have an account with this password No')