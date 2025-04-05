
import unittest
from datetime import datetime
from swot_analysis import SWOTAnalysis

class MockDB:
    def __init__(self):
        self.entries = []

    def insert_one(self, entry):
        self.entries.append(entry)

    def find(self):
        return self.entries


class TestSWOTAnalysis(unittest.TestCase):
    def setUp(self):
        self.mock_db = MockDB()
        self.swot_analysis = SWOTAnalysis(self.mock_db)

    def test_create_analysis(self):
        entry = self.swot_analysis.create_analysis(
            strengths="Strong brand",
            weaknesses="Limited reach",
            opportunities="New market",
            threats="Competitors"
        )
        self.assertIn(entry, self.mock_db.find())

    def test_create_analysis_with_empty_fields(self):
        entry = self.swot_analysis.create_analysis(
            strengths="", weaknesses="", opportunities="", threats=""
        )
        self.assertIn(entry, self.mock_db.find())

if __name__ == "__main__":
    unittest.main()
