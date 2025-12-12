import streamlit as st
from src.analyzer import get_sentiment
from src.vision import analyze_face_emotion

st.set_page_config(page_title="Multimodal Sentiment AI", page_icon="🤖")

st.title("🤖 AI Emotion & Sentiment Detector")

# Create Tabs for different modes
tab1, tab2 = st.tabs(["📝 Text Analysis", "📸 Face Emotion"])

# --- TAB 1: Text Sentiment (Your old code) ---
with tab1:
    st.header("Analyze Text")
    user_text = st.text_area("Enter text:", height=100)
    
    if st.button("Analyze Text"):
        if user_text:
            result = get_sentiment(user_text)
            st.subheader(f"Result: {result['label']} {result['emoji']}")
            st.progress((result['score'] + 1) / 2)
        else:
            st.warning("Please type something.")

# --- TAB 2: Face Emotion (New Feature) ---
with tab2:
    st.header("Analyze Facial Expression")
    st.write("Take a photo to detect your emotion.")
    
    # The Camera Input Widget
    img_file = st.camera_input("Take a picture")

    if img_file is not None:
        with st.spinner("Analyzing your face... (This might take a moment)"):
            # Call the function from src/vision.py
            face_result = analyze_face_emotion(img_file)

            if "error" in face_result:
                st.error("Could not detect a face. Please try again with better lighting.")
            else:
                emotion = face_result['dominant_emotion']
                scores = face_result['all_scores']

                # Display the result
                st.success(f"Detected Emotion: **{emotion.upper()}**")
                
                # Show a bar chart of all emotions
                st.bar_chart(scores)