from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField,BooleanField
from wtforms.validators import DataRequired,Length, Email, EqualTo

class WelcomeForm(FlaskForm):
    patientBtn = SubmitField('PATIENT')
    recipientBtn = SubmitField('REMINDER')
