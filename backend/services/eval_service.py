import requests


class GPTService:
    def __init__(self, api_key):
        self.api_key = api_key
        self.api_url = "https://api.openai.com/v1/chat/completions"

    def query(self, prompt, max_tokens=100, temperature=0.5, top_p=1.0, n=1):
        headers = {"Authorization": f"Bearer {self.api_key}"}
        data = {
            "model": "gpt-3.5-turbo",
            "prompt": prompt,
            "max_tokens": max_tokens,
            "temperature": temperature,
            "top_p": top_p,
            "n": n,
        }
        response = requests.post(self.api_url, headers=headers, json=data)
        if response.status_code == 200:
            return response.json()["choices"][0]["text"].strip()
        else:
            print(f"Error querying GPT-3.5: {response.text}")
            return None
