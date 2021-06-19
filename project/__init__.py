from flask import Flask, render_template



######################################
#### Application Factory Function ####
######################################

def create_app():
    # Create the Flask application
    app = Flask(__name__)

    from flask_assets import Bundle, Environment
    assets = Environment(app)
    css = Bundle("src/main.css", output="dist/main.css", filters="postcss")
    assets.register("css", css)
    css.build()

    register_blueprints(app)
    register_error_pages(app)
    return app


########################
### Helper Functions ###
########################

def register_blueprints(app):
    # Import the blueprints
    from project.pages import pages_blueprint
    app.register_blueprint(pages_blueprint)


def register_error_pages(app):
    @app.errorhandler(404)
    def page_not_found(e):
        return render_template('404.html'), 404
