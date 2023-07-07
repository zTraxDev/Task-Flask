from src.db.db import db
from src.models.UserMode import User

class Task(db.Model):
    __tablename__ = "task"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(100), nullable=False)
    status = db.Column(db.Boolean, default=False)
    create_by = db.Column(db.Integer, db.ForeignKey('users.username'), nullable = False)


    def __init__(self, create_by ,title, description, status = False):
        self.create_by = create_by
        self.title = title
        self.description = description
        self.status = status

    def search_title(self, title):
        return Task.query.filter_by(title=title).first()
    
    def search_state(self, state):
        return Task.query.filter_by(state=state).first()
    
    def __rep__(self):
        return f'<Task: {self.title}>'
