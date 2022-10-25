from data.constants import ByTypesEnum


class SystemLocators:
    ios_keyboard_done_button = (ByTypesEnum.XPATH, '//XCUIElementTypeButton[@name="Done"]')
    ios_activity_indicator = (ByTypesEnum.XPATH, '//XCUIElementTypeActivityIndicator')
