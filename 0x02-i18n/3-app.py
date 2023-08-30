#!/usr/bin/env python3
"""
A basic Flask app
"""
from flask import Flask, render_template, request
from flask_babel import Babel, gettext


class Config(object):
    """
    Config class  that has a LANGUAGES class attribute equal to en/fr
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
babel = Babel(app)

app.config.from_object(Config)


@babel.localeselector
def get_locale():
    """
    Sets the best match language with the babel.localeselector decorator.
    """
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route("/", methods=["GET"], strict_slashes=False)
def index():
    """
    home/index route
    return: template
    """
    return render_template('3-index.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
