class ConfigService:
    """
    singleton хранит конфигурации, заданные при запуске системы.
    """

    def __new__(cls, browser_config=None):
        """
        :param browser_config: конфигурация браузера (класс BrowserConfig)
        """
        if not hasattr(cls, 'instance'):
            cls.instance = super(ConfigService, cls).__new__(cls)
            cls.instance.__browser_config = browser_config
        return cls.instance

    def get_browser_config(self):
        return self.__browser_config
