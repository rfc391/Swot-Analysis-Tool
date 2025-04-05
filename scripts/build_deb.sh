#!/bin/bash
set -e

echo "Building .deb package..."
APP_NAME="swot-analysis-tool"
VERSION="1.0.0"
BUILD_DIR="./deb_build"
INSTALL_DIR="${BUILD_DIR}/opt/${APP_NAME}"

rm -rf $BUILD_DIR
mkdir -p $INSTALL_DIR
cp -r ./src ./requirements.txt $INSTALL_DIR
mkdir -p ${BUILD_DIR}/DEBIAN

cp packaging/control ${BUILD_DIR}/DEBIAN/
cp packaging/postinst ${BUILD_DIR}/DEBIAN/
chmod 755 ${BUILD_DIR}/DEBIAN/postinst

dpkg-deb --build $BUILD_DIR "${APP_NAME}_${VERSION}.deb"
echo ".deb package created."