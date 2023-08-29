#!/usr/bin/env python3
"""
Basic Flask APP
"""
from flask import Flask, render_template, request, globals
from flask_babel import Babel


app = Flask(__name__)


class Config:
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)
babel = Babel(app)


@babel.localeselector
def get_locale():
    locale = request.args.get('locale')
    if locale and locale in app.config['LANGUAGES']:
        return locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user():
    login_as = request.args.get('login_as')
    if not login_as and login_as not in users.keys():
        return None
    return users.get(int(login_as))


@app.before_request
def before_request():
    globals.g.setdefault(request.args.get('login_as'), get_user())


@app.route("/")
def hello():
    user = globals.g.get(request.args.get('login_as'))
    username = user.get('name')
    return render_template('5-index.html', username=username)


if __name__ == '__main__':
    app.run(port=5000)
