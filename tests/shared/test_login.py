import unittest
import pytest

from screens.main_screen import MainScreen as Main
from screens.login_screen import LoginScreen as Login
from data.test_data import TestData


@pytest.mark.usefixtures("driver")
@pytest.mark.android_ios
class LoginTests(unittest.TestCase):
    @pytest.fixture(autouse=True)
    def class_setup(self, driver):
        self.data = TestData()
        self.main = Main(driver)
        self.login = Login(driver)

    def test_positive_login(self):
        self.main.wait_for_activity_indicator()
        self.login.type_email(self.data.credentials['login'])
        self.login.type_password(self.data.credentials['password'])
        self.login.tap_login_button()
        self.event.handle_permission(allow=True)
        assert self.navigation.menu_visible()

