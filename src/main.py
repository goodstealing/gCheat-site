from flask import render_template, Blueprint

main = Blueprint('main', __name__)


@main.route('/')
def main_page():
    return render_template("main_page.html")


@main.route('/сheat-catalog')
def cheat_catalog_page():
    return render_template("сheat_catalog.html")


@main.route('/about-site')
def about_site_page():
    return render_template("about_site.html")


@main.route('/policy')
def policy_page():
    return render_template("policy.html")


@main.route('/сheat-catalog/CS2-midnight')
def midnight_page():
    return render_template("CS2_midnight.html")


@main.route('/сheat-catalog/minecraft-wurst')
def wurst_page():
    return render_template("minecraft_wurst.html")


@main.route('/сheat-catalog/rust-phoenix')
def phoenix_page():
    return render_template("rust_phoenix.html")
