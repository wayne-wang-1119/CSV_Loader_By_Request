import pandas as pd


class ReportGenerator:
    """
    report class for generating data report after appending results to the dataframe
    """

    def __init__(self, format, eval_file_path, original_file_path) -> None:
        self.format = format
        self.eval_file_path = eval_file_path
        self.original_file_path = original_file_path

    def get_file_path(self):
        return self.eval_file_path

    def generate_report(self):
        result_df = pd.read_csv(self.eval_file_path, header=None, names=["Result"])
        original_df = pd.read_csv(self.original_file_path, header=None)
        report_df = pd.merge(left=original_df, right=result_df)
        return report_df
