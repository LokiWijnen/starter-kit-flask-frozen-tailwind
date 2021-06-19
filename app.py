import os, sys
from flask_frozen import Freezer
from project import create_app

app = create_app()

DEBUG = True
app.config.from_object(__name__)

freezer = Freezer(app)

if __name__ == '__main__':
    # To generate the static site files into the build directory:
    # `python3 app.py build`
    if len(sys.argv) > 1 and sys.argv[1] == "build":
        freezer.freeze()

    # To run the site in development mode:
    # `python3 app.py`
    else:
        app.run(port=5000, debug=True)
