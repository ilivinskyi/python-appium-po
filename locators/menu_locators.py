from data.constants import ByTypesEnum
from locators.base_locators import BaseLocators


class MenuLocators:
    menu = (ByTypesEnum.XPATH, '//android.view.ViewGroup[5]/android.widget.Button') if BaseLocators.android \
        else (ByTypesEnum.ACCESSIBILITY_ID, 'menuTabBar')

    logout_button = (ByTypesEnum.XPATH, '//android.widget.TextView[@text="Logout"]') if BaseLocators.android \
        else (ByTypesEnum.XPATH, '//XCUIElementTypeStaticText[@name="Logout"]')

    settings_button = (ByTypesEnum.XPATH, '//android.widget.TextView[@text="Settings"]') if BaseLocators.android \
        else (ByTypesEnum.XPATH, '//XCUIElementTypeStaticText[@name="Settings"]')

    @staticmethod
    def menu_item(item):
        return (ByTypesEnum.XPATH, f'//android.widget.TextView[@text="{item}"]') if BaseLocators.android \
            else (ByTypesEnum.XPATH, f'//XCUIElementTypeStaticText[@name="{item}"]')
