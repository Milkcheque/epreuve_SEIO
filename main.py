import flask
from app import App

app = App()

# Page principale
@app.flask_app.route('/', methods=['GET', 'POST'])
def home():
    return flask.render_template('home.html')

app.flask_app.run()