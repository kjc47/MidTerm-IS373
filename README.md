# MidTerm-IS373 
By Kevin Chavez, Nadzeya Kuzmitch, Robin Pierre
First Make sure to use commands 
echo $DATABASE_URL
export DATABASE_URL='sqlite:///test_models.db' ### test database 
export DATABASE_URL='sqlite:///models.db' ###Main Database 
python models.py #### generates people with age in database 
alembic revision --autogenerate -m "description of your change"

python seed.py ### seeds the data 
pytest



Part 1: Introduction to SQLAlchemy, Alembic, and Pytest

SQLAlchemy - SQLAlchemy is an Object-Relational Mapping (ORM) toolkit for Python. It allows developers to interact with a database using Python classes and objects, abstracting away the complexities of raw SQL queries

Alembic - Alembic as a database migration tool specifically designed to be used with SQLAlchemy. It's used to track, manage, and apply changes to the database schema.

Pytest - powerful testing framework for Python. It's used for writing and running tests, offering a simple syntax for test cases.

How They Work Together

SQLAlchemy manages the application's data model and database interactions.
Alembic tracks and applies changes to the database schema as the data model evolves.
Pytest ensures that changes in the application and database do not break functionality, maintaining the integrity and reliability of the application.


Part 2: Setup and Installation

Virtual Environment Setup

    What is a Virtual Environment?
        Virtual environment is an isolated Python environment that allows you to manage dependencies for different projects separately.

    Creating a Virtual Environment
        Run python -m venv venv (This creates a virtual environment named venv within the project directory).
    Activate the virtual environment:
        Windows: venv\Scripts\activate
        macOS/Linux: source venv/bin/activate
    Installing Packages
        SQLAlchemy Installation - Command: pip install sqlalchemy
        Alembic Installation - Command: pip install alembic
        Pytest Installation - Command: pip install pytest
        Faker Installation - Command: pip install faker

    Project Structure Setup
         Setting up a basic project structure for organization 
            /models: Directory for SQLAlchemy models.
            /migrations: Directory for Alembic migration scripts.
            /tests: Directory for Pytest test cases.
            /factories: Directory for data factory functions (using Faker).

Part 3: Creating Models with SQLAlchemy
    Creating the UserModel Class
        Provide the UserModel class code as shown in the provided scripts.
        Walk through each line of the class, explaining:
            __tablename__: Names the table in the database.
            Columns (id, first_name, last_name, birth, created): Define the table structure.
            Data types (Integer, String, DateTime): SQLAlchemy types representing SQL data types.
            Primary keys, nullable fields, and default values.
    Setting up the SQLAlchemy Base and Engine
        Declarative Base
            Base = declarative_base() and its role as the base class for all models.
        Creating the Database Engine
            create_engine(DATABASE_URL)
    Creating a Database Session
        staging ground for all the objects loaded into the database session object.
        to create a session factory using Session = sessionmaker(bind=engine)

Part 4: Managing Migrations with Alembic
    What are Migrations? 
        Migrations, in the context of a database, are a way to manage, track, and apply changes to a database schema over time. They are particularly important in software development for several reasons:
            Version Control for Database Schema
            Managing Schema Changes
            Facilitating Collaboration
            Safe Application Updates
            Automating Database Setup
            Tracking Database History
    Role of Alembic in Managing Migrations
        Tool that integrates with SQLAlchemy to manage these schema changes. It keeps track of changes using migration scripts, allowing for a version-controlled approach to database schema modifications
    Setting Up Alembic
        Initializing Alembic in the Project
            alembic init migrations to initialize Alembic, which creates a new directory (migrations) containing Alembic configuration and script directories.
        Configuring Alembic
            .ini file, specifically setting the sqlalchemy.url to match the application's database URL.
    Creating a Migration Script
        Generating a New Migration
            alembic revision --autogenerate -m "description". Alembic compares the current database schema with the model definitions to generate these scripts.
        Understanding the Migration Script
            Open a generated script in the versions directory. The upgrade() and downgrade() functions, which define how to apply and revert the migration, respectively.
    Applying Migrations
        Running Migrations
            To apply migrations to the database, use the alembic upgrade head command. This applies all pending migrations up to the latest ("head").
            To revert migrations, if necessary, using alembic downgrade

Part 5: Implementing Factories for Fake Data
    Introduction to Faker and Data Factories
        What is Faker?
            Faker is a Python library used to generate fake but realistic-looking data.
Benefits of Using Data Factories
        Provides a consistent and easy way to generate test data.
        Helps in populating databases with data that mimics real-world scenarios without using sensitive real data.
        Enhances the robustness of tests by using diverse and dynamic data sets.
    Creating a User Factory Function
        Factory Function Setup
            user_factory example: 

                from faker import Faker

                fake = Faker()

                def user_factory(UserModel):
                    return UserModel(
                        first_name=fake.first_name(),
                        last_name=fake.last_name(),
                        birth=fake.date_of_birth()
                    )

        fake = Faker(): Initializes a Faker instance to generate fake data.
        user_factory(UserModel): A function that takes a UserModel class and returns an instance of it filled with fake data.
        How Faker methods like fake.first_name() and fake.date_of_birth() are used to populate the fields.

    Using the User Factory in the Application
        Implementing the Factory
             example of how to use the user_factory to create a user object:
                new_user = user_factory(UserModel)
Part 6: Seeding the Database
    What is Database Seeding?
        The process of populating a database with initial data.
    Preparing the Seed Function
        The seed_users Function:

            from models import Session, UserModel
            from factories import user_factory

        def seed_users(number_of_users=10):
            session = Session()
            users = [userfactory(UserModel) for  in range(number_of_users)]
            session.add_all(users)
            session.commit()
            session.close()
            print(f"Seeded {number_of_users} users to the database.")

    Break down the function and explain each part:
        number_of_users=10: A default parameter that specifies the number of users to be created.
        session = Session(): Initiates a new database session.
        user_factory(UserModel): Uses the factory to generate user instances.
        session.add_all(users): Adds all the user instances to the session.
        session.commit(): Commits the transaction, saving the data to the database.
        session.close(): Closes the session after the operation is complete.

    Executing the Seed Script
        Running the Seeding Process
            This can be done directly within a Python shell or as part of an application's setup process.
            Example:

                python -c "from seed_script import seed_users; seed_users(20)"
Part 7: Testing with Pytest
    Overview of Pytest
         Flexible and easy-to-use testing framework for Python. Highlight its features like simple syntax, powerful fixtures, and extensive plugin support.
    Setting Up Test Environment
        Creating a Pytest Fixture for Database Session:

            import pytest
            from models import Session, create_tables, UserModel, engine

            @pytest.fixture(scope="module")
            def db_session():
                create_tables()  # Create tables in the test database
                session = Session()  # Start a new session
                yield session  # Use the session in tests
                session.close()  # Close the session after tests
                UserModel.table.drop(engine)  # Clean up the database

    Writing Test Cases
        Example of basic test function with Pytest using db_session 

            def test_user_creation(db_session):
            # Your test code here

    Running Tests
         using the pytest command