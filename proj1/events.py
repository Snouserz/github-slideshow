
import time
import os
from flask import Flask, request, session, url_for, redirect, render_template, abort, g, flash, _app_ctx_stack
from werkzeug.security import check_password_hash, generate_password_hash
from hashlib import md5
from datetime import datetime
from models import db, User, Event

app = Flask(__name__)

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(app.root_path, 'events.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False #here to silence deprecation warning
db.init_app(app)

@app.cli.command('initdb')
def initdb_command():
	db.create_all()

@app.route('/')
def eventPage():
	if "username" in session:
		profile_user = User.query.filter_by(username=username)
		evnts = Event.query.filter_by(host= profile_user.username).order_by(Event.id.start()).all()
		pevnts = Event.query.order_by(Event.id.start()).all()
		return render_template('eventsTable', events = evnts, pevnts = pevnts, username=session["username"])
	elif not 
		evnts = None;
		pevnts = Event.query.order_by(Event.id.start()).all()
		return render_template('eventsTable', events = evnts, pevnts = pevnts, username=session["username"])

@app.route('/attend', methods=['GET', 'POST']) 
	if "username" in session:
		event = Event.query.filter_by(id = event_id).first()
		if not event.host = username:
			User.query.filter_by(username=username).first().links.append(event)
			db.session.commit()
			flash("You are now registered for this event")

@app.route('/login', methods=['GET', 'POST'])
def login():
	if "username" in session:
		return redirect(url_for('eventPage'))
	if request.method == 'POST':
		user = User.query.filter_by(username=request.form['username']).first()
		if user is None:
			error = 'Invalid Username'
		elif not check_password_hash(user.pw_hash, request.form['password']):
			error = 'Invalid password'
		else:
			flash('Login successful')
			session['user_id'] = user.id
			return redirect(url_for('eventPage'))
	return render_template('login.html', error = error)

@app.route('/logout')
def logout():
	profile_user = User.query.filter_by(username=username)
	user_id = profile_user.id
	flash('Successfully logged out')
	session.pop(session['user_id'], None)

@app.route('/register')
def register():
	if "username" in session:
		return redirect(url_for('eventPage'))
	if request.method == 'POST':
		if not request.form['username']:
			error = 'You have to enter a username'
		elif not request.form['password']:
			error = 'You have to enter a password'
		elif User.query.filter_by(username=username).first() is not None:
			error = 'The username is already taken'
		else:
			db.session.add(User(request.form['username'], generate_password_hash(request.form['password'])))
			db.session.commit()
			flash('You were successfully registered and can login now')
			return redirect(url_for('login'))
	return render_template('register.html', error=error)

@app.route('/CreateEvent', methods = ['POST'])
def create():

if request.method == 'POST':
	if "username" in session:
		if not request.form['title']:
			error = 'You have to enter a title'
		elif not request.form['starting-time']:
			error = 'You have to enter a start time'
		elif not request.form['ending-time']:
			error = 'You have to enter an ending time'
		else:
		    db.session.add(Event(request.form['title'], request.form['description'], 
			       request.form['starting-time'], request.form['ending-time'], "username"))
		    db.session.commit()

		return render_template('eventCreation', error = error)
	elif not:
		flash('Need to be logged in to create event')
		return redirect(url_for('login'))


@app.route('/CancelEvent', methods = ['GET', 'POST'] )
def cancel():
if request.method == 'POST':
	if request.form['confirmation'] = confirm:
		Event.objects.filter_by(id = event_id).delete()
		db.session.commit()
	return render_template('CancelEvent')