from flask import Flask, render_template, redirect, request
app = Flask(__name__)
port = 5050
host = "0.0.0.0"
recipients = []

@app.route("/", strict_slashes=False)
def home():
  return render_template("/welcome.html")

@app.route("/recipient/", strict_slashes=False)
def recipient():
  return render_template("/recipient.html")

@app.route("/reminder/", strict_slashes=False)
def reminder():
  return render_template("/reminder.html", recipients=recipients)

@app.route("/record/", strict_slashes=False)
def record():
  return render_template("/record.html", recipients=recipients)

@app.route("/recipient/", methods=["POST"], strict_slashes=False)
def input_reciever():
  data = request.get_json()
  recipients.append(data)
  return "OK"

@app.route("/reminder/", methods=["POST"], strict_slashes=False)
def input_reminder():
  data = request.get_json()
  print(data)
  return "OK"

if __name__ == '__main__':
  app.run(host=host, port=port)