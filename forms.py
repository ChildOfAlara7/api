from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired

class AddingForm(FlaskForm):
    login = StringField('Login', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    name = StringField('Name')
    mail = StringField('Mail')
    submit = SubmitField('Submit')

class ShowForm(FlaskForm):
    id = StringField('id', validators=[DataRequired()])
    submit = SubmitField('Submit')