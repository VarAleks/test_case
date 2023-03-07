
from services.browser_config import BrowserConfig
from services.config_service import ConfigService

def pytest_addoption(parser):
    """
    Добавление параметров запуска, которые могут быть заданы из командной строки при запуске тестов
    :return:
    """
    parser.addoption("--browser", action="store", default="chrome", help="Выбор браузера, на котором тестируем (chrome или firefox)")
    parser.addoption("--browser_url", action="store", default="https://demoqa.com", help="Базовый url страницы")

def pytest_configure(config):
    # инициализируем параметры системы
    ConfigService(
        BrowserConfig(config.getoption("--browser_url"), config.getoption("--browser")))
