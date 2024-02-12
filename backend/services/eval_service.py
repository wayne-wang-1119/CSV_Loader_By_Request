import requests
import openai as OpenAI
from dotenv import load_dotenv
import os


class GPTService:
    """
    we use here to query the GPT Service as a module
    """

    def __init__(self, api_key):
        load_dotenv()
        OpenAI.api_key = os.getenv("OPENAI_API_KEY")

    def query(self, prompt):
        try:
            response = OpenAI.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {
                        "role": "system",
                        "content": "You are a helpful copilot that only returns True and False, and is conducting tests on csv file inputs. The test to run and data are given to you as contents from the user. Return your test result and test result only. ",
                    },
                    {"role": "user", "content": prompt},
                ],
            )
            return response.choices[0].message.content.strip()
        except Exception as e:
            print(f"An error occurred: {e}")
            return None
