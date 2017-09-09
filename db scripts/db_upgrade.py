from migrate.versioning import api
import datetime
from config import database_path,db_repository
api.upgrade(database_path, db_repository)
v = api.db_version(database_path, db_repository)
with open('logs.txt','a') as f:
    f.write(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")+' > Current database version: ' + str(v))
