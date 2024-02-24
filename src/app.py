from flask import Flask, render_template, url_for

# Основной файл для работы с Flask
app = Flask(__name__)


@app.route('/')
def main_page():
    return render_template("main_page.html")


@app.route('/сheat-catalog')
def cheat_catalog_page():
    return render_template("сheat_catalog.html")


@app.route('/profile')
def profile_page():
    return render_template("profile.html")


@app.route('/profile/<string:name>')
def profile_page_str(name):
    return f"This is the temporary page of the {name} user."


@app.route('/about-site')
def about_site_page():
    return render_template("about_site.html")


@app.route('/policy')
def policy_page():
    return render_template("policy.html")


@app.route('/sign-up')
def sign_up_page():
    return render_template("sign_up.html")


@app.route('/login')
def login_page():
    return render_template("login.html")


@app.route('/сheat-catalog/CS2-midnight')
def midnight_page():
    return render_template("CS2_midnight.html")


@app.route('/сheat-catalog/minecraft-wurst')
def wurst_page():
    return render_template("minecraft_wurst.html")


@app.route('/сheat-catalog/rust-phoenix')
def phoenix_page():
    return render_template("rust_phoenix.html")


if __name__ == "__main__":
    app.run(debug=True)
