from flask import Blueprint, render_template, redirect, request, current_app, url_for, flash
import os
from werkzeug.utils import secure_filename

bp = Blueprint("images", __name__)


@bp.route("/")
def index():
    create_image_directory()
    return render_template("index.html", images=get_uploaded_images())


@bp.route("/upload", methods=["GET", "POST"])
def upload():
    if request.method == "POST":
        if "file" not in request.files:
            flash("No file part", "danger")
            return redirect(url_for("images.index"))

        file = request.files["file"]
        if file.filename == "":
            flash("No file selected", "danger")
            return redirect(url_for("images.index"))

        if not allowed_file(file.filename):
            flash("Wrong file type", "danger")
            return redirect(url_for("images.index"))

        save_image(file)

    return redirect(url_for("images.index"))


def save_image(file):
    if not file:
        return
    filename = secure_filename(file.filename)
    create_image_directory()
    file.save(os.path.join(current_app.config["UPLOAD_PATH"], filename))
    flash("Upload successfull", "success")


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower(
           ) in current_app.config["ALLOWED_EXTENSIONS"]


def create_image_directory():
    if not os.path.exists(current_app.config["UPLOAD_PATH"]):
        os.makedirs(current_app.config["UPLOAD_PATH"])


def get_uploaded_images():
    image_paths = []
    img_path = current_app.config["UPLOAD_PATH"]
    all_files = [f for f in os.listdir(
        img_path) if os.path.isfile(os.path.join(img_path, f))]
    for file in all_files:
        if allowed_file(file):
            image_paths.append(os.path.join("img", "uploads", file))
    return image_paths
