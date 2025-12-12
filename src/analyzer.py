from textblob import TextBlob

def get_sentiment(text):
    """
    Input: A string of text.
    Output: A dictionary containing the label, color, and score.
    """
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity
    subjectivity = blob.sentiment.subjectivity

    # Determine the label and color based on the score
    if polarity > 0.1:
        return {
            "label": "Positive",
            "score": polarity,
            "subjectivity": subjectivity,
            "color": "green",
            "emoji": "😊"
        }
    elif polarity < -0.1:
        return {
            "label": "Negative",
            "score": polarity,
            "subjectivity": subjectivity,
            "color": "red",
            "emoji": "😠"
        }
    else:
        return {
            "label": "Neutral",
            "score": polarity,
            "subjectivity": subjectivity,
            "color": "gray",
            "emoji": "😐"
        }