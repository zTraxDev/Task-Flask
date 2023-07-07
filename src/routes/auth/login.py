from flask import Blueprint, render_template, redirect, session, flash, url_for, g
from flask import request as req
from src.models.UserMode import User
from src.models.TaskModel import Task
from src.db.db import db
from src.auth.function import verificate_regular
from werkzeug.security import generate_password_hash, gen_salt, check_password_hash

login_router = Blueprint("L", __name__)


@login_router.route("/login", methods =['GET','POST'])
def login():
    if req.method == "POST":
    #Obtenemos los datos del Formulario
       email = req.form['txtUse']
       password = req.form['tpassword']
       a = User.query.filter_by(email=email).first()
       error = None

      #verificamos si el correo es correcto
       if User.search_email(User, email)  is None:
         flash('El usuario no existe')
         return redirect(url_for('L.login'))
      #Verificamos si la contraseña coincide con la de la Base de Datos
       elif not check_password_hash(a.password, password):
         flash(f'Contraseña Incorrecta')
         return redirect(url_for('L.login'))
      #Error de Seguridad
       elif error is None:
         session.clear()
         session["user_id"] = a.id
         return redirect(url_for("I.home"))
      #Retornamos un mensaje y redireccion si hay un error
       else:
         flash(f"El usuario Ya esta registrado")
         return redirect(url_for('L.login'))
     
    return render_template("auth/login.html")

@login_router.route("/register", methods =['GET','POST'])
def register():
     if req.method == "POST":
        username = req.form['user']
        email = req.form['email']
        password = req.form['password']

        hash_ = generate_password_hash(password=password, method="sha256", salt_length=16)
        #-----------------------------------------------
        if User.search_email(User, email): # if a user is found, we want to redirect back to signup page so user can try again
            flash('Este correo Electronico ya existe')
            return redirect(url_for('L.register'))
         
        elif verificate_regular(password):
            flash('La contraseña no puede tener caracteres especiales')
            return redirect(url_for('L.register'))
        
        elif User.search_name(User, username):
            flash('Este nombre ya existe')
            return redirect(url_for('L.register'))
        else:
            new_user = User(username=username, email=email, password=hash_)
            db.session.add(new_user)
            db.session.commit()
            flash(f"Cuenta {username} creada correctamente")
        return redirect(url_for('L.login'))
     
     return render_template("auth/register.html")    



@login_router.route("/logout")
def logout():
   session.clear()
   return redirect(url_for("I.index"))







@login_router.before_app_request
def load_login_user():
   user_id = session.get("user_id")

   if user_id is None:
      g.user = None
   else:
      g.user = User.query.get_or_404(user_id)