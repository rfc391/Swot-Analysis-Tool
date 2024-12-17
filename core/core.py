
import os

def copy_file(src, dst):
    try:
        with open(src, 'rb') as fsrc:
            with open(dst, 'wb') as fdst:
                fdst.write(fsrc.read())
        return f"Copied {src} to {dst}."
    except Exception as e:
        return f"Error: {e}"
            