from datetime import datetime
from sqlalchemy import Column, DateTime, Integer, String, create_engine, MetaData
from sqlalchemy.orm import declarative_base, sessionmaker
from factories import user_factory

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
            f' last_name={self.last_name}, birth={self.birth},' 
            f' created={self.created})'
        )

engine = create_engine('sqlite:///models.db')
Session = sessionmaker(bind=engine)

def create_tables():
    Base.metadata.create_all(engine)

def create_users(number_of_users=10):  # Default to generating 10 users
    session = Session()
    users = [user_factory(UserModel) for _ in range(number_of_users)]
    session.add_all(users)
    session.commit()
    session.close()

if __name__ == "__main__":
    create_tables()
    create_users()

    session = Session()
    user_records = session.query(UserModel).all()
    for user in user_records:
        print(user.full_name)
    session.close()
