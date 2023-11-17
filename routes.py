from flask import Flask, request, jsonify, render_template, redirect, url_for
from models import UserModel, TodoModel, SessionLocal, engine
from sqlalchemy.orm import sessionmaker, scoped_session

app = Flask(__name__)

# Set up the session for the database
session_factory = sessionmaker(bind=engine)
Session = scoped_session(session_factory)

@app.route('/')
def index():
    """Show all users and todos."""
    session = Session()
    users = session.query(UserModel).all()
    todos = session.query(TodoModel).all()
    Session.remove()
    return render_template('index.html', users=users, todos=todos)

# User Routes
@app.route('/users/<int:user_id>')
def get_user(user_id):
    """Retrieve a single user by ID."""
    session = Session()
    user = session.query(UserModel).get(user_id)
    Session.remove()
    if user:
        return jsonify(user.full_name)
    else:
        return jsonify(error="User not found"), 404

# Todo Routes
@app.route('/todos/create', methods=['GET', 'POST'])
def create_todo():
    """Create a new todo item."""
    if request.method == 'POST':
        title = request.form['title']
        description = request.form['description']
        new_todo = TodoModel(title=title, description=description)
        session = Session()
        session.add(new_todo)
        session.commit()
        Session.remove()
        return redirect(url_for('index'))
    return render_template('create_todo.html')

@app.route('/todos/update/<int:todo_id>', methods=['GET', 'POST'])
def update_todo(todo_id):
    """Update an existing todo item."""
    session = SessionLocal()
    todo = session.get(TodoModel, todo_id)
    if request.method == 'POST':
        if todo:
            todo.title = request.form['title']
            todo.description = request.form['description']
            session.commit()
        Session.remove()
        return redirect(url_for('index'))
    return render_template('update_todo.html', todo=todo)

@app.route('/todos/delete/<int:todo_id>', methods=['POST'])
def delete_todo(todo_id):
    """Delete a todo item."""
    session = Session()
    todo = session.get(TodoModel, todo_id)
    if todo:
        session.delete(todo)
        session.commit()
    Session.remove()
    return redirect(url_for('index'))

@app.route('/todos/<int:todo_id>')
def get_todo(todo_id):
    """Retrieve a single todo item."""
    session = Session()
    todo = Session.get(TodoModel, todo_id)
    Session.remove()
    return render_template('todo_view.html', todo=todo)

if __name__ == "__main__":
    app.run(debug=True)
