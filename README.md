# Emotion Detection Web App

This is a small Flask app I built that reads a piece of text and figures out the emotion behind it. It's powered by IBM's Watson NLP Emotion Prediction service, and it scores five emotions — anger, disgust, fear, joy, and sadness — then tells you which one is dominant.

You type something in, hit "Run Sentiment Analysis," and it comes back with a breakdown of all five emotions plus whichever one came out on top. If you leave the input blank or send something invalid, it doesn't crash — it just tells you to try again.

Under the hood it's a pretty standard Flask setup: `server.py` handles the routes and the error handling, `emotion_detection.py` does the actual talking to Watson's API, and there's a keyword-based version tucked away in the `EmotionDetection/` folder as an alternative approach. The front end is just a simple HTML page with a bit of JavaScript to handle the form.

**To run it yourself**, you'll need Python 3.12+ and pip. Clone the repo, install Flask and requests, and run `python server.py`. Then just open `localhost:5000` in your browser and start typing.

If you'd rather hit it directly, there's an API endpoint too — `/emotionDetector`, a GET request with a `textToAnalyze` parameter. Something like:

```
http://localhost:5000/emotionDetector?textToAnalyze=I am so happy today!
```

and you'll get back something like: *"For the given statement, the system response is 'anger': 0.0, 'disgust': 0.0, 'fear': 0.0, 'joy': 0.95 and 'sadness': 0.0. The dominant emotion is joy."* Send it nothing, and you'll just get "Invalid text! Please try again!" instead of an error page.

On the error-handling side: if Watson's API returns a 400 (which happens with blank or bad input), the detector quietly returns `None` for every emotion instead of blowing up, and the server catches that and turns it into a friendly message.

There's a full test suite covering all five emotions (`python -m unittest test_emotion_detection.TestEmotionDetection`), and it runs clean — 5 tests, all passing, in about 0.015 seconds. The code also scores a perfect 10/10 on PyLint, so it's reasonably clean as far as structure, docstrings, and naming go.

This was originally built as a final project, so it also includes a few specific deliverables from that assignment — updated error handling in the emotion detector function, matching error handling on the server side, and the fully PyLint-clean version of `server.py`.

It leans on Flask for the web framework, Watson NLP for the actual emotion detection, `requests` for hitting the API, `unittest` for testing, and PyLint for code quality checks. The Watson endpoint it talks to is `sn-watson-emotion.labs.skills.network`, using the `emotion_aggregated-workflow_lang_en_stock` model.

This was built for learning purposes, so if you've got suggestions or spot something worth improving, feel free to open an issue. License details are in the `LICENSE` file, and credit goes to IBM Skills Network for the Watson API this whole thing runs on, along with the usual thanks to the Flask and Python testing communities.

**Author:** Edwardi
