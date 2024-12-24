
import unittest
from core import FileHandler
import os

class TestFileHandler(unittest.TestCase):
    def setUp(self):
        self.test_file = "test_file.txt"
        self.copy_path = "copy_test_file.txt"
        self.move_path = "moved_test_file.txt"
        with open(self.test_file, "w") as f:
            f.write("Test content")

    def tearDown(self):
        for file in [self.test_file, self.copy_path, self.move_path]:
            if os.path.exists(file):
                os.remove(file)

    def test_copy_file(self):
        result = FileHandler.copy_file(self.test_file, self.copy_path)
        self.assertTrue(os.path.exists(self.copy_path))
        self.assertIn("copied", result)

    def test_move_file(self):
        result = FileHandler.move_file(self.test_file, self.move_path)
        self.assertTrue(os.path.exists(self.move_path))
        self.assertIn("moved", result)

    def test_delete_file(self):
        result = FileHandler.delete_file(self.test_file)
        self.assertFalse(os.path.exists(self.test_file))
        self.assertIn("deleted", result)

if __name__ == "__main__":
    unittest.main()
