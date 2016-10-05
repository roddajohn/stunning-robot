from flask import render_template, flash, redirect, request, session, url_for, jsonify
from forms import *
from app import app, db, models
from sqlalchemy import or_

@app.route('/', methods=['GET'])
@app.route('/index', methods=['GET'])
def index():
    user = None
    if 'username' in session and session['username']:
        user = models.User.query.filter_by(username = session['username']).first()
        flash('You are logged in')

    return render_template("index.html", user = user)

@app.route('/logout')
def logout():
    session.pop('username')
    flash('Logged out')
    return redirect('index')

@app.route('/create', methods=['GET', 'POST'])
def create():
    create_form = CreateForm()

    if create_form.validate_on_submit():
        new_user = models.User(username = create_form.username.data)
        new_user.set_password(create_form.password.data)
        db.session.add(new_user)
        db.session.commit()
        flash('You have signed up!')
        return redirect('login')

    return render_template('create.html', create_form = create_form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    login_form = LoginForm()

    if login_form.validate_on_submit():
        session['username'] = login_form.username.data
        return redirect('index')

    return render_template('login.html', login_form = login_form)



