import datetime
from models import create_tables, UserModel, engine, Session, seed_users
from factories import user_factory
import pytest

@pytest.fixture(scope="module")
def db_session():
    # Create tables
    create_tables()

    # Create a new session
    session = Session()

    yield session  # this is where the testing happens

    session.close()
    # Drop all tables after tests
    UserModel.__table__.drop(engine)

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
    assert user.full_name == "John Doe"

def test_created_field(db_session):
    now = datetime.datetime.utcnow()
    user = UserModel(first_name="Jane", last_name="Doe")
    db_session.add(user)
    db_session.commit()

    user_from_db = db_session.query(UserModel).filter_by(first_name="Jane").first()
    assert user_from_db.created >= now

def test_seed_users(db_session):
    seed_users()
    user_count = db_session.query(UserModel).count()
    assert user_count >= 2
