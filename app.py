from flask import Flask, render_template, request

app = Flask(__name__)

VALID_USERNAME = "admin"
VALID_PASSWORD = "1234"

@app.route('/')
def home ():
	return render_template('login.html')

@app.route('/login', methods=['POST'])
def login ():
	username = request.form['username']
	password = request.form['password']

	if username == VALID_USERNAME and password == VALID_PASSWORD:
		return "<h2>Login Succesful!</h2>"
	else:
		return "<h2>Invalid username or password</h2>"

if __name__ == '__main__':
	app.run(debug=True)
