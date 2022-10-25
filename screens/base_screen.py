import time

from typing import Union
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from utility.logging import LoggingHelper
from data.constants import TestConst as TestConst
from data.strings import CapabilitiesStrings as Capabilities

import locators.os_related_locators


class BaseScreen:
    _android = None
    caps = Capabilities
    test_const = TestConst

    def __init__(self, driver):
        self.driver = driver
        self._android = self.test_const.OS == self.caps.android

    logs = LoggingHelper()

    def get_element(self, locator, wait_time=TestConst.WAIT_TIME):
        self.logs.info(self.logs.locator_check_message(locator))
        element = None
        try:
            element = WebDriverWait(self.driver, wait_time).until(ec.presence_of_element_located(locator))
            self.logs.info(self.logs.locator_found_message(locator))
        except Exception as e:
            self.logs.error(f'Get element Error {e}')
            raise AssertionError(e)
        assert element
        return element

    def tap_to_coordinates(self, coordinates: Union[tuple]):
        self.logs.info(f"Try tap to coordinates {coordinates}")
        try:
            self.driver.tap([coordinates])
        except Exception as e:
            self.logs.error(f'Get element Error {e}')
            raise AssertionError(e)

    def get_elements(self, locator, wait_time=TestConst.WAIT_TIME):
        self.logs.info(self.logs.locator_check_message(locator))
        element = None
        try:
            element = WebDriverWait(self.driver, wait_time).until(ec.presence_of_all_elements_located(locator))
            self.logs.info(self.logs.locator_found_message(locator))
        except Exception as e:
            self.logs.error(f'Get element Error {e}')
            raise AssertionError(e)
        assert element
        return element

    def element_is_displayed(self, locator, wait_time=10):
        try:
            self.logs.info(self.logs.locator_check_message(locator))
            self.get_element(locator, wait_time)
            return True
        except:
            self.logs.info(f'{self.logs.locator_check_message(locator)} not found')
            return False

    def find_and_click_element(self, locator):
        try:
            self.logs.info(self.logs.locator_check_message(locator))
            element = self.get_element(locator)
            self.logs.info(self.logs.clicking_locator(locator))
            element.click()
        except Exception as e:
            self.logs.error(f'Find and click Error {e}')
            raise AssertionError(e)
        return True

    def wait_for_clickable_and_click(self, locator):
        self.logs.info(self.logs.waiting_for_click(locator))
        try:
            element = WebDriverWait(self.driver, TestConst.WAIT_TIME).until(ec.element_to_be_clickable(locator))
            self.logs.info(self.logs.clicking_locator(locator))
            element.click()
            return True
        except Exception as e:
            self.logs.error(f'Wait for clickable and click Error {e}')
            raise AssertionError(e)

    def clear_field(self, locator):
        self.logs.info(self.logs.clearing_field(locator))
        try:
            element = self.get_element(locator)
            element.clear()
        except Exception as e:
            self.logs.error(f'Clear Field Error {e}')
            raise AssertionError(e)

    def set_text(self, locator, text):
        self.logs.info(self.logs.sending_text_to_element(text, locator))
        try:
            element = self.get_element(locator)
            element.click()
            element.clear()
            element.set_value(text)
        except Exception as e:
            self.logs.error(f'Set Text Error {e}')
            raise AssertionError(e)
        return True

    def get_text(self, locator):
        element = None
        self.logs.info(self.logs.getting_text_from_element(locator))
        try:
            element = self.get_element(locator)
            self.logs.info(self.logs.text_of_locator(locator, element))
        except Exception as e:
            self.logs.error(f'Get Text Error {e}')
            raise AssertionError(e)
        assert element
        return element.text

    def wait_for_disappear(self, locator):
        try:
            self.get_element(locator)
            WebDriverWait(self.driver, 60).until_not(ec.presence_of_element_located(locator))

        except Exception as e:
            self.logs.error(f'Wait for disappear Error {e}')
            raise AssertionError(e)

    def hide_android_keyboard(self):
        try:
            self.driver.hide_keyboard()
        except Exception as e:
            self.logs.error(f'Hide keyboard Error {e}')
            raise AssertionError(e)

    def hide_ios_keyboard(self):
        self.logs.info("Hiding ios keyboard")
        try:
            done_button = self.get_element(locators.os_related_locators.SystemLocators.ios_keyboard_done_button)
            if done_button.is_displayed():
                done_button.click()
        except Exception as e:
            self.logs.error(f'Hide keyboard Error {e}')
            raise AssertionError(e)

    def swipe_method(self, start_location: Union[list, tuple], end_location: Union[list, tuple]):
        self.logs.info("Try to swipe")
        try:
            if type(start_location) is list:
                start_x, start_y = start_location[0], start_location[1]
            else:
                element_location = self.get_element(start_location).location
                element_size = self.get_element(start_location).size
                start_x = int(element_location['x'] + (element_size['width'] / 2))
                start_y = int(element_location['y'] + (element_size['height'] / 2))
            if type(end_location) is list:
                end_x, end_y = end_location[0], end_location[1]
            else:
                element_location = self.get_element(end_location).location
                element_size = self.get_element(end_location).size
                end_x = int(element_location['x'] + (element_size['width'] / 2))
                end_y = int(element_location['y'] + (element_size['height'] / 2))
            self.logs.info(f'Swipe from X:{start_x};Y:{start_y} to X:{end_x};Y:{end_y}')
            self.driver.swipe(start_x, start_y, end_x, end_y, 1000)
            time.sleep(1)
        except Exception as e:
            self.logs.error(f'Swipe Error {e}')
            raise AssertionError(e)
        self.logs.info("Swipe successful")

