# Assuming this is part of eval_route.py
from flask import Blueprint, request, jsonify
from services.eval_service import GPTService
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

eval_blueprint = Blueprint("eval", __name__)
gpt_service = GPTService(api_key=api_key)


@eval_blueprint.route("/evaluate", methods=["POST"])
def evaluate():
    data = request.json
    prompt = data.get("prompt")
    records = data.get("records")

    if not prompt or not records:
        return jsonify(error="Missing prompt or records"), 400

    evaluations = []
    for record in records:
        response = gpt_service.query(
            "For the data below, answer if they meet the requirements mentioned in prompt\n"
            + f"{prompt}\n{record}",
            max_tokens=100,
        )
        if response:
            evaluations.append(response)
        else:
            evaluations.append("Error or no response from GPT-3.5")

    return jsonify({"evaluations": evaluations}), 200
