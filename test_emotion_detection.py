import unittest
from EmotionDetection.emotion_detection import emotion_detection

class TestEmotionDetecctionFunction(unittest.TestCase):

    def test_joy(self):
        text1 = 'I am glad this happened'
        self.assertEqual(emotion_detection(text1)['dominant_emotion'], 'joy')
    
    def test_anger(self): 
        text2 = 'I am really mad about this'
        self.assertEqual(emotion_detection(text2)['dominant_emotion'], 'anger')        
        
    def test_disgust(self):
        text3 = 'I feel disgusted just hearing about this'
        self.assertEqual(emotion_detection(text3)['dominant_emotion'], 'disgust')
    
    def test_sadness(self):
        text4 = 'I am so sad about this'
        self.assertEqual(emotion_detection(text4)['dominant_emotion'], 'sadness')        
    
    def test_fear(self):    
        text5 = 'I am really afraid that this will happen'
        self.assertEqual(emotion_detection(text5)['dominant_emotion'], 'fear')

if __name__ == '__main__':
    unittest.main()
