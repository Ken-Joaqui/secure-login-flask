from flask import Flask, render_template, request
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)

login_attempts = {}
MAX_ATTEMPTS = 3

fake_users = {
	"admin": generate_password_hash("1234"),
	"ken": generate_password_hash("pogi"),
	"noone": generate_password_hash("who")
}

@app.route('/')
def home ():
	return render_template('login.html')

@app.route('/login', methods=['POST'])
def login ():
	username = request.form['username']
	password = request.form['password']

	if username not in login_attempts:
		login_attempts[username] = 0
	
	if login_attempts[username] >= MAX_ATTEMPTS:
		return "<h2>Too many failed attempts. Access Blocked.</h2>"

	if username in fake_users and check_password_hash(fake_users[username], password):
		login_attempts[username] = 0
		return "<h2>Login Succesful!</h2>"
	else:
		login_attempts[username] += 1
		return f"<h2>Invalid login. Attempt {login_attempts[username]}/{MAX_ATTEMPTS}</h2>"

if __name__ == '__main__':
	app.run(debug=True)
