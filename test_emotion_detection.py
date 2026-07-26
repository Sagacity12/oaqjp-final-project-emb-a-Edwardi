import unittest
import sys
import os

# Add parent directory to path if not already there
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from EmotionDetection.emotion_detection import emotion_detector


class TestEmotionDetection(unittest.TestCase):
    """Unit tests for emotion_detector function"""

    def test_joy(self):
        """Test detection of joy emotion"""
        statement = "I am glad this happened"
        result = emotion_detector(statement)
        self.assertEqual(result['dominant_emotion'], 'joy')

    def test_anger(self):
        """Test detection of anger emotion"""
        statement = "I am really mad about this"
        result = emotion_detector(statement)
        self.assertEqual(result['dominant_emotion'], 'anger')

    def test_disgust(self):
        """Test detection of disgust emotion"""
        statement = "I feel disgusted just hearing about this"
        result = emotion_detector(statement)
        self.assertEqual(result['dominant_emotion'], 'disgust')

    def test_sadness(self):
        """Test detection of sadness emotion"""
        statement = "I am so sad about this"
        result = emotion_detector(statement)
        self.assertEqual(result['dominant_emotion'], 'sadness')

    def test_fear(self):
        """Test detection of fear emotion"""
        statement = "I am really afraid that this will happen"
        result = emotion_detector(statement)
        self.assertEqual(result['dominant_emotion'], 'fear')


if __name__ == '__main__':
    unittest.main()
