# MidTerm-IS373
First Make sure to use commands 
echo $DATABASE_URL
export DATABASE_URL='sqlite:///test_models.db' ### test database 
export DATABASE_URL='sqlite:///models.db' ###Main Database 
python models.py 
alembic revision --autogenerate -m "Test Migration"
python seed.py 
pytest



