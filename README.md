# Secure Login System with Brute-force Protection (Python + Flask)

A beginner-friendly cloud and cybersecurity project that simulates a secure login page with password hashing and brute-force attack prevention. This project is part of my early training in cloud and security fundamentals.

---

## Features

- Secure login with hashed passwords using `werkzeug`
- Supports multiple user credentials
- Brute-force protection: blocks login after 3 failed attempts per user
- Built with Flask, Python, HTML
- Cloud-ready: structured for AWS EC2 deployment

---

## Screenshots

### Login Page

A simple HTML login interface styled with Bootstrap:

![Login Page](screenshots/login-page.png)

---

### Brute-force Protection Triggered

After 3 failed attempts, login is temporarily disabled per user:

![Brute Force Blocked](screenshots/too-many-attempts.png)

---

