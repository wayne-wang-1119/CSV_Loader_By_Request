# Assuming this is part of eval_route.py
from flask import Blueprint, request, jsonify, send_from_directory
from services.eval_service import GPTService
import os
from dotenv import load_dotenv
import pandas as pd
from services.data_service import load_and_process_csv
import traceback
from utils.report_generator import ReportGenerator

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")  ## get open ai api key, set it up in .env

eval_blueprint = Blueprint("eval", __name__)
gpt_service = GPTService(
    api_key=api_key
)  ## custome defiend class for calling gpt, should include a callback

reporter = ReportGenerator(
    eval_file_path=os.path.join(os.getcwd(), "evaluations.csv"),
    original_file_path=os.path.join(os.getcwd(), "file.csv"),
)


@eval_blueprint.route("/evaluate", methods=["POST"])
async def evaluate():
    """
    We use this to chunk and send each chunk to GPT to ask for a test result, this is my knowledge of how testing works
    """
    prompt = request.json.get("prompt")
    file_path = request.json.get("file")

    if not prompt or not file_path:
        return jsonify(error="Missing prompt or file path"), 400

    try:
        serialized_records = load_and_process_csv(file_path, chunk_size=1000)
        evaluations = []

        reporter.original_file_path = file_path
        for record in serialized_records:
            # response = gpt_service.query(f"{prompt}\n{record}")
            # if response:
            #     evaluations.append(response)
            # else:
            #     evaluations.append("Error or no response from GPT-3.5")
            evaluations.append("True")
        # Save evaluations to a new CSV
        eval_file_path = os.path.join(os.getcwd(), "evaluations.csv")
        evaluations_df = pd.DataFrame(evaluations, columns=["Result"])
        evaluations_df.to_csv(eval_file_path, index=False, mode="w")
        reporter.eval_file_path = eval_file_path
        df = reporter.generate_report()
        print(df)
        return jsonify({"file": eval_file_path})
    except Exception as e:
        error_details = traceback.format_exc()
        print(error_details)  # Log to console for debugging.
        return jsonify({"error": str(e), "details": error_details}), 500


@eval_blueprint.route("/evaluation_results", methods=["GET"])
async def get_evaluation_results():
    try:
        df = reporter.generate_report()
        return jsonify(df.to_dict(orient="records"))
    except Exception as e:
        return jsonify(error=str(e)), 500
