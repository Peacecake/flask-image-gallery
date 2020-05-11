from flask import Flask
import os


def create_app():
    app = Flask(__name__)
    app.secret_key = "mysupersecretkey"
    app.config["ALLOWED_EXTENSIONS"] = {"png", "jpg", "jpeg", "gif", "bmp"}
    app.config["UPLOAD_PATH"] = os.path.join(
        os.getcwd(), "flaskapp", "static", "img", "uploads")

    from flaskapp.blueprints import images
    app.register_blueprint(images.bp)

    return app
