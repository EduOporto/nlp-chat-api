from sql_db.connectors.SQLAlch_connector import engine_connector

def db_creator(db_name, db_models=None):

    # Create the DB
    engine = engine_connector()
    engine.execute(f"CREATE DATABASE IF NOT EXISTS {db_name}")

    # Create tables if passed
    if db_models != None:
        db_models.create_all()

    return f"{db_name} created succesfully"