# MidTerm-IS373
First Make sure to use commands 
echo $DATABASE_URL
export DATABASE_URL='sqlite:///test_models.db' ### test database 
export DATABASE_URL='sqlite:///models.db' ###Main Database 
python models.py #### generates people with age in database 
alembic current
alembic revision --autogenerate -m "description of your change"

python seed.py ### seeds the data 
pytest
