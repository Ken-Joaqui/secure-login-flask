from flask import Flask, render_template, request
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)

VALID_USERNAME = "admin"
HASHED_PASSWORD = generate_password_hash("1234")

@app.route('/')
def home ():
	return render_template('login.html')

@app.route('/login', methods=['POST'])
def login ():
	username = request.form['username']
	password = request.form['password']

	if username == VALID_USERNAME and check_password_hash(HASHED_PASSWORD, password):
		return "<h2>Login Succesful!</h2>"
	else:
		return "<h2>Invalid username or password</h2>"

if __name__ == '__main__':
	app.run(debug=True)
