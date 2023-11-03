import os
import pytest
from models import create_tables, seed_users, UserModel, engine, Session

# Setup and Teardown methods
@pytest.fixture(scope='module')
def setup_module():
    # Set the DATABASE_URL to point to a test database
    os.environ["DATABASE_URL"] = 'sqlite:///test_models.db'
    
    # Create tables and seed users for tests
    create_tables()
    seed_users()
    
    yield

    # Cleanup: Close the engine and remove the test database file
    engine.dispose()
    if os.path.exists('test_models.db'):
        os.unlink('test_models.db')

# Test functions
def test_user_count(setup_module):
    session = Session()
    user_count = session.query(UserModel).count()
    session.close()
    assert user_count >= 2, "Should have at least two seeded users"

def test_user_full_name(setup_module):
    session = Session()
    user = session.query(UserModel).first()
    full_name = user.full_name
    session.close()
    assert ' ' in full_name, "Full name should have a space between first and last name"
