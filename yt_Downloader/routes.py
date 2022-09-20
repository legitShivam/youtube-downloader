from yt_Downloader import app
from flask import render_template, redirect, url_for, flash
from yt_Downloader.forms import videoLinkForm


@app.route("/", methods=['GET', 'POST'])
def home_page():
    form = videoLinkForm()
    if form.validate_on_submit():
        link = form.link.data()
        return redirect(url_for('home_page'))
    return render_template("index.html", form=form)


@app.route("/settings")
def settings_page():
    return render_template("settings.html")


@app.route("/about us")
def about_us_page():
    return render_template("about us.html")




# @app.route("/register", methods=['GET', 'POST'])
# def register_page():
#     form = RegisterForm()
#     if form.validate_on_submit():
#         name = form.name.data
#         userName = form.userName.data
#         password = form.password.data
#         confirmPassword = form.confirmPassword.data
#         character = form.character.data
#         return redirect(url_for('home_page'))
#     if form.errors != {}:   # If there are no errors i.e error dictionary is empty
#         for err_msg in form.errors.values():
#             flash(err_msg)
#     return render_template('register.html', form=form)


@app.route("/instructions")
def instructions_page():
    form = LoginForm()
    return render_template('instructions.html', form=form)

