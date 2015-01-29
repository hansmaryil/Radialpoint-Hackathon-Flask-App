from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(64), index=True, unique=False)
    last_name = db.Column(db.String(64), index=True, unique=False)    
    email = db.Column(db.String(120), index=True, unique=True)

    def __repr__(self):
        return '<User %r>' % (self.first_name, self.last_name)