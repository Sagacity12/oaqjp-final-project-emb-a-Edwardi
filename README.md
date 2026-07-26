# Emotion Detection Flask Application

A Flask-based web application that analyzes text input and detects emotions using the Watson NLP Emotion Prediction service. The application identifies five core emotions: anger, disgust, fear, joy, and sadness, and determines the dominant emotion.

## Features

- **Real-time Emotion Analysis**: Analyzes text input and returns emotion scores
- **Five Emotion Detection**: Detects anger, disgust, fear, joy, and sadness
- **Dominant Emotion Identification**: Identifies which emotion is most prominent
- **Error Handling**: Robust handling of blank or invalid inputs with user-friendly messages
- **RESTful API**: Clean API endpoint for emotion detection
- **Static Code Quality**: Achieved 10/10 PyLint score for code quality
- **Unit Tests**: Comprehensive test suite for all emotion types

## Project Structure

```
Flask/final_project/
├── EmotionDetection/
│   ├── __init__.py
│   └── emotion_detection.py      # Core emotion detection logic
├── static/
│   └── mywebscript.js            # Frontend JavaScript
├── templates/
│   └── index.html                # Web interface
├── server.py                     # Flask application server
├── emotion_detection.py          # Watson API integration
├── test_emotion_detection.py     # Unit tests
├── README.md                     # This file
├── LICENSE                       # License file
└── .gitignore                    # Git ignore rules
```

## Installation

### Prerequisites

- Python 3.12 or higher
- pip (Python package manager)

### Setup

1. Clone the repository:
```bash
git clone https://github.com/Sagacity12/oaqjp-final-project-emb-a-Edwardi
cd oaqjp-final-project-emb-a-Edwardi
```

2. Install required dependencies:
```bash
pip install flask requests
```

3. (Optional) Install development dependencies:
```bash
pip install pylint
```

## Usage

### Running the Application

1. Start the Flask server:
```bash
python server.py
```

2. Open your web browser and navigate to:
```
http://localhost:5000
```

3. Enter text in the input field and click "Run Sentiment Analysis" to see the emotion analysis results.

### API Endpoint

**Endpoint**: `/emotionDetector`
**Method**: GET
**Parameters**:
- `textToAnalyze` (string): The text to analyze for emotions

**Example Request**:
```
http://localhost:5000/emotionDetector?textToAnalyze=I am so happy today!
```

**Example Response** (Success):
```
For the given statement, the system response is 'anger': 0.0, 'disgust': 0.0, 'fear': 0.0, 'joy': 0.95 and 'sadness': 0.0. The dominant emotion is joy.
```

**Example Response** (Error - Blank Input):
```
Invalid text! Please try again!
```

## Error Handling

The application includes comprehensive error handling:

- **Status Code 400**: When the Watson API returns a 400 status (blank or invalid input), the emotion detector returns `None` for all emotion values
- **None Dominant Emotion**: When `dominant_emotion` is `None`, the server returns: "Invalid text! Please try again!"

### Error Handling Implementation

**emotion_detection.py** (lines 11-20):
```python
# Check for status code 400 (Bad Request - blank or invalid input)
if response.status_code == 400:
    return {
        'anger': None,
        'disgust': None,
        'fear': None,
        'joy': None,
        'sadness': None,
        'dominant_emotion': None
    }
```

**server.py** (lines 29-31):
```python
# Handle error case when dominant_emotion is None (blank input)
if dominant_emotion is None:
    return "Invalid text! Please try again!"
```

## Testing

Run the unit tests to verify functionality:

```bash
python -m unittest test_emotion_detection.TestEmotionDetection
```

### Test Coverage

The test suite includes tests for all five emotions:
- ✅ Joy detection
- ✅ Anger detection
- ✅ Disgust detection
- ✅ Sadness detection
- ✅ Fear detection

**Test Results**:
```
Ran 5 tests in 0.015s
OK
```

## Code Quality

### PyLint Score: 10/10 ⭐

The application maintains perfect code quality standards:
- Module-level docstrings
- Function-level docstrings
- PEP 8 compliance
- Clear variable naming
- Proper error handling
- Clean code structure

Run PyLint analysis:
```bash
python -m pylint server.py
```

## Technologies Used

- **Flask**: Web framework for Python
- **Watson NLP**: IBM Watson Natural Language Processing for emotion detection
- **Requests**: HTTP library for API calls
- **unittest**: Python testing framework
- **PyLint**: Static code analysis tool

## API Integration

This application integrates with the Watson Emotion Prediction API:
- **Endpoint**: `https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict`
- **Model**: `emotion_aggregated-workflow_lang_en_stock`

## Development

### File Descriptions

- **server.py**: Main Flask application with routes and error handling
- **emotion_detection.py**: Watson API integration with status code checking
- **EmotionDetection/emotion_detection.py**: Keyword-based emotion detection (alternative implementation)
- **test_emotion_detection.py**: Unit tests for emotion detection functionality
- **templates/index.html**: Web interface for user interaction
- **static/mywebscript.js**: Frontend JavaScript for form handling

## Assessment Deliverables

This project includes the following assessment deliverables:

1. **7a_error_handling_function**: Updated `emotion_detector` function with status_code 400 handling
2. **7b_error_handling_server**: Modified `server.py` with dominant_emotion None handling
3. **8a_server_modified**: Server.py file with 10/10 PyLint score

## Contributing

This is a final project for educational purposes. For suggestions or improvements, please open an issue.

## License

See the LICENSE file for details.

## Author

Edwardi - [GitHub Profile](https://github.com/Sagacity12)

## Acknowledgments

- IBM Skills Network for the Watson Emotion Prediction API
- Flask documentation and community
- Python testing best practices

---

**Project Status**: ✅ Complete - All requirements met with 10/10 code quality score
