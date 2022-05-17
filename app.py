from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# initialize todo app
app = Flask(__name__)

# connect to todo app database
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:2135@localhost:5432/todoapp'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# create a database instance
db = SQLAlchemy(app)

# create a migrate instance
migrate = Migrate(app, db)

# create class for Todo app
class Todo(db.Model):
	__tablename__ = 'todos'

	# todos table columns
	id = db.Column(db.Integer, primary_key=True)
	description = db.Column(db.String(), nullable=False)
	completed = db.Column(db.Boolean, nullable=False, default=False)

	# wrapper method
	def __repr__(self):
		return f'<Todo id = {self.id} description = {self.description}'

# run todo app
if __name__ == '__main__':
	app.debug = True
	app.run(host="0.0.0.0")
