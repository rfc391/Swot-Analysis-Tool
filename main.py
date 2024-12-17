
import sys
from api.api import app
from gui.gui import FileApp

def main():
    if len(sys.argv) > 1 and sys.argv[1] == "api":
        app.run(host="0.0.0.0", port=5000)
    else:
        import tkinter as tk
        root = tk.Tk()
        app = FileApp(root)
        root.mainloop()

if __name__ == "__main__":
    main()
