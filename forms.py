from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, length
from flask_wtf import FlaskForm

class loginform(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember me')
    submit = SubmitField('Login')
