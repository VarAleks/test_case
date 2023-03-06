class BrowserConfig:
    """
    Конфигурация браузера.
    """
    CHROME = 'chrome'
    FIREFOX = 'firefox'

    def __init__(self, browser_base_url, browser=CHROME):
        """
        :param browser: тип используемого браузера
        """
        self.__browser = browser
        self.__elem_timeout = 30
        self.__browser_base_url = browser_base_url

    def get_browser(self):
        return self.__browser

    # def get_display_type(self):
    #     return self.__display_type
    #
    # def get_elem_timeout(self):
    #     return self.__elem_timeout
    #
    # def get_browser_base_url(self):
    #     return self.__browser_base_url
