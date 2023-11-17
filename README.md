# MidTerm-IS373
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
... (111 lines left)