from flask import Flask, flash, redirect, render_template, request, session, abort, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:qwe123@localhost/postgres'
db = SQLAlchemy(app)

class Publisher(db.Model):
	__tablename__ = 'publisher'
	name = db.Column(db.String(255), unique=True, nullable=False, primary_key=True)
	email = db.Column(db.String(255), nullable=False)
	publisher = db.relationship('Application', cascade='all, save-update, delete, delete-orphan')

class Application(db.Model):
	name = db.Column(db.String(255), unique=True, nullable=False, primary_key=True)
	publisher = db.Column(db.String(255), db.ForeignKey('publisher.name', onupdate="CASCADE"))
	rating = db.Column(db.Float, nullable=False)
	genre = db.Column(db.String(255), nullable=False)

db.create_all()

db.session.query(Application).delete()
db.session.query(Publisher).delete()
db.session.commit()

p1 = Publisher(name="Boogle", email="boogle@boogle.com")
p2 = Publisher(name="ZeptoFacility", email="zepto@zepto.com")
p3 = Publisher(name="Wolf Group", email="wolf@wolf.com")
p4 = Publisher(name="Fullbricks Studios", email="brick@brick.com")
a1 = Application(name="MeTube", publisher="Boogle", rating=4.4, genre="Family")
a2 = Application(name="Tear the Rope", publisher="ZeptoFacility", rating=4.2, genre="Puzzle")
a3 = Application(name="Wolf Rahm Beta", publisher="Wolf Group", rating=4.9, genre="Books")
a4 = Application(name="PaperBoard", publisher="Boogle", rating=4.1, genre="Entertainment")
a5 = Application(name="Jetpack Pleasureride 2", publisher="Fullbricks Studios", rating=4.8, genre="Racing")
db.session.add(p1)
db.session.add(p2)
db.session.add(p3)
db.session.add(p4)
db.session.commit()
db.session.add(a1)
db.session.add(a2)
db.session.add(a3)
db.session.add(a4)
db.session.add(a5)
db.session.commit()

@app.route("/")
def hello():
	application = Application.query.all()
	publisher = Publisher.query.all()
	app_name = 'Application'
	pub_name = 'Publisher'
	return render_template('index.html', app=application, pub=publisher, app_name=app_name, pub_name=pub_name)

# CREATE
@app.route('/<table>/Create', methods=['post'])
def add(table):
	if table == 'Application':
		name = request.form.get('name')
		publisher = request.form.get('publisher')
		rating = request.form.get('rating')
		genre = request.form.get('genre')
		result = Application(name=name, publisher=publisher, rating=rating, genre=genre)
	elif table == 'Publisher':
		name = request.form.get('name')
		email = request.form.get('email')
		result = Publisher(name=name, email=email)
	try:
		db.session.add(result)
		db.session.commit()
	except Exception:
		return redirect(url_for('hello'))
	return redirect(url_for('hello'))

# UPDATE
@app.route('/<table>/Update', methods=['post'])
def update(table):
	if table == 'Application':
		for k,v in request.form.items():
			original_name = ':'.join(k.split(':')[1:])
			name = v
			break
		publisher = request.form.get('publisher')
		rating = request.form.get('rating')
		genre = request.form.get('genre')
		application = db.session.query(Application).get(original_name)
		application.name = name
		application.publisher = publisher
		application.rating = rating
		application.publisher = publisher
		application.genre = genre
	elif table == 'Publisher':
		for k,v in request.form.items():
			original_name = ':'.join(k.split(':')[1:])
			name = v
			break
		email = request.form.get('email')
		publisher = db.session.query(Publisher).get(original_name)
		publisher.name = name
		publisher.email = email
	try:
		db.session.commit()
	except Exception:
		return redirect(url_for('hello'))
	return redirect(url_for('hello'))

# DELETE
@app.route('/<table>/Delete/<name>')
def delete(table,name):
	if table == 'Application':
		data = Application.query.all()
	elif table == 'Publisher':
		data = Publisher.query.all()
	for d in data:
		if d.name == name:
			db.session.delete(d)
			db.session.commit()
	return redirect(url_for('hello'))


if __name__ == "__main__":
	app.run()