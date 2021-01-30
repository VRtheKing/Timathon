from flask import Flask, redirect, url_for, render_template, request, jsonify, make_response
import backend_api
import commands

app = Flask(__name__)

@app.route("/", methods=['POST','GET'])
def home():

	if request.method == 'POST':
		x = request.form['text']
		backend_api.start(x)
	return render_template("index.html")

@app.route("/speak", methods =['POST','GET'])
def speak():

	req = request.get_json()
	speaker = commands.speak_commands()
	speak = speaker.speak(req)
	print(req)

	res = make_response(jsonify({"message":speak},200))

	return res

@app.route("/about", methods=['POST','GET'])
def about():
	return render_template("about.html")

if __name__ == "__main__":
	app.run(debug = True)
