import requests

API_URL = "https://api-inference.huggingface.co/models/w11wo/indonesian-roberta-base-sentiment-classifier"
headers = {"Authorization": "Bearer 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"}


def query(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.json()


if __name__ == "__main__":
    payload = {"inputs": "Saya sangat senang dengan film ini"}
    print(query(payload))
