
import shutil
import os

class FileHandler:
    @staticmethod
    def copy_file(src, dst):
        try:
            shutil.copy2(src, dst)
            return f"File successfully copied from {src} to {dst}"
        except Exception as e:
            return f"Error copying file: {str(e)}"

    @staticmethod
    def move_file(src, dst):
        try:
            shutil.move(src, dst)
            return f"File successfully moved from {src} to {dst}"
        except Exception as e:
            return f"Error moving file: {str(e)}"

    @staticmethod
    def delete_file(filepath):
        try:
            os.remove(filepath)
            return f"File {filepath} successfully deleted"
        except Exception as e:
            return f"Error deleting file: {str(e)}"
