from faker import Faker
from datetime import datetime

fake = Faker()

def user_factory(UserModel):  # Notice UserModel is now a parameter
    return UserModel(
        first_name=fake.first_name(),
        last_name=fake.last_name(),
        birth=fake.date_of_birth()
    )

def todo_factory(TodoModel):  # Adding a factory function for TodoModel
    return TodoModel(
        title=fake.sentence(nb_words=4),  # Generates a fake sentence with 4 words
        description=fake.text(max_nb_chars=200),  # Generates a piece of text with a maximum of 200 characters
        completed=fake.boolean(chance_of_getting_true=25),  # 25% chance to be True
        created=fake.date_time_this_year(before_now=True, after_now=False, tzinfo=None)  # Random date/time from this year
    )
