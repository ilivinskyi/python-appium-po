import logging
import os
import time
import pytest

from py._xmlgen import html
from datetime import datetime
from appium import webdriver
from selenium.common.exceptions import WebDriverException
from appium.webdriver.appium_service import AppiumService
from data.strings import ServerStrings as Server
from data.driver_data import AndroidDriverData
from data.driver_data import IOSDriverData

appium_service = AppiumService()
path_to_file = os.path.dirname(__file__)


@pytest.mark.optionalhook
def pytest_html_results_table_header(cells):
    cells.insert(3, html.th('Timestamp', class_='sortable time', col='time'))
    cells.pop()


@pytest.mark.optionalhook
def pytest_html_results_table_row(report, cells):
    cells.insert(3, html.td(datetime.now(), class_='col-time'))
    cells.pop()


@pytest.mark.hookwrapper
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    report.timestamp = str(item.function.__doc__)


def pytest_addoption(parser):
    # parser.addoption('--os', action='store', default='android', help='target OS')
    parser.addoption('--os', action='store', default='ios', help='target OS')
    # parser.addoption('--os_version', action='store', default='12', help='select os Version')
    # parser.addoption('--os_version', action='store', default='16.0', help='select os Version')


def pytest_configure(config):
    os.environ["os"] = config.getoption('os')
    os.environ["os_version"] = config.getoption('os_version')


@pytest.fixture(scope="function", autouse=True)
def take_screenshots(request):
    yield
    if request.session.testsfailed:
        driver = request.node.funcargs['driver']
        time.sleep(1)
        take_screenshot(driver, request)
        driver.quit()
    appium_down()


def take_screenshot(driver, request):
    test_reports_paths = f'test-reports/screenshots/{os.getenv("os").lower()}'
    full_test_reports_path = os.path.join(path_to_file, test_reports_paths)
    if not os.path.exists(full_test_reports_path):
        os.makedirs(full_test_reports_path)
    file_name = f'{request.node.nodeid}_{datetime.today().strftime("%Y-%m-%d_%H:%M")}_FAILED.png'.replace(
        "/", "_").replace("::", "__")
    screenshot_path = os.path.join(full_test_reports_path, file_name)
    driver.save_screenshot(screenshot_path)


@pytest.fixture(scope='function')
def driver():
    appium_local_host_url = f'{Server.server_url}:{Server.server_port}{Server.server_base_path}'
    logging.info('Preparing')
    logging.info('Starting driver and setting capabilities...')
    if os.getenv('os').lower() == 'android':
        caps = AndroidDriverData().android_caps(
            version=os.getenv('os_version'))
    elif os.getenv('os').lower() == 'ios':
        caps = IOSDriverData().ios_caps(version=os.getenv('os_version'))
    else:
        logging.error(f'{os.getenv("os_version")} is incorrect OS')
        raise Exception
    appium_up()
    logging.info(f'{os.getenv("os")} capabilities is set to: ')
    for keys, values in caps.items():
        logging.info(f'{keys} : {str(values)}')
    x = 0
    driver = None
    while x < 5:
        try:
            driver = webdriver.Remote(appium_local_host_url, desired_capabilities=caps)
            break
        except:
            time.sleep(5)
            x = x + 1
    if driver:
        logging.info(f'SessionID: {driver.session_id}')
        logging.info('Driver is ready')
    else:
        logging.error('WebDriver exception')
        raise WebDriverException

    yield driver
    driver.quit()
    logging.info('Closing driver')


def appium_up() -> None:
    log_appium_status()
    try:
        # it needs to remain these vars below for future implementations in order to run tests in parallel
        # later for each variable we need to add "--bootstrap-port" and "--webdriveragent-port"
        android_args = ['--base-path', Server().server_base_path,
                        '--port', Server().server_port]

        ios_args = ['--base-path', Server().server_base_path,
                    '--port', Server().server_port]

        appium_service.start(args=android_args if os.getenv('os').lower() == 'android' else ios_args)
    except Exception as e:
        raise Exception(f'Appium does not run. {e}')
    log_appium_status()


def appium_down() -> None:
    appium_service.stop()
    log_appium_status()


def log_appium_status():
    logging.info(f'Appium up: {appium_service.is_running}')
    logging.info(f'Appium listening: {appium_service.is_listening}')