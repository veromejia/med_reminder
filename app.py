from flask import Flask, render_template, url_for, redirect, request
from forms.patientform import PatientForm
from forms.prescriptionform import PrescriptionForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'e045fd27f61b2a04b5edbb45fa1350045fe8eb10653be9631d422f6427ba77b6'


@app.route('/', methods=['GET', 'POST'])
@app.route('/home', methods=['POST', 'GET'])
def home():
    if request.method == 'POST':
        if request.form['submit'] == 'ADD PATIENT':
            form=PatientForm()
            return render_template("/recipient.html", form=form)

        if request.form['submit'] == 'ADD REMINDER':
            form=PrescriptionForm()
            return render_template("/reminder.html", form=form)

    return render_template("/welcome.html")


@app.route('/recipient', methods=['POST', 'GET'])
def recipient():
    form = PatientForm()
    if form.validate_on_submit():
        form.save()
        return redirect(url_for('home'))
    return render_template('recipient.html', form=form)


@app.route('/reminder', methods=['POST', 'GET'])
def reminder():
    form = PrescriptionForm()
    form.getPatients()

    if request.method == 'POST':
        if form.validateForm():
            form.save()
            return redirect(url_for('home'))
    return render_template('reminder.html', form=form)
