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

@app.route('/todos/create', methods=['POST'])
def create_todo():
	body = {}
	error = False

	try:
		description = request.get_json()['description']
		todo = Todo(description=description)
		body['description'] = todo.description
		db.session.add(todo)
		db.session.commit()
	except:
		error = True
		db.session.rollback()
		print(sys.exc_info())
	finally:
		db.session.close()
		if error == True:
			abort(400)
		else
			return (jsonify(body)

@app.route('/')
def index():
	return render_template('index.html', data=Todo.query.all())

# run todo app
if __name__ == '__main__':
	app.debug = True
	app.run(host="0.0.0.0")
