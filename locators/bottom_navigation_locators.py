from data.constants import ByTypesEnum
from locators.base_locators import BaseLocators


class BottomNavigationLocators:
    menu_android_prefix = '//androidx.recyclerview.widget.RecyclerView/'

    menu = (ByTypesEnum.XPATH, menu_android_prefix + 'android.view.ViewGroup[5]/android.widget.Button') \
        if BaseLocators.android else (ByTypesEnum.ACCESSIBILITY_ID, 'menuTabBar')
