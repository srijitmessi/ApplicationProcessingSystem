import os.path

db_path = os.path.abspath(os.path.dirname(__file__))
db_uri = 'sqlite:///{}'.format(db_path)
database_path = os.path.join(db_uri, r'db\users.db')
db_repository = os.path.join(db_path, r'db_repository')
host_path = "localhost"
port = 5000
debug = True
