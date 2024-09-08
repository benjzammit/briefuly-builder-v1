from textblob import TextBlob

def analyze_sentiment(text):
    blob = TextBlob(text)
    sentiment = blob.sentiment
    return sentiment.polarity, sentiment.subjectivity

def interpret_sentiment(polarity, subjectivity):
    if polarity <= -0.5:
        polarity_text = "The brief has a very negative tone, which might not be engaging. Consider revising the content to include more positive and inspiring language."
    elif polarity < -0.1:
        polarity_text = "The brief has a somewhat negative tone. Ensure that the overall message remains optimistic and solution-oriented."
    elif polarity <= 0.1:
        polarity_text = "The brief has a neutral tone. Consider adding elements that evoke positive emotions to make your message more compelling."
    elif polarity <= 0.5:
        polarity_text = "The brief has a positive tone, which is generally engaging. Positive language can inspire and motivate your audience."
    else:
        polarity_text = "The brief has a very positive tone, which is highly engaging. A positive tone can significantly boost audience morale."

    if subjectivity <= 0.3:
        subjectivity_text = "The brief is very objective, focusing on facts. Consider incorporating some subjective elements like testimonials or personal stories."
    elif subjectivity <= 0.5:
        subjectivity_text = "The brief is fairly objective. Adding a bit more personal touch or opinion can make the content more relatable."
    elif subjectivity <= 0.7:
        subjectivity_text = "The brief is somewhat subjective, focusing on opinions. Ensure they are backed by facts to maintain credibility."
    else:
        subjectivity_text = "The brief is very subjective, focusing heavily on opinions. Balance it with factual information to strengthen your argument."

    return polarity_text, subjectivity_text
