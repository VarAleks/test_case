class BrowserConfig:
    """
    Конфигурация браузера.
    """
    CHROME = 'chrome'
    FIREFOX = 'firefox'

    def __init__(self, browser_base_url, browser=CHROME):
        """
        :param browser: тип используемого браузера
        :param browser_base_url: основной домен приложения (страницы)
        """
        self.__browser = browser
        self.__elem_timeout = 30
        self.__browser_base_url = browser_base_url

    def get_browser(self):
        return self.__browser

    def get_browser_base_url(self):
        return self.__browser_base_url
