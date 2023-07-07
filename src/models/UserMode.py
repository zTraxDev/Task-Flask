from src.db.db import db


class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable = False)
    password = db.Column(db.String(100), nullable = False)


    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password


    def search_name(self, name):
        return User.query.filter_by(username=name).first()
    
    def search_email(self, email):
        return User.query.filter_by(email=email).first()
        
    def __rep__(self):
        return f'<Nombre: {self.username}>'