#!/bin/bash
echo "Building Windows .exe using PyInstaller..."
pyinstaller packaging/pyinstaller.spec --onefile
echo ".exe build complete."