from flask import Blueprint, render_template, redirect, flash, g, sessions, request, url_for
from src.db.db import db
from src.models.TaskModel import Task
from src.models.UserMode import User
from src.auth.function import login_required, get_task, get_task_query

task_router = Blueprint("Task", __name__)


@task_router.route("/tareas")
@login_required
def task():
    tareas = Task.query.all()
    return render_template("public/task.html", task_ = tareas)


@task_router.route("/create", methods =['GET','POST'])
@login_required
def create_task():
     if request.method == "POST":
        title_ = request.form['title']
        des = request.form['description']
        #-----------------------------------------------
         # if a user is found, we want to redirect back to signup page so user can try again
        new_task = Task(create_by=g.user.id,title=title_, description=des)
        exits_task = Task.query.filter_by(create_by=g.user.id).first() 
        
        if exits_task:
           flash('Esta Tarea ya esta creada')
           return redirect(url_for("Task.create_task"))
        else:
         db.session.add(new_task)
         db.session.commit()
         flash(f"Tarea Creada")
         return redirect(url_for('Task.task'))
     
     return render_template("public/create_task.html")    



@task_router.route("/update/<int:id>", methods=('GET', 'POST'))
@login_required
def update(id):
    task_ = get_task(id)

    if request.method == "POST":
      task_.title = request.form['titulo_']
      task_.description = request.form['description_']
      task_.state = True if request.form.get("status") == "on" else False

      try:
         db.session.commit()
         return redirect(url_for("Task.task"))
      except Exception as e:
         print(f"Error al Insertar la Tarea")
    return render_template("public/edit_task.html", edit_task = task_)



@task_router.route("/delete/<int:id>")
@login_required
def delete(id):
   try:
    tarea = get_task(id)
    db.session.delete(tarea)
    db.session.commit()
    flash("Tarea Eliminada Correctamente!")
   except Exception as e:
      print(f"Error al Borrar la tarea {e}")
   return redirect(url_for("Task.task"))