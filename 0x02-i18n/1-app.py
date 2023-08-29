#!/usr/bin/env python3
"""
Basic Flask app with a single route, an index.html template,
and integration of Flask-Babel extension.
"""

from flask import Flask, render_template
from flask_babel import Babel

app = Flask(__name__)
babel = Babel(app)


class Config:
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)


@app.route('/')
def index():
    """Render the index.html template."""
    return render_template('0-index.html')


if __name__ == '__main__':
    app.run()
