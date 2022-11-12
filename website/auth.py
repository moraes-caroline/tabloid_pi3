from unicodedata import category
from flask import Blueprint, render_template, request, flash, redirect, url_for
from sqlalchemy import null
from .models import User
from .models import Estabelecimentos
from . import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, login_required, logout_user, current_user 




auth = Blueprint('auth', __name__)

@auth.route('/login',  methods=['GET', 'POST'])
def login():
    data = request.form
    print(data)
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        

        user = User.query.filter_by(email=email).first()
        
        if user:
            if check_password_hash(user.password, password):
                 flash('Logado com sucesso', category='success')
                 login_user(user, remember=True)
                 
                 return redirect(url_for("views.admin", user=current_user))
            else:
                flash('Incorreto password, tente novamente!', category='error')
        else:
            flash('Email não existente', category='error')
       
    return render_template('login.html', user=current_user)

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('views.home'))

@auth.route('/cadastro', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        nome_empresa = request.form.get('nome_empresa')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        user = User.query.filter_by(email=email).first()

        if user:
            flash('Email deve ser informado', category='error')
        if len(email)< 4:
            flash('email deve ter mais de 4 caracteres', category='error')
        elif len(nome_empresa) < 2:
            flash(' nome deve ter mais de um caractere', category='error')
        elif len(password1) < 6:
            flash(' Senha deve ter mais de 6 caractere', category='error')
        elif (password2) != password1:
            flash('Senhas não correspondentes', category='error')
        else:
            # add user to database
            new_user = User(email=email, nome_empresa=nome_empresa, password=generate_password_hash(password1,  method='sha256'))
            db.session.add(new_user)
            db.session.commit()

           # comercio = Estabelecimentos(nome=nome_mercado)
          #  db.session.add(comercio)
         #   db.session.commit()
            #login_user(user, remember=True)
            flash('conta criado com sucesso!', category='success')
            return redirect(url_for('views.home'))




    return render_template('cadastro.html')
