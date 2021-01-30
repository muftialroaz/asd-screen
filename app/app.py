from flask import Flask


def create_app(config=None):
    """Menginisiasi app untuk dijalankan oleh flask"""
    from . import routes

    app = Flask(__name__, template_folder="templates")
    if config is not None:
        if isinstance(config, dict):
            app.config.update(config)
        elif config.endswith('.py'):
            app.config.from_pyfile(config)
    else:
        app.config.from_pyfile("config.py")

    # models.init_app(app)
    routes.init_app(app)

    return app
