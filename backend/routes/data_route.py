# Assuming this is part of data_route.py
from flask import Blueprint, request, jsonify
from werkzeug.utils import secure_filename
from services.data_service import load_and_process_csv
import os
import tempfile

data_blueprint = Blueprint("data", __name__)


@data_blueprint.route("/upload", methods=["POST"])
async def upload_file():
    """
    We use this function to handle file uploads, right now we accept csv files. We store them temp on server because it is easy to implement it this way for now
    """
    if "file" not in request.files:
        return jsonify(error="No file part"), 400
    file = request.files["file"]
    if file.filename == "":
        return jsonify(error="No selected file"), 400
    if file and file.filename.endswith(".csv"):
        filename = secure_filename(file.filename)
        wd = os.getcwd()
        file_path = os.path.join(wd, filename)
        print(file_path)
        file.save(file_path)
        return jsonify({"file": file_path}), 200
    else:
        return jsonify(error="Unsupported file type"), 400
