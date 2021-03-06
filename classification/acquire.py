import pandas as pd
import env

def get_connection(db, user=env.username, host=env.hostname, password=env.password):
    return f'mysql+pymysql://{user}:{password}@{host}/{db}'

def get_titanic_data():
    return pd.read_sql('SELECT * FROM passengers', get_connection('titanic_db'))

def get_iris_data():
    return pd.read_sql('SELECT m.*, s.species_name FROM measurements m JOIN species s USING(species_id)', get_connection('iris_db'))