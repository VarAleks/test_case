from pages import pase_selectors
from pages.base_page import BasePage


class ElementsPage(BasePage):
    def __init__(self, browser):
        """
        :param browser: браузер, в котором будет работать страница
        """
        super().__init__(browser)

    def should_be_elements_page(self):
        self.assert_presence(pase_selectors.ElementsPage.MAIN_HEADER, "Страница Elements не загрузилась")

