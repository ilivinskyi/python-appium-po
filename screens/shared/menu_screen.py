import enum

from locators.menu_locators import MenuLocators
from locators.base_locators import BaseLocators
from screens.base_screen import BaseScreen


class MenuItems(enum.Enum):
    settings = 'Settings'
    logout = 'Logout'
    share = 'Share'


class MenuFragment(BaseScreen):
    _android = None

    def __init__(self, driver):
        super().__init__(driver)
        self._android = self.test_const.OS == self.caps.android

    def _open_menu(self):
        if self._android:
            self.swipe_method(BaseLocators.locators_for_scroll, [100, 50])
            self.swipe_method(BaseLocators.additional_android_scroll_locator, [100, 50])
        else:
            self.swipe_method(BaseLocators.locators_for_scroll, [100, 50])

    def logout(self):
        self.open_menu_item(MenuLocators().menu_item(MenuItems.logout))

    def open_menu_item(self, item: MenuItems):
        self._open_menu()
        self.find_and_click_element(MenuLocators.menu)
        self.find_and_click_element(MenuLocators().menu_item(item.value))


