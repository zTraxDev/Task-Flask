from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from src.routes.auth.login import login_router
from src.routes.public.page import page_router
from src.routes.public.task import task_router
from src.routes.public.profile import perfil_router

app = Flask(__name__, template_folder="templates", static_folder="static")
db = SQLAlchemy()


app.register_blueprint(task_router)
app.register_blueprint(login_router)
app.register_blueprint(page_router)
app.register_blueprint(perfil_router)
app.config.from_mapping(
    DEBUG=True,
    SECRET_KEY = "test",
    SQLALCHEMY_DATABASE_URI = "sqlite:///task-app.sql"
)