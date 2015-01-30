from app import db

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(64), index=True, unique=False)
    last_name = db.Column(db.String(64), index=True, unique=False)    
    email = db.Column(db.String(120), index=True, unique=False)

    def __init__(self, first_name, last_name, email):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email

    def __repr__(self):
        return '<id {}>'.format(self.id)