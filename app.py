from flask import Flask, render_template, url_for, flash, redirect, request
from forms.patientform import PatientForm
from forms.prescriptionform import PrescriptionForm
from forms.dashboardform import DashBoardForm

app = Flask(__name__)
mykey = 'e045fd27f61b2a04b5edbb45fa1350045fe8eb10653be9631d422f6427ba77b6'
app.config['SECRET_KEY'] = mykey


@app.route('/', methods=['GET', 'POST'])
@app.route('/landingpage', methods=['POST', 'GET'])
def home():
    return render_template("landingpage.html")


@app.route('/welcome', methods=['POST', 'GET'])
def welcome():
    if request.method == 'POST':
        if request.form['submit'] == 'ADD PATIENT':
            return redirect(url_for('recipient'))

        if request.form['submit'] == 'ADD REMINDER':
            return redirect(url_for('reminder'))

        if request.form['submit'] == 'DASHBOARD':
            return redirect(url_for('dashboard'))
    return render_template("welcome.html")


@app.route('/recipient', methods=['POST', 'GET'])
def recipient():
    form = PatientForm()
    if form.validate_on_submit():
        form.save()
        return redirect(url_for('welcome'))
    return render_template('recipient.html', form=form)


@app.route('/reminder', methods=['POST', 'GET'])
def reminder():
    form = PrescriptionForm()
    form.getPatients()

    if request.method == 'POST':
        isvalid, inputs = form.validateForm()
        print(isvalid)
        print(inputs)
        if isvalid:
            form.save()
            return redirect(url_for('welcome'))
        else:
            for input in inputs:
                flash('Check the input {}, the value is invalid!'.format(
                    input), 'danger')
    return render_template('reminder.html', form=form)


@app.route('/dashboard/', defaults={
    'patientID': 0, 'taskID': 0}, methods=['POST', 'GET'])
@app.route('/dashboard2/<int:patientID>/<int:taskID>', methods=['POST', 'GET'])
def dashboard(patientID, taskID):
    form = DashBoardForm()
    prescriptions = []
    tasks = []
    form.getPatients()
    if not patientID == 0:
        form.selectedid = patientID
        prescriptions = form.getPrescriptions()
        if not taskID == 0:
            tasks = form.getTasks(taskID)
    return render_template(
        'dashboard.html', form=form, prescriptions=prescriptions, tasks=tasks)


@app.route('/about', methods=['POST', 'GET'])
def about():
    return render_template('about.html')


@app.route('/features', methods=['POST', 'GET'])
def features():
    return render_template('features.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
