import os.path

db_path = os.path.abspath(os.path.dirname(__file__))
db_uri = 'sqlite:///{}'.format(db_path)
database_path = os.path.join(db_uri, 'db\users.db')
