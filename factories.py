from faker import Faker

fake = Faker()

def user_factory(UserModel):  # Notice UserModel is now a parameter
    return UserModel(
        first_name=fake.first_name(),
        last_name=fake.last_name(),
        birth=fake.date_of_birth()
    )
