import functools
import re
from flask import redirect, url_for, g, flash
from src.models.TaskModel import Task


def login_required(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.user is None:
           flash(f"No tienes acceso a esta pagina")
           return redirect(url_for('I.index'))
        return view(**kwargs)
    return wrapped_view


def verificate_regular(params):
    patron = re.compile(r'[^a-zA-Z0-9]')
    return bool(patron.search(params))


def get_task(id):
  get = Task.query.get_or_404(id)
  return get


def get_task_query(parametro):
  get = Task.query.filter_by(title=parametro).first()
  return get