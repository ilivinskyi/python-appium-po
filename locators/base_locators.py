from data.constants import TestConst
from data.constants import ByTypesEnum
from data.strings import CapabilitiesStrings as Capabilities, AndroidString


class BaseLocators:
    android = TestConst.OS == Capabilities.android
    android_prefix = AndroidString().id_prefix
    locators_for_scroll = (ByTypesEnum.XPATH, 'android.view.ViewGroup[5]/android.widget.Button') \
        if android else (ByTypesEnum.ACCESSIBILITY_ID, 'elementToSwipe')
    additional_android_scroll_locator = (ByTypesEnum.XPATH, 'android.view.ViewGroup[5]/android.widget.Button')
