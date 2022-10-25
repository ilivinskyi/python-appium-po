import unittest
import pytest

from screens.main_screen import MainScreen as Main
from screens.login_screen import LoginScreen as Login
from screens.shared.menu_screen import MenuFragment as Menu
from data.test_data import TestData


@pytest.mark.android_ios
@pytest.mark.usefixtures("driver")
class LogoutTests(unittest.TestCase):
    @pytest.fixture(autouse=True)
    def classSetup(self, driver):
        self.data = TestData()
        self.main = Main(driver)
        self.login = Login(driver)
        self.menu = Menu(driver)

    def test_logout(self):
        self.main.wait_for_activity_indicator()
        self.login.login(email=self.data.credentials['login'],
                         password=self.data.credentials['password'])

        self.event.handle_permission(allow=True)
        self.menu.logout()
        self.main.wait_for_activity_indicator()
        assert self.main.logged_out()
