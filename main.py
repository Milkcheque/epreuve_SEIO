from flask import render_template, redirect, url_for, request
from app import App
from SQLite_query import *

app = App()

# Page principale
@app.flask_app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('home.html', tagline=get_website_component("tagline"),
                                        logged= app.user.get_user_log())

# Page de connexion
@app.flask_app.route('/login', methods=['GET', 'POST'])
def login_page():
    if request.method == 'POST':
        id = request.form.get("user-id")
        pwd = request.form.get("password")
        if verify_user_id(id):
            if verify_password(id, pwd):
                app.user.id = id
                app.user.set_user_log(True)
                return redirect(url_for('dashboard_page'))
            else:
                return render_template('login.html',    tagline=get_website_component("tagline"),
                                                        error="Mot de passe incorrect")
        else:
            return render_template('login.html',    tagline=get_website_component("tagline"),
                                                    error="Identifiant incorrect")
    return render_template('login.html', tagline=get_website_component("tagline"))

# Page de déconnexion
@app.flask_app.route('/logout', methods=['GET', 'POST'])
def logout_page():
    app.user.set_user_log(False)
    return render_template('logout.html', tagline=get_website_component("tagline"))

# Page de dashboard
@app.flask_app.route('/dashboard', methods=['GET', 'POST'])
def dashboard_page():
    if request.method == 'POST':
        new_pwd = request.form.get("new-pwd")
        confirmed_pwd = request.form.get("confirmed-pwd")
        new_tagline = request.form.get("new-tagline")
        if new_pwd != None and confirmed_pwd != None:
            if new_pwd == confirmed_pwd and not verify_password(app.user.id, new_pwd):
                change_password(app.user.id, new_pwd)   #TODO popup de confirmation
            else:
                return render_template('dashboard.html', tagline=get_website_component("tagline"))
        if new_tagline != None:
            modify_tagline(new_tagline)
    return render_template('dashboard.html', tagline=get_website_component("tagline"))

#TODO faire navbar_component.html pour pouvoir la mettre aux pages voulues

app.flask_app.run()