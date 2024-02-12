# Assuming this is part of eval_route.py
from flask import Blueprint, request, jsonify, send_from_directory
from services.eval_service import GPTService
import os
from dotenv import load_dotenv
import pandas as pd
from services.data_service import load_and_process_csv

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")  ## get open ai api key, set it up in .env

eval_blueprint = Blueprint("eval", __name__)
gpt_service = GPTService(
    api_key=api_key
)  ## custome defiend class for calling gpt, should include a callback


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
        serialized_records = load_and_process_csv(file_path, chunk_size=500)
        evaluations = []
        for record in serialized_records:
            response = gpt_service.query(f"{prompt}\n{record}", max_tokens=100)
            if response:
                evaluations.append(response)
            else:
                evaluations.append("Error or no response from GPT-3.5")

        # Save evaluations to a new CSV
        eval_file_path = os.path.join(os.getcwd(), "evaluations.csv")
        pd.DataFrame(evaluations).to_csv(eval_file_path, index=False)

        return send_from_directory(
            directory=os.path.dirname(eval_file_path),
            filename=os.path.basename(eval_file_path),
            as_attachment=True,
        )
    except Exception as e:
        return jsonify(error=str(e)), 500
