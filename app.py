import streamlit as st
from text_module import analyze_text
from image_module import classify_image
from speech_module import text_to_speech

st.set_page_config(page_title="AI Multi System", layout="centered")
st.title("🤖 AI Multi-Feature System")
st.write("An integrated AI system for Text, Image, and Speech processing")
st.markdown("---")

tab1, tab2, tab3 = st.tabs(["🧠 Text", "🖼️ Image", "🎤 Speech"])

# TEXT
with tab1:
    st.header("🧠 Text Sentiment Analysis")
    user_text = st.text_input("Enter your text")
    if st.button("Analyze Text"):
        st.write(analyze_text(user_text))

# IMAGE
with tab2:
    st.subheader("🖼️ Image Processing")
    uploaded_file = st.file_uploader("Upload an image")
    if uploaded_file:
        from PIL import Image
        import tempfile
        # Show image
        image = Image.open(uploaded_file)
        st.image(image, caption="Uploaded Image", use_column_width=True)
        # Save temporarily for processing
        with tempfile.NamedTemporaryFile(delete=False) as tmp:
            tmp.write(uploaded_file.getvalue())
            result = classify_image(tmp.name)
        st.write("Prediction:", result)


# SPEECH (Text → Voice)
with tab3:
    st.header("🎤 Text to Speech")
    speech_text = st.text_input("Enter text to speak")
    if st.button("Speak"):
        text_to_speech(speech_text)

st.markdown("---")
st.subheader("📊 Project Overview")
st.write("""
This AI Multi-Feature System integrates:

• Natural Language Processing (Text Sentiment Analysis)  
• Computer Vision (Image Processing using OpenCV)  
• Speech Processing (Text-to-Speech using gTTS)  

The system is modular, scalable, and designed using Python and Streamlit.
""")

with st.sidebar:
    st.title("Controls")
    if st.button("🔄 Reset App"):
        st.experimental_rerun()

    if st.button("❌ Exit"):
        st.stop()