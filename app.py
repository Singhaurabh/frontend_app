from flask import Flask, render_template, request, redirect, url_for, flash, session
import sqlite3
import os

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'

# Database setup
DB_NAME = 'db.sqlite3'

def init_db():
    with sqlite3.connect(DB_NAME) as conn:
        conn.execute('''CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL,
            gender TEXT
        )''')

def setup():
    init_db()

app.before_request_funcs.setdefault(None, []).append(setup)


# =========================
# Routes
# =========================

@app.route('/')
def home():
    return redirect(url_for('login'))

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']
        try:
            with sqlite3.connect(DB_NAME) as conn:
                conn.execute("INSERT INTO users (name, email, password) VALUES (?, ?, ?)", (name, email, password))
            flash('Signup successful! Please login.', 'success')
            return redirect(url_for('login'))
        except sqlite3.IntegrityError:
            flash('Email already exists.', 'error')
    return render_template('signup.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        with sqlite3.connect(DB_NAME) as conn:
            cur = conn.cursor()
            cur.execute("SELECT * FROM users WHERE email = ? AND password = ?", (email, password))
            user = cur.fetchone()
        if user:
            session['user_id'] = user[0]
            session['email'] = user[2]
            return redirect(url_for('gender'))
        else:
            flash('Invalid email or password', 'error')
    return render_template('login.html')


@app.route('/reset_password', methods=['GET', 'POST'])
def reset_password():
    # Placeholder logic — add token verification if needed
    if request.method == 'POST':
        password = request.form['password']
        confirm = request.form['confirm_password']
        if password == confirm and 'email' in session:
            with sqlite3.connect(DB_NAME) as conn:
                conn.execute("UPDATE users SET password = ? WHERE email = ?", (password, session['email']))
            flash('Password updated!', 'success')
            return redirect(url_for('login'))
        else:
            flash('Passwords do not match.', 'error')
    return render_template('reset_password.html')

@app.route('/logout')
def logout():
    session.clear()
    flash('You have been logged out.', 'info')
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)
