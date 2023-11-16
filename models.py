from datetime import datetime
from sqlalchemy import Column, DateTime, Integer, String, Boolean, create_engine, MetaData
from sqlalchemy.orm import declarative_base, sessionmaker
import os

Base = declarative_base()

class UserModel(Base):
    __tablename__ = 'user'
    
    id = Column(Integer, primary_key=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    birth = Column(DateTime)
    created = Column(DateTime, default=datetime.utcnow)
    
    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'
    
    def __repr__(self):
        return (
            f'UserModel (id={self.id}, first_name={self.first_name},'
            f'last_name={self.last_name}, birth={self.birth},' 
            f'created={self.created})'
        )

class TodoModel(Base):
    __tablename__ = 'todo'
    
    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    description = Column(String)
    completed = Column(Boolean, default=False)
    created = Column(DateTime, default=datetime.utcnow)

    def __repr__(self):
        return (
            f'TodoModel (id={self.id}, title={self.title}, description={self.description},'
            f'completed={self.completed}, created={self.created})'
        )

DATABASE_URL = os.environ.get('DATABASE_URL', 'sqlite:///models.db')
engine = create_engine(DATABASE_URL)

Session = sessionmaker(bind=engine)

def create_tables():
    Base.metadata.create_all(engine)

def drop_tables():
    """Drop all tables in the database."""
    Base.metadata.drop_all(engine)

# The functions for creating users and seeding can remain the same.
# You might want to add similar functions for Todos if needed.

if __name__ == "__main__":
    # Uncomment the line below to drop tables
    # drop_tables()

    # Create and seed tables
    create_tables()
    # create_users()  # Uncomment to create users
    # seed_users()  # Uncomment to seed users

    # Print all user full names
    session = Session()
    user_records = session.query(UserModel).all()
    for user in user_records:
        print(user.full_name)
    
    # If you have todos to print, you can do so here
    # todo_records = session.query(TodoModel).all()
    # for todo in todo_records:
    #     print(todo)

    session.close()
