from ast import Index

from flask import render_template, redirect, session, request, flash
from flask_bcrypt import bcrypt
from TvShows import app


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/register', methods=['POST'])
def register_user():
    if not index.validate_index(request.form):
        return redirect('/')
    pw_hash = bcrypt.generate_password_hash(request.form['password'])
    data = {
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'email': request.form['email'],
        'password': pw_hash
    }

    user_id = Index.create_user(data)
    session['user_id'] = user_id
    return redirect('/dashboard')


@app.route('/login', methods=['POST'])
def login():
    data = {
        'email': request.form['email'],
        'password': request.form['password']
    }

    user = Index.get_email(data)

    if not user:
        flash("Invalid login")
        return redirect('/')
    if not bcrypt.check_password_hash(user.password, request.form['password']):
        flash("Invalid password")
        return redirect('/')
    session['user_id'] = user.id

    return redirect('/dashboard')

