#!/bin/bash
echo "Building AppImage..."
appimage-builder --recipe packaging/appimage-builder.yml
echo ".AppImage build complete."