from flask import Flask

from apps.app1.routes import app1


def create_app():
    app = Flask(__name__)
    app.register_blueprint(app1)
    return app


if __name__ == "__main__":
    create_app().run()
