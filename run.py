from src.main import app
from src.db.db import db, migrate

migrate.init_app(app, db)

db.init_app(app)

with app.app_context():
    db.create_all()

if __name__ == "__main__":
    app.run()
    