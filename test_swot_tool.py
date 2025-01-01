
import unittest
from unittest.mock import MagicMock
from swot_analysis import SWOTAnalysis
from swot_ai_helper import SWOTAIHelper

class TestSWOTTool(unittest.TestCase):
    def setUp(self):
        # Mocking SWOTAnalysis
        self.mock_db = MagicMock()
        self.swot_analysis = SWOTAnalysis(self.mock_db)

        # Mocking SWOTAIHelper
        self.swot_ai_helper = SWOTAIHelper()
        self.swot_ai_helper.suggest_swot = MagicMock(
            return_value="Mocked AI suggestion"
        )

    def test_create_swot_entry(self):
        # Testing creation of a SWOT entry
        entry = self.swot_analysis.create_analysis(
            strengths="Strong customer loyalty",
            weaknesses="Limited distribution",
            opportunities="Emerging markets",
            threats="Competitors"
        )
        self.mock_db.insert_one.assert_called_once_with(entry)

    def test_ai_suggestion(self):
        # Testing AI suggestion mock
        suggestion = self.swot_ai_helper.suggest_swot("opportunity", "new market")
        self.assertEqual(suggestion, "Mocked AI suggestion")

if __name__ == "__main__":
    unittest.main()
