import datetime
from models import UserModel, engine, SessionLocal, init_db
from factories import user_factory
from seed import seed_users

import pytest

@pytest.fixture(scope="module")
def db_session():
    # Initialize the database (create tables)
    init_db()

    # Create a new session
    session = SessionLocal()

    yield session  # this is where the testing happens

    # Teardown: close the session and drop all tables
    session.close()
    UserModel.metadata.drop_all(engine)

@pytest.fixture(scope="function")
def seed_database(db_session):
    # Seed the database with users, using a smaller number for testing
       db_session.query(UserModel).delete()
       db_session.commit()
       seed_users(db_session, UserModel, 5)
       db_session.commit()

       yield
       db_session.query(UserModel).delete()
       db_session.commit()
def test_user_creation(db_session):
    user = user_factory(UserModel)
    db_session.add(user)
    db_session.commit()

    fetched_user = db_session.query(UserModel).first()
    assert fetched_user is not None
    assert fetched_user.first_name == user.first_name
    assert fetched_user.last_name == user.last_name

def test_full_name_property(db_session):
    user = UserModel(first_name="John", last_name="Doe")
    db_session.add(user)
    db_session.commit()
    assert user.full_name == "John Doe"

def test_created_field(db_session):
    now = datetime.datetime.utcnow()
    user = UserModel(first_name="Jane", last_name="Doe")
    db_session.add(user)
    db_session.commit()

    user_from_db = db_session.query(UserModel).filter_by(first_name="Jane").first()
    time_buffer = datetime.timedelta(seconds=1)
    assert user_from_db.created <= now + time_buffer

def test_seed_users(db_session, seed_database):
    # seed_database fixture is used to seed users before the test
    user_count = db_session.query(UserModel).count()
    assert user_count == 5
