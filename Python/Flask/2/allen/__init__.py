from flask import Flask

def create_app(test_config=None):
    app = Flask(__name__)
    app.secret_key = 'Alvin333#'

    from . import allen
    app.register_blueprint(allen.bp)

    return app