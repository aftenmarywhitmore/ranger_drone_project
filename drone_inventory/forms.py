from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email



class UserLoginForm(FlaskForm):
    #email, password, submit_button
    email = StringField('Email', validators = [DataRequired(), Email()]) #check there's data being passed into form AND that it's a valid emamil
    first_name = StringField('First Name')
    last_name = StringField('Last Name')
    password = PasswordField('Password', validators = [DataRequired()]) #password will be starred out eventually so we need a password field
    submit_button = SubmitField() #hotspot for errors: () after [DataRequired()]
    