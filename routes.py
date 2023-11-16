from flask import Flask, request, jsonify, render_template, redirect, url_for
from models import UserModel, TodoModel, Session, engine
from sqlalchemy.orm import scoped_session

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

# Add additional CRUD routes for UserModel and TodoModel here

if __name__ == "__main__":
    app.run(debug=True)
