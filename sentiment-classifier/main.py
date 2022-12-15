import requests

API_URL = "https://api-inference.huggingface.co/models/w11wo/indonesian-roberta-base-sentiment-classifier"
headers = {"Authorization": "Bearer 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"}


def query(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.json()


def main():
    # read test.txt file
    with open("3.txt", encoding="utf-8") as f:
        lines = f.readlines()

    # remove newlines
    lines = [line.rstrip() for line in lines]

    # query API
    for line in lines:
        result = []
        payload = {"inputs": line}
        result.append(line)
        response = query(payload)

        # get all scores from response
        for item in response:
            for label in item:
                if label["label"] == "positive":
                    result.append(label["score"])

        for item in response:
            for label in item:
                if label["label"] == "negative":
                    result.append(label["score"])

        for item in response:
            for label in item:
                if label["label"] == "neutral":
                    result.append(label["score"])

        # print result
        print(result)
        # write result to csv file
        with open("result_3.csv", "a", encoding="utf-8") as f:
            f.write(",".join(map(str, result)) + "\n")


if __name__ == "__main__":
    main()
