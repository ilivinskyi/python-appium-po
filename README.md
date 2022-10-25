# Automation Mobile Framework

## About
An automation framework for Android / iOS Applications built with Appium and Python.

## Requires
* Homebrew:
>     /usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)" 
* NPM & Node:
>     brew install node
```bash
    node -v
```
```bash
    npm -v
```
* ADB command line tool
* Appium console:
>     npm install -g appium@next
>     npm install -g appium-doctor
>     appium driver install uiautomator2
>     appium driver install xcuitest
```bash
    appium-doctor
```
* [**Appium desktop**](https://github.com/appium/appium-desktop/releases)
* [**Appium inspector**](https://github.com/appium/appium-inspector/releases)


## Install environment for running tests on Android devices:
* [**Android Studio**](https://developer.android.com/studio)
* [**Java**](https://www.oracle.com/java/technologies/downloads/#jdk18-mac)

## Install environment for running tests on iOS devices:
* XCode
* Carthage
>     brew install carthage

## How to Install and Run the Project:
1. Install Python version 3.10
2. Install pipenv using the command:
>     pip install pipenv
3. Run tests with command:
>    - pipenv run py.test --log-cli-level=INFO -s --reruns 1 --html=test-reports/report.html --os=android --os_version=12 tests/shared/test_login.py
>    - pipenv run py.test --log-cli-level=INFO -s --reruns 1 --html=test-reports/report.html --os=ios --os_version=15.5 tests/shared/test_login.py
4. Run tests with markers:
>- pipenv run py.test --log-cli-level=INFO -m "not ios" -s --reruns 1 --html=test-reports/report.html --os=android --os_version=12
>- pipenv run py.test --log-cli-level=INFO -m "ios" -s --reruns 1 --html=test-reports/report.html --os=ios --os_version=15.2
>- pipenv run py.test --log-cli-level=INFO -m "android_ios" -s --reruns 1 --html=test-reports/report.html --os=ios --os_version=15.2

## Useful commands:
* [**ADB commands**](https://developer.android.com/studio/command-line/adb)
>     adb devices
>     emulator -list-avds
>     cd ~/Library/Android/sdk/emulator && ./emulator -avd device_name
>     kill -9 $(lsof -t -i:4723)