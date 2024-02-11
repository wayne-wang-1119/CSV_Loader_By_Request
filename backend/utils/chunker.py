import pandas as pd


def chunk_csv(file_path, chunk_size):
    """Yields chunks of a CSV file as DataFrames."""
    chunk_iterator = pd.read_csv(file_path, chunksize=chunk_size)
    for chunk in chunk_iterator:
        yield chunk
