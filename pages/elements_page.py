from pages import pase_selectors
from pages.base_page import BasePage


class ElementsPage(BasePage):
    """
    Страница Elements
    """

    def __init__(self, browser):
        """
        :param browser: браузер, в котором будет работать страница
        """
        super().__init__(browser)
        self.select = pase_selectors.ElementsPage
        self.url = self.url + "/elements"

    def click_check_box_in_menu(self):
        """
        Клик на элемент CheckBox в меню
        """
        self.click_element(self.select.CHECK_BOX_IN_MENU)

    def should_be_elements_page(self):
        """
        Проверка загрузки страницы Elements
        """
        self.assert_presence(pase_selectors.ElementsPage.ELEMENTS_HEADER, "Страница Elements не загрузилась")
