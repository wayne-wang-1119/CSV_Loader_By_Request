# Assuming this is part of data_route.py
from flask import Blueprint, request, jsonify
from werkzeug.utils import secure_filename
from services.data_service import load_and_process_csv
import os

data_blueprint = Blueprint("data", __name__)


@data_blueprint.route("/upload", methods=["POST"])
def upload_file():
    if "file" not in request.files:
        return jsonify(error="No file part"), 400
    file = request.files["file"]
    if file.filename == "":
        return jsonify(error="No selected file"), 400
    if file and file.filename.endswith(".csv"):
        filename = secure_filename(file.filename)
        file_path = os.path.join("/tmp", filename)
        file.save(file_path)
        serialized_records = load_and_process_csv(file_path, chunk_size=500)
        os.remove(file_path)
        return jsonify({"processed_records": serialized_records}), 200
    else:
        return jsonify(error="Unsupported file type"), 400
