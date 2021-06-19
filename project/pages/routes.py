from . import pages_blueprint
from flask import render_template


@pages_blueprint.route('/')
def home():
    return render_template('pages/home.html')
