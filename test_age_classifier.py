import unittest
from age_classifier import AgeClassifier


class TestAgeClassifier(unittest.TestCase):

    def setUp(self):
        self.age_classifier = AgeClassifier()

    def test_toddler_age(self):
        self.assertEqual(self.age_classifier.classify_age(2), "Toddler")
        self.assertEqual(self.age_classifier.classify_age(4), "Toddler")

    def test_child_age(self):
        self.assertEqual(self.age_classifier.classify_age(5), "Child")
        self.assertEqual(self.age_classifier.classify_age(12), "Child")

    def test_teen_age(self):
        self.assertEqual(self.age_classifier.classify_age(13), "Teen")
        self.assertEqual(self.age_classifier.classify_age(19), "Teen")

    def test_adult_age(self):
        self.assertEqual(self.age_classifier.classify_age(20), "Adult")
        self.assertEqual(self.age_classifier.classify_age(64), "Adult")

    def test_senior_age(self):
        self.assertEqual(self.age_classifier.classify_age(65), "Senior")
        self.assertEqual(self.age_classifier.classify_age(80), "Senior")

    def test_negative_age(self):
        with self.assertRaises(ValueError):
            self.age_classifier.classify_age(-1)


if __name__ == '__main__':
    unittest.main()
    
    