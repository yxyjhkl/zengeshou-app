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

# 明确指定 SDK 安装路径和 build-tools 版本
android.sdk_path = /opt/android-sdk
android.build_tools_version = 31.0.0

[buildozer]
log_level = 2
warn_on_root = 1
