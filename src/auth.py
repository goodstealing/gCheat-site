from flask import Blueprint, render_template, url_for, request, redirect
from werkzeug.security import generate_password_hash
from .models import User
from . import db

auth = Blueprint('auth', __name__)


@auth.route('/profile')
def profile_page():
    return render_template("profile.html")


@auth.route('/signup')
def signup():
    return render_template("signup.html")


# POST запрос обработки регистрации
@auth.route('/signup', methods=['POST'])
def signup_post():
    email = request.form.get('email')
    name = request.form.get('name')
    password = request.form.get('password')

    # print(email, password)
    user = User.query.filter_by(email=email).first()
    if user:
        print("Пользователь с таким именем уже существует.")

    new_user = User(email=email, name=name, password=generate_password_hash(password, method='sha256'))
    db.session.add(new_user)
    db.session.commit()

    return redirect(url_for('auth.login'))


@auth.route('/login')
def login():
    return render_template("login.html")


@auth.route('/login', methods=['POST'])
def login_post():
    email = request.form.get('email')
    password = request.form.get('password')
    rememberme = request.form.get('rememberme')

    print(email, password, rememberme)

    return redirect(url_for('main.main_page'))


@auth.route('/logout')
def logout():
    return "sd"
