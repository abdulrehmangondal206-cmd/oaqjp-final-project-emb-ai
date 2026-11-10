"""Basic test for the emotion detection application."""
import unittest
from emotion_detection import emotion_detector


class TestEmotionDetector(unittest.TestCase):
    """Basic tests for emotion_detector."""

    def test_response_contains_emotions(self):
        """The Watson response should contain emotion predictions."""
        result = emotion_detector("I am really mad about this")
        self.assertIn("emotionPredictions", result)


if __name__ == "__main__":
    unittest.main()
