from flask import Blueprint, render_template, url_for

auth = Blueprint('auth', __name__)


@auth.route('/profile')
def profile_page():
    return render_template("profile.html")


@auth.route('/sign-up')
def sign_up_page():
    return render_template("sign_up.html")


@auth.route('/login')
def login_page():
    return render_template("login.html")


@auth.route('/logout')
def logout():
    return "sd"


@auth.route('/user/<username>')
def profile(username):
    if username == 'goodstealing':
        return f'Профиль пользователя {username}'
    else:
        return 'Пользователь не найден', 404