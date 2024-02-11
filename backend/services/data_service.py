from utils.chunker import chunk_csv
import json


def load_and_process_csv(file_path, chunk_size=500):
    """Loads CSV in chunks, processes each chunk."""
    for chunk in chunk_csv(file_path, chunk_size):
        process_chunk(chunk)


def process_chunk(chunk):
    """Process chunk with pandas to make readable content for LLMs."""
    records = chunk.to_dict(orient="records")
    serialized_records = [json.dumps(record) for record in records]
    return serialized_records
