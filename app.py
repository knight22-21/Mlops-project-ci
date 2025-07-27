import streamlit as st
from textblob import TextBlob

st.title("🧠 Basic Sentiment Analyzer")
st.write("Enter a sentence to see if it's Positive, Negative, or Neutral.")

text = st.text_area("Your text here:")

if text:
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity

    if polarity > 0:
        sentiment = "Positive 😊"
    elif polarity < 0:
        sentiment = "Negative 😠"
    else:
        sentiment = "Neutral 😐"

    st.write(f"**Sentiment:** {sentiment}")
    st.write(f"**Polarity Score:** {polarity:.3f}")
