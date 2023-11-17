import pytest
from flask_testing import TestCase
from models import UserModel, TodoModel, SessionLocal, init_db, engine, Base
from routes import app
from seed import seed_users

# Set up a fixture for database session
@pytest.fixture(scope="module")
def db_session():
    init_db()  # Initialize the database schema
    session = SessionLocal()
    seed_users(session, UserModel, 20)  # Seed the database
    yield session
    session.close()
    Base.metadata.drop_all(engine)  # Clean up after tests

# Test case class using Flask-Testing
class MyTest(TestCase):

    # This is a Flask-Testing method to create a Flask application instance
    def create_app(self):
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False
        return app

    # Set up the test database and seed it
    def setUp(self):
        super().setUp()
        init_db()
        self.db_session = SessionLocal()
        seed_users(self.db_session, UserModel, 20)  # Seed with 20 user instances for testing
        todo = TodoModel(title="Todo Title", description="A test todo")
        self.db_session.add(todo)
        self.db_session.commit()
        self.todo_id = todo.id  # Store the ID of the new todo for use in tests
        self.db_session.close()


    # Teardown the test database
    def tearDown(self):
        self.db_session.close()
        Base.metadata.drop_all(engine)

    # Test creating a todo
    def test_create_todo(self):
        response = self.client.post('/todos/create', data={
            'title': 'Test Todo',
            'description': 'Test Description'
        }, follow_redirects=True)
        print(response.data) 
        self.assertEqual(response.status_code, 200)
        self.assertIn('Test Todo', response.data.decode())

    # Test getting a todo
    def test_get_todo(self):
        # Use the stored todo_id
        response = self.client.get(f'/todos/{self.todo_id}')
        self.assertEqual(response.status_code, 200)
        self.assertIn('Todo Title', response.data.decode())
    # Test updating a todo
    def test_update_todo(self):
        # Use the stored todo_id
        response = self.client.post(f'/todos/update/{self.todo_id}', data={
            'title': 'Updated Todo',
            'description': 'Updated Description'
        }, follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn('Updated Todo', response.data.decode())

    # Test deleting a todo
    def test_delete_todo(self):
        # Use the stored todo_id
        response = self.client.post(f'/todos/delete/{self.todo_id}', follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        # Additional check to ensure the todo has been deleted
        response = self.client.get(f'/todos/{self.todo_id}')
        self.assertNotIn('Todo Title', response.data.decode()) # Additional check can be performed to ensure the todo has been deleted

# This allows running the tests via the command line
if __name__ == '__main__':
    pytest.main()
