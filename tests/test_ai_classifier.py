import unittest
from src.ai.swot_ai_engine import SWOTAI

class TestSWOTAI(unittest.TestCase):
    def setUp(self):
        self.ai = SWOTAI(offline=True)

    def test_strength_classification(self):
        label, confidence = self.ai.classify_entry("Our team has a strong research capability.")
        self.assertEqual(label, "Strength")

    def test_weakness_classification(self):
        label, confidence = self.ai.classify_entry("There is a lack of funding for the project.")
        self.assertEqual(label, "Weakness")

    def test_opportunity_classification(self):
        label, confidence = self.ai.classify_entry("There is an emerging market in South Asia.")
        self.assertEqual(label, "Opportunity")

    def test_threat_classification(self):
        label, confidence = self.ai.classify_entry("Cyber threats are becoming more complex.")
        self.assertEqual(label, "Threat")

if __name__ == '__main__':
    unittest.main()