import os


class TestConst:
    WAIT_TIME = 30
    OS = os.getenv('os').lower()


class ByTypesEnum:
    ID = 'id'
    XPATH = 'xpath'
    ACCESSIBILITY_ID = 'accessibility id'
