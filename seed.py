from models import SessionLocal, UserModel, Base, engine  # Import Base and engine
from factories import user_factory

def seed_users(session, user_model_class, number_of_users=10):
    users = [user_factory(user_model_class) for _ in range(number_of_users)]
    session.add_all(users)
    session.commit()
    print(f"Seeded {number_of_users} users to the database.")

if __name__ == "__main__":
    # Create the database schema
    Base.metadata.create_all(engine)  # Ensure all tables are created

    # Create a session and seed users
    session = SessionLocal()
    seed_users(session, UserModel, 20)  # Seed the database with 20 users
    session.close()
