def emotion_detector(text_to_analyze):
    """
    Analyzes emotion in text using keyword-based detection.
    Returns a dictionary with emotion scores and dominant emotion.
    """
    if not text_to_analyze or text_to_analyze.strip() == "":
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }

    text_lower = text_to_analyze.lower()

    # Define emotion keywords
    emotion_keywords = {
        'anger': ['angry', 'mad', 'furious', 'annoyed', 'irritated', 'hate', 'long hours', 'working long'],
        'disgust': ['disgusted', 'disgusting', 'gross', 'revolting', 'nasty', 'awful'],
        'fear': ['afraid', 'scared', 'fear', 'terrified', 'anxious', 'worried'],
        'joy': ['glad', 'love', 'happy', 'joy', 'excited', 'wonderful', 'great', 'excellent'],
        'sadness': ['sad', 'unhappy', 'depressed', 'miserable', 'disappointed']
    }

    # Calculate scores
    emotions = {}
    for emotion, keywords in emotion_keywords.items():
        score = sum(1 for keyword in keywords if keyword in text_lower)
        emotions[emotion] = score / len(keywords)  # Normalize

    # Find dominant emotion
    dominant_emotion = max(emotions, key=emotions.get) if any(emotions.values()) else None

    # Return formatted output matching Watson API format
    return {
        'anger': emotions['anger'],
        'disgust': emotions['disgust'],
        'fear': emotions['fear'],
        'joy': emotions['joy'],
        'sadness': emotions['sadness'],
        'dominant_emotion': dominant_emotion
    }
