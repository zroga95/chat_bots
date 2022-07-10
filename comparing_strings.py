from nltk.sentiment import SentimentIntensityAnalyzer
import re
import numpy as np


def getClosestSentiment(lines, input_str):
    sia = SentimentIntensityAnalyzer()
    line_sentiment = []
    for i in lines:
        scores = sia.polarity_scores(i)
        line_sentiment.append(scores)
    submitted_sent = sia.polarity_scores(input_str)
    sent_diff = np.zeros(len(lines))
    for item in submitted_sent.items():
        cat = item[0]
        for i in range(0, len(lines)):
            #sum of 
            sent_diff[i] += (item[1] - line_sentiment[i][cat])**2
    output_str = lines[np.where(sent_diff==sent_diff.min())[0][0]]
    return output_str