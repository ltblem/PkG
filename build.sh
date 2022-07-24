#!/bin/sh
pyinstaller -Fn pkg pkg
rm pkg.spec
rm -rf build/
mv dist/pkg ./
rmdir dist/