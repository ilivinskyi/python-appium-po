from screens.base_screen import BaseScreen
from locators.login_locators import LoginLocators


class LoginScreen(BaseScreen):
    _android = None

    def __init__(self, driver):
        super().__init__(driver)
        self._android = self.test_const.OS == self.caps.android

    def type_email(self, email):
        self.find_and_click_element(LoginLocators.login_field)
        self.clear_field(LoginLocators.login_field)
        self.set_text(LoginLocators.login_field, email)
        if not self._android:
            self.hide_ios_keyboard()

    def type_password(self, password):
        self.find_and_click_element(LoginLocators.password_field)
        self.clear_field(LoginLocators.password_field)
        self.set_text(LoginLocators.password_field, password)
        if not self._android:
            self.hide_ios_keyboard()
        else:
            self.hide_android_keyboard()

    def tap_login_button(self):
        self.find_and_click_element(LoginLocators.login_button)

    def tap_forget_password_button(self):
        self.find_and_click_element(LoginLocators.forgot_password_button)

    def tap_registration_button(self):
        self.find_and_click_element(LoginLocators.registration_button)

    def login(self, email, password):
        self.type_email(email)
        self.type_password(password)
        self.tap_login_button()
