from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired, Length


class LoginForms(FlaskForm):
    username = StringField('Username', validators=[InputRequired(), Length(1, 32)])
    password = PasswordField('Password', validators=[InputRequired(), Length(6, 32)])
    submit = SubmitField('Login in')


class RegisterForms(FlaskForm):
    username = StringField('Username', validators=[InputRequired(), Length(1, 32)])
    password = PasswordField('Password', validators=[InputRequired(), Length(6, 32)])
    repeat_password = PasswordField('Repeat password', validators=[InputRequired(), Length(6, 32)])
    submit = SubmitField('Register')
