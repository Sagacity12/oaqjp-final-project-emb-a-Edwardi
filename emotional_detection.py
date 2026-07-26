from emotion_detection import emotion_detector

def emotion_detector(text_to_analyze):
    """
    Simple rule-based emotion detector using keyword matching.
    Returns a dictionary with emotion scores.
    """
    text_lower = text_to_analyze.lower()

    # Define emotion keywords
    emotion_keywords = {
        'joy': ['love', 'happy', 'joy', 'excited', 'wonderful', 'great', 'excellent'],
        'sadness': ['sad', 'unhappy', 'depressed', 'miserable', 'disappointed'],
        'anger': ['angry', 'mad', 'furious', 'annoyed', 'irritated', 'hate'],
        'fear': ['afraid', 'scared', 'fear', 'terrified', 'anxious', 'worried'],
        'surprise': ['surprise', 'amazed', 'shocked', 'astonished']
    }

    # Calculate scores
    emotions = {}
    for emotion, keywords in emotion_keywords.items():
        score = sum(1 for keyword in keywords if keyword in text_lower)
        emotions[emotion] = score / len(keywords)  # Normalize

    # Find dominant emotion
    dominant_emotion = max(emotions, key=emotions.get) if any(emotions.values()) else 'neutral'

    return {
        'emotions': emotions,
        'dominant_emotion': dominant_emotion
    }

# Test the function
if __name__ == "__main__":
    result = emotion_detector("I love this new technology.")
    print(f"Emotions detected: {result['emotions']}")
    print(f"Dominant emotion: {result['dominant_emotion']}")

result = emotion_detector("I love this new technology.")
print(result)
