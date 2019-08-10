from flask import request, redirect, url_for, render_template, flash, session
from flask_blog import app
from flask_login import login_user, logout_user, login_required
from flask_blog.models.users import User


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        if request.form['username'] != app.config['USERNAME']:
            flash('User name is different')
        elif request.form['password'] != app.config['PASSWORD']:
            flash('Password is different')
        else:
            login_user(User("request.form['username']"))
            flash('Login successful')
            return redirect(url_for('show_entries'))
    return render_template('login.html')


@app.route('/logout')
def logout():
    logout_user()
    flash('Logged Out')
    return redirect(url_for('login'))

@app.errorhandler(404)
def non_existant_route(error):
    return redirect(url_for('login'))
