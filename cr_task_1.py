# -*- coding: utf-8 -*-
"""CR-Task-1

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1eKwRdVpA56SOQInT7eiBv82UL894-Dwk
"""

!pip install emoji
import re
import pandas as pd
import numpy as np
import emoji
from collections import Counter
import matplotlib.pyplot as plt
from PIL import Image
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
# Extract the Date time
def date_time(s):
    pattern='^([0-9]+)(\/)([0-9]+)(\/)([0-9]+),([0-9]+):([0-9]+)[ ]?(AM|PM|am|pm)? -'
    result=re.match(pattern, s)
    if result:
        return True
    return False

# Extract contacts
def find_contact(s):
    s=s.split(":")
    if len(s)==2:
        return True
    else:
        return False

# Extract Message
def getMassage(line):
    splitline=line.split(' - ')
    datetime= splitline[0];
    date, time= datetime.split(', ')
    message=" ".join(splitline[1:])

    if find_contact(message):
        splitmessage=message.split(": ")
        author=splitmessage[0]
        message=splitmessage[1]
    else:
        author=None
    return date, time, author, message
data=[]
conversation='/content/sample_data/chat.txt'
with open(conversation, encoding="utf-8") as fp:
    fp.readline()
    messageBuffer=[]
    date, time, author= None, None, None
    while True:
        line=fp.readline()
        if not line:
            break
        line=line.strip()
        if date_time(line):
            if len(messageBuffer) >0:
                data.append([date, time, author, ''.join(messageBuffer)])
            messageBuffer.clear()
            date, time, author, message=getMassage(line)
            messageBuffer.append(message)
        else:
            messageBuffer.append(line)
import nltk
nltk.download('vader_lexicon')
print("Shape before dropping missing values:", df.shape)
data = df.dropna()
print("Shape after dropping missing values:", data.shape)
import pandas as pd
from nltk.sentiment.vader import SentimentIntensityAnalyzer

# Assuming 'data' is your initial DataFrame
df = pd.DataFrame(data, columns=["Date", "Time", "contact", "Message"])
df['Date'] = pd.to_datetime(df['Date'])

# Drop rows with missing values
data = df.dropna()

# Initialize SentimentIntensityAnalyzer
sentiments = SentimentIntensityAnalyzer()

# Create lists to store sentiment scores
positive_scores = []
negative_scores = []
neutral_scores = []

# Calculate sentiment scores
for message in data["Message"]:
    sentiment_score = sentiments.polarity_scores(message)
    positive_scores.append(sentiment_score["pos"])
    negative_scores.append(sentiment_score["neg"])
    neutral_scores.append(sentiment_score["neu"])

# Create new columns in the DataFrame for sentiment scores
data["positive"] = positive_scores
data["negative"] = negative_scores
data["neutral"] = neutral_scores

# Display the DataFrame
print(data.head(7))
x=sum(data["positive"])
y=sum(data["negative"])
z=sum(data["neutral"])

def score(a, b, c):
    if a > b and a > c:
        return "Positive"
    elif b > a and b > c:
        return "Negative"
    else:
        return "Neutral"

overall_sentiment = score(x, y, z)
print(overall_sentiment)