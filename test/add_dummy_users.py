from create_db import db
from app.models import User
admin = User('admin', 'admin','fac')
guest = User('student', 'student','stud')
db.session.add(admin)
db.session.add(guest)
db.session.commit()
