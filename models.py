from datetime import datetime
from sqlalchemy import Column, DateTime, Integer, String, create_engine, MetaData
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

DATABASE_URL = os.environ.get('DATABASE_URL', 'sqlite:///models.db')
engine = create_engine(DATABASE_URL)

Session = sessionmaker(bind=engine)

def create_tables():
    Base.metadata.create_all(engine)

def drop_tables():
    """Drop all tables in the database."""
    Base.metadata.drop_all(engine)

def create_users():
    session = Session()
    users = [
        # Add user instances here if needed
    ]
    for user in users:
        session.add(user)
    session.commit()
    session.close()

def seed_users(n=10):
    from factories import user_factory  # Ensure you have this factory module available
    session = Session()
    for _ in range(n):
        user = user_factory(UserModel)
        session.add(user)
    session.commit()
    session.close()

if __name__ == "__main__":
    # Uncomment the line below to drop tables
    # drop_tables()

    # Create and seed tables
    create_tables()
    create_users()
    seed_users()

    # Print all user full names
    session = Session()
    user_records = session.query(UserModel).all()
    for user in user_records:
        print(user.full_name)
    session.close()
