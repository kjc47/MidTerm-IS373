from flask import Flask, render_template, redirect, url_for, flash
from models import UserModel, TodoModel, SessionLocal, engine
from sqlalchemy.orm import scoped_session, sessionmaker
from forms import TodoForm
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(24).hex()  # Set a random SECRET_KEY for CSRF protection

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
        return render_template('user_view.html', user=user)
    else:
        flash('User not found', 'error')
        return redirect(url_for('index'))

# Todo Routes
@app.route('/todos/create', methods=['GET', 'POST'])
def create_todo():
    """Create a new todo item."""
    form = TodoForm()
    if form.validate_on_submit():
        session = Session()
        new_todo = TodoModel(title=form.title.data, description=form.description.data)
        session.add(new_todo)
        session.commit()
        Session.remove()
        flash('Todo created successfully!', 'success')
        return redirect(url_for('index'))
    return render_template('create_todo.html', form=form)

@app.route('/todos/update/<int:todo_id>', methods=['GET', 'POST'])
def update_todo(todo_id):
    """Update an existing todo item."""
    session = Session()
    todo = session.query(TodoModel).get(todo_id)
    form = TodoForm(obj=todo)
    if form.validate_on_submit():
        todo.title = form.title.data
        todo.description = form.description.data
        session.commit()
        Session.remove()
        flash('Todo updated successfully!', 'success')
        return redirect(url_for('index'))
    Session.remove()
    return render_template('update_todo.html', form=form, todo_id=todo_id)

@app.route('/todos/delete/<int:todo_id>', methods=['POST'])
def delete_todo(todo_id):
    """Delete a todo item."""
    session = Session()
    todo = session.query(TodoModel).get(todo_id)
    if todo:
        session.delete(todo)
        session.commit()
        flash('Todo deleted successfully!', 'success')
    else:
        flash('Todo not found', 'error')
    Session.remove()
    return redirect(url_for('index'))

@app.route('/todos/<int:todo_id>')
def get_todo(todo_id):
    """Retrieve a single todo item."""
    session = Session()
    todo = session.query(TodoModel).get(todo_id)
    Session.remove()
    if todo:
        return render_template('todo_view.html', todo=todo)
    else:
        flash('Todo not found', 'error')
        return redirect(url_for('index'))

if __name__ == "__main__":
    app.run(debug=True)
