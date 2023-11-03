from datetime import datetime
from sqlalchemy import Column, DateTime, Integer, String, create_engine, MetaData
from sqlalchemy.orm import declarative_base, sessionmaker

Base = declarative_base()

class UserModel(Base):
    __tablename__ = 'user'
    
    id = Column(Integer, primary_key=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    birth = Column(DateTime)
    created = Column(DateTime, default=datetime.utcnow)
    
    def __repr__(self):
        return (
            f'UserModel (id={self.id}, first_name={self.first_name},'
            f'last_name={self.last_name}, birth={self.birth},' 
            f'created={self.created})'
        )
    
engine = create_engine('sqlite:///models.db')
Session = sessionmaker(bind=engine)

def create_tables():
    Base.metadata.create_all(engine)

def create_users():
    session = Session()
    users = [
        UserModel(first_name='Bob', last_name='Preston', birth=datetime(1980, 5, 2)),
        UserModel(first_name='Susan', last_name='Sage', birth=datetime(1979, 6, 12)),
    ]
    for user in users:
        session.add(user)
    session.commit()
    session.close()

if __name__ == "__main__":
    create_tables()
    create_users()

    session = Session()
    user_records = session.query(UserModel).all()
    for user in user_records:
        print(user)
    session.close()
