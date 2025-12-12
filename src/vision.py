import cv2
import numpy as np
from PIL import Image
from deepface import DeepFace

def analyze_face_emotion(image_buffer):
    """
    Takes a photo object from Streamlit, converts it,
    and returns the dominant emotion.
    """
    try:
        # 1. Convert the image buffer (from camera) to a format Python understands
        img = Image.open(image_buffer)
        img_array = np.array(img)

        # 2. Convert RGB (standard) to BGR (OpenCV standard)
        img_array = cv2.cvtColor(img_array, cv2.COLOR_RGB2BGR)

        # 3. Use DeepFace to analyze emotions
        # 'enforce_detection=False' allows it to run even if it's not 100% sure there's a face
        predictions = DeepFace.analyze(img_array, actions=['emotion'], enforce_detection=False)
        
        # DeepFace returns a list, we take the first face detected
        result = predictions[0]
        
        return {
            "dominant_emotion": result['dominant_emotion'],
            "all_scores": result['emotion']
        }
    except Exception as e:
        return {"error": str(e)}