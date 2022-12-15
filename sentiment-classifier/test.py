def main():
    data = [
        [
            {"label": "positive", "score": 0.9987772107124329},
            {"label": "neutral", "score": 0.0007797925500199199},
            {"label": "negative", "score": 0.0004430696426425129},
        ],
        [
            {"label": "negative", "score": 0.9876170754432678},
            {"label": "neutral", "score": 0.006823385134339333},
            {"label": "positive", "score": 0.00555954547598958},
        ],
        [
            {"label": "neutral", "score": 0.9876170754432678},
            {"label": "negative", "score": 0.006823385134339333},
            {"label": "positive", "score": 0.00555954547598958},
        ],
    ]

    print(data[0][0]["label"], data[0][0]["score"])

    # get all scores from data
    for item in data:
        for label in item:
            if label["label"] == "positive":
                print(label["label"], label["score"])

    for item in data:
        for label in item:
            if label["label"] == "negative":
                print(label["label"], label["score"])

    for item in data:
        for label in item:
            if label["label"] == "neutral":
                print(label["label"], label["score"])


if __name__ == "__main__":
    main()
