from flask import Blueprint, render_template, redirect, url_for, g, session, request, flash
from src.db.db  import db
from src.models.TaskModel import Task
from src.models.UserMode import User
from src.auth.function import login_required, verificate_regular
from werkzeug.security import generate_password_hash, check_password_hash
perfil_router = Blueprint("Perfil", __name__)


@perfil_router.route("/cambiar_nombre/<int:id>", methods=('GET', 'POST'))
@login_required
def change_username(id: int):
   if id != g.user.id:
      return redirect(url_for("Perfil.change_username", id =g.user.id))

   if request.method == "POST":
      user_name= User.query.get_or_404(id)
      new_name = request.form['new_name']
      confirm_pass = request.form['password']
      check = check_password_hash(user_name.password, confirm_pass)

      if new_name == user_name.username:
         flash("Nombre de usuario ya existe")
         return redirect(url_for("Perfil.change_username", id =g.user.id))
      if not check:
         flash("Contraseña incorrecta")
         return redirect(url_for("Perfil.change_username", id =g.user.id))
      else:
           user_name.username = new_name
           db.session.commit()
           flash("Nombre cambiado Correctamente!")
           return redirect(url_for("I.perfil", id = g.user.id))
   return render_template("auth/change_username.html")

@perfil_router.route("/cambiar_email/<int:id>", methods=('GET', 'POST'))
@login_required
def change_email(id: int):
   user_pass = User.query.get_or_404(id)
   if id != g.user.id:
      return redirect(url_for("Perfil.change_email", id =g.user.id))
   

   if request.method == "POST":
      old_email = request.form['old_email']
      new_email =  request.form['new_email']

      if old_email != user_pass.email:
         flash("Correo incorrecto")
         return redirect(url_for("Perfil.change_email", id =g.user.id))
      if new_email == user_pass.email:
         flash("Correo Electronico ya existe")
         return redirect(url_for("Perfil.change_email", id =g.user.id))
      else:
           user_pass.email = new_email
           db.session.commit()
           flash("Correo cambiado Correctamente!")
           return redirect(url_for("I.perfil", id = g.user.id))
   return render_template("auth/change_gmail.html")


@perfil_router.route("/cambiar_contraseña/<int:id>", methods=('GET', 'POST'))
@login_required
def change_password(id: int):
    user_pass = User.query.get_or_404(id)
    if request.method == "POST":
        if id != g.user.id:
         return redirect(url_for("Perfil.change_password", id =g.user.id))
        
        password_old = request.form['old_password']
        password = request.form['new_password']
        check = check_password_hash(user_pass.password, password_old)
        hash_ = generate_password_hash(password, method="sha256")

        if not check:
           flash("Contraseña Incorrecta")
           return redirect(url_for("Perfil.change_password", id =g.user.id))
        elif verificate_regular(password):
           flash('La contraseña no puede tener caracteres especiales')
           return redirect(url_for('Perfil.change_password', id = g.user.id))
        else:
           user_pass.password = hash_
           db.session.commit()
           flash("Contraseña actualizada correctamente!")
           return redirect(url_for("I.perfil", id = g.user.id))
    return render_template("auth/change_password.html")