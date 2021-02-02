from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
	
	id = db.Column(db.Integer, primary_key = True)
	username = db.Column(db.String(24), unique = True, nullable=False)
	pw_hash = db.Column(db.String(64), unique = True, nullable=False)

	#one to many
	my_events = db.relationship('Event', backref = 'User') 

	#many to many
	events = db.relationship('Event', secondary=links, backref=db.backref('attendees', lazy = 'dynamic'))

	def __init__(self, username, pw_hash):
		self.username = username
		self.pw_hash = pw_hash

	def __repr__(self):
		return '<User {}>'.format(self.username)

	links = db.Table('links',
	db.Column('user_id', db.Integer, db.ForeignKey('User.user_id')),
	db.Column('event_id', db.Integer, db.ForeignKey('Event.event_id'))
	)

class Event(db.Model):

	id = db.Column(db.Integer, primary_key = True)
	host = db.Column(db.String(24), nullable=False)
	title = db.Column(db.String(24), nullable=False)
	desc = db.Column(db.String(144), nullable=False)
	start = db.Column(db.DateTime, nullable=False)
	end = db.Column(db.DateTime, nullable=False)

	#many to many
	users = db.relationship('User', backref='Event', lazy = 'dynamic')
	
	def __init__(title, desc, start, end, host):
			self.title = title
			self.desc = desc
			self.start = start
			self.end = end
			self.host = host
