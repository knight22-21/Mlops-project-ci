from textblob import TextBlob

def analyze_sentiment(text):
    polarity = TextBlob(text).sentiment.polarity
    if polarity > 0:
        return "Positive"
    elif polarity < 0:
        return "Negative"
    else:
        return "Neutral"

def test_positive_sentiment():
    text = "I absolutely love this!"
    assert analyze_sentiment(text) == "Positive"

def test_negative_sentiment():
    text = "This is the worst thing ever."
    assert analyze_sentiment(text) == "Negative"

def test_neutral_sentiment():
    text = "The cat is on the mat."
    assert analyze_sentiment(text) == "Neutral"

def test_boundary_case_positive():
    # A slightly positive sentence
    text = "This is fine."
    assert analyze_sentiment(text) == "Positive"

def test_boundary_case_negative():
    # A slightly negative sentence
    text = "Not great."
    assert analyze_sentiment(text) == "Negative"

def test_empty_string():
    text = ""
    assert analyze_sentiment(text) == "Neutral"
    
def test_whitespace_string():
    text = "   "
    assert analyze_sentiment(text) == "Neutral" 
    

