#!/usr/bin/python3
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo


class WelcomeForm(FlaskForm):
    """wtf Form linked with welcome template"""
    patientBtn = SubmitField('PATIENT')
    recipientBtn = SubmitField('REMINDER')
