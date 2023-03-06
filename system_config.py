class SystemConfig:
    """
    Конфигурация системы.
    """

    def __init__(self, base_url, auth_url, api_url):
        """
        :param base_url: базовый url системы
        :param api_url: url апи системы
        """
        self.__base_url = base_url
        self.__api_url = api_url
        self.__auth_url = auth_url

    def get_base_url(self):
        return self.__base_url

    def get_api_url(self):
        return self.__api_url

    def get_auth_url(self):
        return self.__auth_url
