import datetime
import config
from create_db import db, User
admin = User('admin', 'admin')
guest = User('student', 'student')
db.session.add(admin)
db.session.add(guest)
db.session.commit()
