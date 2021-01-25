from flask import Flask, redirect, url_for, render_template, request
import backend_api

app = Flask(__name__)

@app.route("/", methods=['POST','GET'])
def home():
	if request.method == 'POST':
		x = request.form['text']
		backend_api.start(x)
	return render_template("index.html")



if __name__ == "__main__":
	app.run(debug=True)
