from create_db import db
from models import User
admin = User('admin', 'admin')
guest = User('student', 'student')
db.session.add(admin)
db.session.add(guest)
db.session.commit()
