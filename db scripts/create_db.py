from app import db
from migrate.versioning import api
from config import database_path,db_repository
import os.path
if not os.path.exists(db_repository):
    api.create(db_repository, 'database repository')
    api.version_control(database_path, db_repository)
else:
    api.version_control(database_path, db_repository, api.version(db_repository))
db.create_all()
