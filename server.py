"""Flask server for Emotion Detection Application"""

from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)


@app.route('/')
def index():
    """Render the main page"""
    return render_template('index.html')


@app.route('/emotionDetector')
def emotion_detector_route():
    """
    Analyze emotion from the text parameter and return formatted response
    """
    # Get the text to analyze from query parameters
    text_to_analyze = request.args.get('textToAnalyze')

    # Call the emotion_detector function
    response = emotion_detector(text_to_analyze)

    # Extract dominant emotion
    dominant_emotion = response['dominant_emotion']

    # Handle error case when dominant_emotion is None (blank input)
    if dominant_emotion is None:
        return "Invalid text! Please try again!"

    # Extract emotions
    anger = response['anger']
    disgust = response['disgust']
    fear = response['fear']
    joy = response['joy']
    sadness = response['sadness']

    # Format the response string
    formatted_response = (
        f"For the given statement, the system response is "
        f"'anger': {anger}, 'disgust': {disgust}, 'fear': {fear}, "
        f"'joy': {joy} and 'sadness': {sadness}. "
        f"The dominant emotion is {dominant_emotion}."
    )

    return formatted_response


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
