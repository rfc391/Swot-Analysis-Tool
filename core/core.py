
import os
import shutil
import logging

# Setup logging
logging.basicConfig(
    filename="logs/operations.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

class FileHandler:
    @staticmethod
    def copy_file(src, dst):
        try:
            shutil.copy(src, dst)
            logging.info(f"Copied file from {src} to {dst}")
            return f"File copied from {src} to {dst}."
        except Exception as e:
            logging.error(f"Error copying file: {e}")
            return f"Error: {e}"

    @staticmethod
    def move_file(src, dst):
        try:
            shutil.move(src, dst)
            logging.info(f"Moved file from {src} to {dst}")
            return f"File moved from {src} to {dst}."
        except Exception as e:
            logging.error(f"Error moving file: {e}")
            return f"Error: {e}"

    @staticmethod
    def delete_file(filepath):
        try:
            os.remove(filepath)
            logging.info(f"Deleted file {filepath}")
            return f"File {filepath} deleted."
        except Exception as e:
            logging.error(f"Error deleting file: {e}")
            return f"Error: {e}"
