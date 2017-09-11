import imp, datetime
from migrate.versioning import api
from app import db
from config import db_repository,database_path
v = api.db_version(database_path, db_repository)
migration = db_repository + ('/versions/%03d_migration.py' % (v+1))
tmp_module = imp.new_module('old_model')
old_model = api.create_model(database_path, db_repository)
exec(old_model, tmp_module.__dict__)
script = api.make_update_script_for_model(database_path, db_repository, tmp_module.meta, db.metadata)
open(migration, "wt").write(script)
api.upgrade(database_path, db_repository)
v = api.db_version(database_path, db_repository)
with open('logs.txt','a') as f:
    f.write(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")+' > New migration saved as ' + migration)
    f.write(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")+' > Current database version: ' + str(v))
