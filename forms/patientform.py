from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField,BooleanField
from wtforms.validators import DataRequired,Length, Email, EqualTo
from backend.models.db_storage import DBStorage
from backend.models.patient import Patient

class PatientForm(FlaskForm):
    firstName = StringField('First Name',validators=[ DataRequired(),Length(min=2,max=20) ], render_kw={"placeholder": "First Name"} )
    lastname = StringField('Last Name',validators=[ DataRequired(),Length(min=2,max=20) ], render_kw={"placeholder": "Last Name"} )
    email = StringField('Email',validators=[DataRequired(),Email()], render_kw={"placeholder": "johndoe@gmail.com"})
    phone_no = StringField('Phone',validators=[ DataRequired(),Length(min=2,max=20)], render_kw={"placeholder": "XXX-XXX-XXXX"} )
    submit = SubmitField('CREATE')

    def save(self):
        db = DBStorage()
        p = Patient()
        p.name = self.firstName.data
        p.last_name = self.lastname.data
        p.email = self.email.data
        p.phone = self.phone_no.data
        db.add_patient(p)



