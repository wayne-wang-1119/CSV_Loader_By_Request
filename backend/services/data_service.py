from utils.chunker import chunk_csv
import json


def load_and_process_csv(file_path, chunk_size=500):
    """Loads CSV in chunks, processes each chunk."""
    processed_records = []
    try:
        for chunk in chunk_csv(file_path, chunk_size):
            serialized_records = process_chunk(chunk)
            processed_records.extend(serialized_records)
    except Exception as e:
        return f"Error occurred: {str(e)}"
    return processed_records


def process_chunk(chunk):
    """Process chunk with pandas to make readable content for LLMs."""
    records = chunk.to_dict(orient="records")
    serialized_records = [json.dumps(record) for record in records]
    return serialized_records
