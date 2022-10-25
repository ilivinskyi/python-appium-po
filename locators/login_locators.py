from data.constants import ByTypesEnum
from locators.base_locators import BaseLocators


class LoginLocators:
    login_field = (ByTypesEnum.ID, f'{BaseLocators.android_prefix}/loginUserEditText') if BaseLocators.android \
        else (ByTypesEnum.XPATH, '//XCUIElementTypeTextField')

    password_field = (ByTypesEnum.ID, f'{BaseLocators.android_prefix}/loginPasswordEditText') if BaseLocators.android \
        else (ByTypesEnum.XPATH, '//XCUIElementTypeSecureTextField')

    login_button = (ByTypesEnum.ID, f'{BaseLocators.android_prefix}/loginButton') if BaseLocators.android \
        else (ByTypesEnum.ACCESSIBILITY_ID, 'loginBtn')

    registration_button = (ByTypesEnum.ID, f'{BaseLocators.android_prefix}/registerButton') if BaseLocators.android \
        else (ByTypesEnum.XPATH, '//XCUIElementTypeStaticText[@name="Registration"]')

    forgot_password_button = (ByTypesEnum.ID, f'{BaseLocators.android_prefix}/loginForgotButton') if \
        BaseLocators.android else (ByTypesEnum.XPATH, '//XCUIElementTypeStaticText[@name="Forgot password?"]')
