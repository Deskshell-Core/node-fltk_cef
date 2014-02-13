#!/bin/bash

echo "=> Moving files around..."
[ ! -d "build/Release/fltk_cef.app" ] && mv -v \
	"build/Release/fltk_cef.node" \
	"build/Release/fltk_cef.app"
[ ! -d "build/Release/fltk_cef.app/Contents/Frameworks/node Helper.app" ] && cp -Rv \
	"build/Release/node Helper.app" \
	"build/Release/fltk_cef.app/Contents/Frameworks/"
[ ! -d "build/Release/fltk_cef.app/Contents/Frameworks/Chromium Embedded Framework.framework" ] && mv -v \
	"build/Release/fltk_cef.app/Contents/Frameworks/CEF.framework" \
	"build/Release/fltk_cef.app/Contents/Frameworks/Chromium Embedded Framework.framework"
[ ! -f "build/Release/fltk_cef.app/Contents/MacOS/fltk_cef.node" ] && mv -v \
	"build/Release/fltk_cef.app/Contents/MacOS/fltk_cef" \
	"build/Release/fltk_cef.app/Contents/MacOS/fltk_cef.node"

echo "=> Linking correctly."
USUAL="@executable_path/libcef.dylib"
install_name_tool -change \
	"$USUAL" \
	"@loader_path/../Frameworks/Chromium Embedded Framework.framework/Libraries/libcef.dylib" \
	"build/Release/fltk_cef.app/Contents/MacOS/fltk_cef.node"
install_name_tool -change \
	"$USUAL" \
	"@executable_path/../../../../Frameworks/Chromium Embedded Framework.framework/Libraries/libcef.dylib" \
	"build/Release/fltk_cef.app/Contents/Frameworks/node Helper.app/Contents/MacOS/node Helper"
