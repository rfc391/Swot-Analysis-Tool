
import unittest
from unittest.mock import patch, MagicMock
import sys
import os

# Add project directory to sys.path for module resolution
sys.path.append("/mnt/data/swot_tool_extracted/Swot-Analysis-Tool-main")

from swot_analysis import SWOTAnalysisApp

class TestSWOTAnalysis(unittest.TestCase):
    @patch('tkinter.Tk', return_value=MagicMock())
    @patch('tkinter.StringVar', return_value=MagicMock())
    @patch('tkinter.IntVar', return_value=MagicMock())
    def setUp(self, mock_intvar, mock_stringvar, mock_tk):
        self.root = mock_tk()
        self.app = SWOTAnalysisApp(self.root)
    
    def test_initial_setup(self):
        self.assertIsNotNone(self.app)
        self.assertIsNotNone(self.app.root)
    
    def test_window_title(self):
        self.app.root.title = MagicMock(return_value="Advanced SWOT Analysis Tool")
        self.assertEqual(self.app.root.title(), "Advanced SWOT Analysis Tool")
    
    def test_window_geometry(self):
        self.app.root.geometry = MagicMock(return_value="900x800")
        self.assertEqual(self.app.root.geometry(), "900x800")

if __name__ == "__main__":
    unittest.main()
