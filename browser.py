from selenium import webdriver

from services.browser_config import BrowserConfig
from services.config_service import ConfigService


class Browser:
    """
    Браузер, содержит логику работы с драйвером.
    """

    def __init__(self, browser_config=None):
        """
        :param browser_config: конфигурация браузера
        """
        self.browser_config = ConfigService().get_browser_config() if browser_config is None else browser_config
        self.driver = None

    def open(self):
        if self.driver is None:
            self.init_driver(self.browser_config)
        return self

    def init_driver(self, browser_conf):
        """
        Инициализация браузера по его конфигурации.

        :param browser_conf: конфигурация браузера (класс browser.BrowserConfig)
        """
        if browser_conf.get_browser() == BrowserConfig.CHROME:
            self.driver = webdriver.Chrome(executable_path='/binary/chromedriver')
        elif browser_conf.get_browser() == BrowserConfig.FIREFOX:
            self.driver = webdriver.Firefox(executable_path='/binary/geckodriver')
        self.driver.maximize_window()

    def refresh_page(self):
        self.driver.refresh()

    def close(self):
        """
        Закрытие браузера.
        """
        self.driver.quit()

    def get_driver(self):
        return self.driver
