from flask import Flask, render_template, request
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)

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

	if username in fake_users and check_password_hash(fake_users[username], password):
		return "<h2>Login Succesful!</h2>"
	else:
		return "<h2>Invalid username or password</h2>"

if __name__ == '__main__':
	app.run(debug=True)
