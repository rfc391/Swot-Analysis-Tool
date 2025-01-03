
import os
import shutil
import logging
from typing import Tuple

class FileHandler:
    @staticmethod
    def _validate_paths(*paths) -> Tuple[bool, str]:
        for path in paths:
            if not os.path.exists(os.path.dirname(path)):
                return False, f"Directory does not exist for path: {path}"
        return True, ""

    @staticmethod
    def copy_file(src: str, dst: str) -> str:
        try:
            valid, error = FileHandler._validate_paths(src, dst)
            if not valid:
                return error

            shutil.copy2(src, dst)
            logging.info(f"Copied file from {src} to {dst}")
            return f"File successfully copied from {src} to {dst}"
        except Exception as e:
            logging.error(f"Error copying file: {e}")
            return f"Error copying file: {str(e)}"

    @staticmethod
    def move_file(src: str, dst: str) -> str:
        try:
            valid, error = FileHandler._validate_paths(src, dst)
            if not valid:
                return error

            shutil.move(src, dst)
            logging.info(f"Moved file from {src} to {dst}")
            return f"File successfully moved from {src} to {dst}"
        except Exception as e:
            logging.error(f"Error moving file: {e}")
            return f"Error moving file: {str(e)}"

    @staticmethod
    def delete_file(filepath: str) -> str:
        try:
            if not os.path.exists(filepath):
                return f"File does not exist: {filepath}"

            os.remove(filepath)
            logging.info(f"Deleted file {filepath}")
            return f"File {filepath} successfully deleted"
        except Exception as e:
            logging.error(f"Error deleting file: {e}")
            return f"Error deleting file: {str(e)}"
