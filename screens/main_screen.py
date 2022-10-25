from screens.base_screen import BaseScreen
from locators.os_related_locators import SystemLocators
from locators.login_locators import LoginLocators


class MainScreen(BaseScreen):
    _android = None

    def __init__(self, driver):
        super().__init__(driver)
        self._android = self.test_const.OS == self.caps.android

    def wait_for_activity_indicator(self):
        if not self._android:
            self.wait_for_disappear(SystemLocators.ios_activity_indicator)
        else:
            # PASS is used here because this element disappears too quickly and tests do not handle this entity
            pass
        return True

    def logged_out(self):
        return self.element_is_displayed(LoginLocators.login_field)
