[app]

# (str) Title of your application
title = 填空题练习-精简版

# (str) Package name
package.name = practiceapp

# (str) Package domain (needed for android/ios packaging)
package.domain = com.practiceapp

# (str) Source code where the main.py live
source.dir = .

# (list) Source files to include (let empty to include all the files)
source.include_exts = py,png,jpg,kv,atlas,json,docx,ttf,ttc

# (str) Application versioning (method 1)
version = 1.0

# (list) Application requirements
requirements = python3,kivy,python-docx,lxml,pillow

# (str) Presplash of the application
#presplash.filename = %(source.dir)s/data/presplash.png

# (str) Icon of the application
#icon.filename = %(source.dir)s/data/icon.png

# (str) Supported orientation (landscape, sensorLandscape, portrait, sensorPortrait or all)
orientation = portrait

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 0

[buildozer]

# (int) Log level (0 = error only, 1 = info, 2 = debug (with command output))
log_level = 2

# (int) Display warning if buildozer is run as root (0 = False, 1 = True)
warn_on_root = 1

[android]

# (int) Target Android API, should be as high as possible.
api = 31

# (int) Minimum API your APK will support.
minapi = 21

# (str) Android NDK version to use
ndk = 25b

# (str) Android SDK version to use
sdk = 31

# (bool) Use --private data storage (True) or --dir public storage (False)
private_storage = True

# (str) Android logcat filters to use
#android.logcat_filters = *:S python:D

# (bool) Copy library instead of making a libpymodules.so
#android.copy_libs = 1

# (str) The Android arch to build for, choices: armeabi-v7a, arm64-v8a, x86, x86_64
android.archs = arm64-v8a, armeabi-v7a

# (bool) enables Android auto backup feature (Android API >=23)
android.allow_backup = True

# (bool) Accept Android SDK license
accept_sdk_license = True
