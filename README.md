# 🤖 Multimodal Sentiment & Emotion Analysis

A real-time AI application that detects human sentiment using two different methods:
1. **Text Analysis:** Determines if a sentence is Positive, Negative, or Neutral.
2. **Facial Emotion Recognition:** Uses your camera to detect emotions (Happy, Sad, Angry, etc.) in real-time.

## 🚀 Live Demo
**[Click here to view the app] (Your_Streamlit_Share_Link_Goes_Here)**
*(Once you deploy, paste your Streamlit Cloud link above)*

## 🛠️ Tech Stack
* **Python 3.10+**
* **Streamlit** (Frontend Interface)
* **TextBlob** (NLP for Text Sentiment)
* **DeepFace** (Computer Vision for Emotion Detection)
* **OpenCV** (Image Processing)

## 📂 Project Structure

sentiment-face-app/
├── src/
│   ├── analyzer.py    # Logic for text sentiment
│   └── vision.py      # Logic for facial emotion recognition
├── app.py             # Main Streamlit application
├── requirements.txt   # List of dependencies
└── README.md          # Project documentation

====================================================================================
💿 How to Run Locally
If you want to run this on your own computer, follow these steps:

1. Clone the repository
git clone [https://github.com/YourUsername/sentiment-face-app.git](https://github.com/YourUsername/sentiment-face-app.git)
cd sentiment-face-app

2. Create a Virtual Environment
Bash

# Windows
python -m venv venv
.\venv\Scripts\activate

# Mac/Linux
python3 -m venv venv
source venv/bin/activate
3. Install Dependencies
Bash

pip install -r requirements.txt

4. Run the App
Bash

streamlit run app.py

📸 Features

    Text Mode: Type any sentence to get a Polarity Score (-1 to +1) and Subjectivity Score.

    Camera Mode: Snap a photo to instantly detect your current emotion using Deep Learning.

📝 License

This project is open-source and available for educational purposes.


### 💡 Pro Tip: Add Your Screenshots!
Since you already took screenshots of the app working, you can add them to your README to make it look amazing.
1.  Upload your screenshots (like `image_ab7d6a.jpg`) to your GitHub repository (drag and drop them).
2.  Add this line inside the README code above:
    ```markdown
    ![App Screenshot](image_ab7d6a.jpg)
    ```

This makes your project look very professional for your portfolio!
