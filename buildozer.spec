[app]
title = 增额寿简版建议书生成助手
package.name = zengeshou
package.domain = org.laohe
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.11.2
requirements = python3,kivy,pdfplumber,openpyxl,pillow
orientation = portrait
fullscreen = 0
android.permissions = INTERNET,READ_EXTERNAL_STORAGE,WRITE_EXTERNAL_STORAGE
android.api = 31
android.minapi = 21
android.archs = arm64-v8a, armeabi-v7a

# 关键配置：指定 SDK 和 NDK 路径，避免与系统环境冲突
android.sdk_path = /home/runner/android-sdk
android.ndk_path = /home/runner/.buildozer/android/platform/android-ndk-r25b
android.build_tools_version = 31.0.0
android.gradle_version = 7.6.3

[buildozer]
log_level = 2
warn_on_root = 1
