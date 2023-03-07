from pages import pase_selectors
from pages.base_page import BasePage


class MainPage(BasePage):
    def __init__(self, browser):
        """
        :param browser: браузер, в котором будет работать страница
        """
        super().__init__(browser)

    def click_elements(self):
        """
        Кликает на карточку Elements на странице
        """
        self.click_element(pase_selectors.MainPage.EVENTS_BTN)
