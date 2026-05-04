from textblob import TextBlob

def analyze_text(text):
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity

    if polarity > 0:
       return f"Sentiment: Positive 😊 (Score: {polarity})"
    elif polarity < 0:
        return f"Sentiment: Negative 😠 (Score: {polarity})"
    else:
        return f"Sentiment: Neutral 😐 (Score: {polarity})"

if __name__ == "__main__":
    text = input("Enter text: ")
    print(analyze_text(text))