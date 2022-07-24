#!/bin/sh
pyinstaller -Fn pkg pkg.py
rm pkg.spec
rm -rf build/
mv dist/pkg ./
rmdir dist/