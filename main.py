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
    if(app.user.get_user_log()):
        return redirect(url_for('home'))
    if request.method == 'POST':
        id = request.form.get("user-id")
        pwd = request.form.get("password")
        if verify_user_id(id):
            if verify_password(id, pwd):
                app.user.id = id
                app.user.set_user_log(True)
                return redirect(url_for('dashboard_page'))
            else:
                return render_template('login.html', error="Mot de passe incorrect")
        else:
            return render_template('login.html', error="Identifiant incorrect")
    return render_template('login.html')

# Page de déconnexion
@app.flask_app.route('/logout', methods=['GET', 'POST'])
def logout_page():
    app.user.set_user_log(False)
    return render_template('logout.html')

# Page de dashboard
@app.flask_app.route('/dashboard', methods=['GET', 'POST'])
def dashboard_page():
    if(not app.user.get_user_log()):
        return redirect(url_for('home'))
    
    error = ""
    to_be_confirmed = False

    if request.method == 'POST':
        new_pwd = request.form.get("new-pwd")
        confirmed_pwd = request.form.get("confirmed-pwd")
        new_tagline = request.form.get("new-tagline")
        in_confirmation = request.form.get("is_confirmed")
        if new_pwd != None and confirmed_pwd != None:
            # Si le nouveau mot de passe est le même que l'ancien
            if verify_password(app.user.id, new_pwd):
                error = 'Entrez un nouveau mot de passe différent du précédent.'
            # Si le nouveau mot de passe et celui de confirmation sont identiques 
            elif new_pwd == confirmed_pwd:
                app.user.pwd = new_pwd
                to_be_confirmed = True
            # Cas où les mots de passe ne sont pas identiques 
            else:
                error = 'Entrez le même mot de passe pour le confirmer.'

            return render_template('dashboard.html',    tagline=get_website_component("tagline"),
                                                        logged= app.user.get_user_log(), 
                                                        error=error,
                                                        in_confirmation=to_be_confirmed)
            
        if in_confirmation:
            change_password(app.user.id, app.user.pwd)
            app.user.pwd = ""
        
        if new_tagline != None:
            modify_tagline(new_tagline)
    return render_template('dashboard.html', tagline=get_website_component("tagline"),
                                            logged= app.user.get_user_log())

app.flask_app.run()