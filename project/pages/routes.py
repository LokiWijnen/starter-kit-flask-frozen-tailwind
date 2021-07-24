from . import pages_blueprint
from flask import render_template


@pages_blueprint.route('/')
def home():
    return render_template('pages/home.html')


# This is specifically for netlify.com which is where the demo is currently hosted.
# Your hosting provider might need error pages handled differently.
# Please see the netlify.toml file in the root of the project for more info.
@pages_blueprint.route('/404/')
def static_error_404():
    return render_template('404.html')
