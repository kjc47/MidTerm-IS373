# factories.py
from faker import Faker
from models import UserModel

fake = Faker()

def user_factory():
    return UserModel(
        first_name=fake.first_name(),
        last_name=fake.last_name(),
        birth=fake.date_of_birth()
    )
