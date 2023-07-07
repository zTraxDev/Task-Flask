from flask import Blueprint, render_template, redirect, session, flash, url_for, g
from src.db.db import db
from src.models.UserMode import User
from src.models.TaskModel import Task
from src.auth.function import login_required, get_task
import base64
page_router = Blueprint("I", __name__)


@page_router.route("/")
def index():
    return render_template("public/index.html")

@page_router.route("/home")
@login_required
def home():
    task = Task.query.all()
    return render_template("public/home.html")


@page_router.route("/perfil/<int:id>")
@login_required
def perfil(id):
    if id != g.user.id:
        flash("No puedes ver el perfil de otro usuario")
        return redirect(url_for("I.perfil", id=g.user.id))
    return render_template("public/perfil.html")