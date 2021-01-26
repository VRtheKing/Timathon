from flask import Flask, redirect, url_for, render_template, request
import backend_api
import commands
from flask_ngrok import run_with_ngrok

app = Flask(__name__)

@app.route("/", methods=['POST','GET'])
def home():
	if request.method == 'POST':
		x = request.form['text']
		backend_api.start(x)
	return render_template("index.html")

@app.route("/speak", methods =['POST','GET'])
def speak():
	command = commands.take_commands()
	speak = commands.speak_commands(command)
	return redirect(url_for('home'))

if __name__ == "__main__":
	app.run(debug = True)
