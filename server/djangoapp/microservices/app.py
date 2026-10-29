from flask import Flask
from nltk.sentiment import SentimentIntensityAnalyzer
import json

app = Flask("Sentiment Analyzer")

sia = SentimentIntensityAnalyzer()


@app.get('/')
def home():
    return "Welcome to the Sentiment Analyzer. Use /analyze/text to get the sentiment"


@app.get('/analyze/<path:input_txt>')
def analyze_sentiment(input_txt):
    scores = sia.polarity_scores(input_txt)
    print(scores)
    pos = float(scores['pos'])
    neg = float(scores['neg'])
    neu = float(scores['neu'])
    compound = float(scores['compound'])

    if compound > 0.05 or (pos > neg and pos > neu):
        res = "positive"
    elif compound < -0.05 or (neg > pos and neg > neu):
        res = "negative"
    else:
        res = "neutral"

    response = json.dumps({"sentiment": res})
    print(response)
    return response, 200, {'Content-Type': 'application/json'}


if __name__ == "__main__":
    app.run(port=5050, debug=True)
