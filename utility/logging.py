import logging


class LoggingHelper:
    @staticmethod
    def info(message):
        logging.info(message)

    @staticmethod
    def error(message):
        logging.error(message)

    @staticmethod
    def locator_found_message(locator):
        return f'Element {locator} found'

    @staticmethod
    def locator_check_message(locator):
        return f'Checking for {locator} element'

    @staticmethod
    def locator_not_found(locator):
        return f'Element {locator} not found'

    @staticmethod
    def clicking_locator(locator):
        return f'Clicking {locator} element'

    @staticmethod
    def waiting_for_click(locator):
        return f'Waiting for {locator} element to click it'

    @staticmethod
    def sending_text_to_element(text, locator):
        return f'Sending {text} to {locator} element'

    @staticmethod
    def getting_text_from_element(locator):
        return f'Getting text from {locator} element'

    @staticmethod
    def text_of_locator(locator, element):
        return f'Text of {locator} is {element.text}'

    @staticmethod
    def clearing_field(locator):
        return f'Clearing {locator} field'
