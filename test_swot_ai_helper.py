
import unittest
from swot_ai_helper import SWOTAIHelper

class MockSWOTAIHelper(SWOTAIHelper):
    def __init__(self):
        pass

    def suggest_swot(self, category, description):
        # Mock AI behavior
        suggestions = {
            "strength": f"Strength: {description}",
            "weakness": f"Weakness: {description}",
            "opportunity": f"Opportunity: {description}",
            "threat": f"Threat: {description}"
        }
        return suggestions.get(category.lower(), "Invalid category")

class TestSWOTAIHelper(unittest.TestCase):
    def setUp(self):
        self.helper = MockSWOTAIHelper()

    def test_valid_category(self):
        result = self.helper.suggest_swot("strength", "brand loyalty")
        self.assertEqual(result, "Strength: brand loyalty")

    def test_invalid_category(self):
        result = self.helper.suggest_swot("unknown", "unknown aspect")
        self.assertEqual(result, "Invalid category")

if __name__ == "__main__":
    unittest.main()
