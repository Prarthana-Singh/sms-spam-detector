


import streamlit as st
import pickle
from nltk.corpus import stopwords
import nltk
from nltk.stem.porter import PorterStemmer
import string

# Download NLTK resources
nltk.download('punkt')
nltk.download('stopwords')

# Initialize PorterStemmer
ps = PorterStemmer()

# Text transformation function
def transform_text(text):
    if not text.strip():
        return ""  # Handle empty input
    text = text.lower()
    text = nltk.word_tokenize(text)

    y = []
    for i in text:
        if i.isalnum():
            y.append(i)

    text = y[:]
    y.clear()

    for i in text:
        if i not in stopwords.words('english') and i not in string.punctuation:
            y.append(i)

    text = y[:]
    y.clear()

    for i in text:
        y.append(ps.stem(i))

    return " ".join(y)

# Load the vectorizer and model
try:
    tfidf = pickle.load(open('vectorizer.pkl', 'rb'))
    model = pickle.load(open('model.pkl', 'rb'))
except Exception as e:
    st.error(f"Error loading model or vectorizer: {e}")

# Streamlit UI
st.set_page_config(page_title="SMS Spam Detector", page_icon="📩", layout="centered")

# Header
import streamlit as st

# Display a small image
st.image("https://png.pngtree.com/png-vector/20231116/ourmid/pngtree-sms-red-circle-web-glossy-icon-read-sms-png-image_10550188.png", width=150)  # Adjust the width as needed
st.title("📩 SMS Spam Detector")
st.write("Enter a message to check if it's Spam or Not.")

# Sidebar
with st.sidebar:
    st.header("About")
    st.write("This app detects whether an SMS message is spam or not using machine learning.")
    st.write("Built with ❤️ by Prarthana Singh⭐")
    st.markdown("---")
    st.write("© 2025 SMS Spam Detector. All rights reserved.")
    st.write("[GitHub Repository](https://github.com/Prarthana-Singh/sms-spam-detector)")

# Text input
input_sms = st.text_area("Enter SMS Here:", "")

# Predict button
if st.button('🔍 Predict'):
    if not input_sms.strip():
        st.warning("Please enter a message.")
    else:
        # 1. preprocess
        transformed_sms = transform_text(input_sms)
        # st.write("Transformed Text:", transformed_sms)  # Debugging

        # 2. vectorize
        vector_input = tfidf.transform([transformed_sms])
        # st.write("Vectorized Input Shape:", vector_input.shape)  # Debugging

        # 3. predict
        result = model.predict(vector_input)[0]
        # st.write("Prediction Result:", result)  # Debugging

        # Display result
        if result == 1:
            st.error("🚨 Spam Message Detected!")
        else:
            st.success("✅ This is NOT a Spam Message.")
            st.balloons()
