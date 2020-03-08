from flask import Flask, render_template, url_for,redirect, request
from forms.patientform import PatientForm
from forms.prescriptionform import PrescriptionForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'e045fd27f61b2a04b5edbb45fa1350045fe8eb10653be9631d422f6427ba77b6'

@app.route('/',methods=['POST','GET'])
@app.route('/home', methods=['POST','GET'])
def home():
    if request.method == 'POST':
        if request.form['submit'] == 'ADD PATIENT':
            return redirect( url_for('recipient') )
        
        if request.form['submit'] == 'ADD REMINDER':
            return redirect( url_for('reminder') )
    
    return render_template("/welcome.html")

@app.route('/recipient/',methods=['POST','GET'])
def recipient():
    form = PatientForm()
    if form.validate_on_submit():
        form.save()
        return redirect( url_for('home') )
    return render_template('recipient.html',form=form)

@app.route('/reminder', methods=['POST','GET'])
def reminder():
    form = PrescriptionForm()
    form.getPatients()
    print(form.printObj())
    print(form.start_dt.data)
    print(form.end_dt.data)
    print(form.validate_on_submit())

    if request.method == 'POST':
        if form.validateForm():
            form.save()
            return redirect( url_for('home') )

    #if form.validate_on_submit():
    #    form.save()
    #    return redirect( url_for('home') )

    #if request.method == 'POST':
    #    if request.form['submit'] == 'HOME':
    #        return redirect( url_for('home') )
    return render_template('reminder.html', form=form)


 # env FLASK_APP=app.py FLASK_DEBUG=1 flask run 