from data.strings import AndroidString as Android
from data.strings import IosStrings as Ios


class AndroidDriverData:

    @staticmethod
    def android_caps(version=Android.latest):
        desired_caps = dict(
            platformName=Android.android,
            app='path/to/file',
            platformVersion=version,
            deviceName=Android.device_name,
            appPackage=Android.app_package,
            clearSystemFiles=True,
            automationName=Android.automation_name,
            autoGrantPermissions=True,
            avd=Android.device_name,
            skipDeviceInitialization=False,
            audioPlayback=False,
            skipLogcatCapture=False,
            autoAcceptAlerts=True,
            wdaLaunchTimeout=120000,
            wdaStartupRetries=4,
            newCommandTimeout=180,
            fullReset=False,
            noReset=True,
            shouldTerminateApp=True,
            avdLaunchTimeout=300000,
            avdReadyTimeout=300000,
            isHeadless=False
        )
        return desired_caps


class IOSDriverData:
    @staticmethod
    def ios_caps(version):
        desired_caps = dict(
            platformName=Ios.ios,
            platformVersion=version,
            deviceName=Ios.device_name,
            automationName=Ios.automation_name,
            app='path/to/file',
            showXcodeLog=True,
            sendKeyStrategy='grouped',
            elementResponseAttributes=True,
            isAutomationEnabled=True,
            autoAcceptAlerts=True,
            autoDismissAlerts=False,
            connectHardwareKeyboard=True,
            wdaLaunchTimeout=120000,
            wdaStartupRetries=4,
            newCommandTimeout=180,
            fullReset=False,
            noReset=True,
            shouldTerminateApp=True,
            launchTimeout=20000,
            showIOSLog=True,
            isHeadless=False
        )
        return desired_caps
