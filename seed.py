# seed.py

from models import Session, UserModel
from factories import user_factory

def seed_users(number_of_users=10):
    session = Session()
    users = [user_factory(UserModel) for _ in range(number_of_users)]
    session.add_all(users)
    session.commit()
    session.close()
    print(f"Seeded {number_of_users} users to the database.")

if __name__ == "__main__":
    seed_users(20)  # Seed the database with 20 users
